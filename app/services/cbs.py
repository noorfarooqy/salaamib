from decimal import Decimal
from typing import Optional, Dict, Any
from app.core.config import settings
from datetime import datetime
import aiohttp
from app.services.xml_parser import CBSXMLParser
import logging
import os
from pathlib import Path

from app.services.logger import cbs_logger

class CBSConnectionError(Exception):
    """Exception raised for CBS connection errors."""
    pass

class FlexcubeService:
    def __init__(self):
        self.headers = {
            'Content-Type': 'text/xml;charset=UTF-8',
            'SOAPAction': ''
        }
        self.logger = logging.getLogger(__name__)

    def _get_branch_code(self, account_number: str) -> str:
        """Extract branch code from account number"""
        if len(account_number) == 10:
            return account_number[:3]
        return "001"  # Default branch if account number format is invalid

    def _create_header(self, service: str, operation: str, branch: str = "001") -> Dict[str, str]:
        """Create FCUBS header for requests"""
        # Order matters for the header fields
        return {
            "SOURCE": settings.CBS_SOURCE,
            "UBSCOMP": settings.CBS_UBSCOMP,
            "USERID": settings.CBS_USERID,
            "BRANCH": branch,
            "SERVICE": service,
            "OPERATION": operation,
        }

    def _create_soap_envelope(self, header: Dict[str, str], body: Dict[str, Any]) -> str:
        """Create SOAP envelope with header and body"""
        # Format header XML with fcub namespace
        header_xml = "\n".join([f"<fcub:{k}>{v}</fcub:{k}>" for k, v in header.items()])
        
        # Format body XML recursively with fcub namespace
        def dict_to_xml(d: Dict[str, Any], indent: int = 0) -> str:
            xml = []
            for k, v in d.items():
                if isinstance(v, dict):
                    inner_xml = dict_to_xml(v, indent + 4)
                    xml.append(f"{' ' * indent}<fcub:{k}>\n{inner_xml}\n{' ' * indent}</fcub:{k}>")
                else:
                    xml.append(f"{' ' * indent}<fcub:{k}>{v}</fcub:{k}>")
            return "\n".join(xml)
        
        body_xml = dict_to_xml(body["FCUBS_BODY"])  # Remove extra nesting
        service = header["SERVICE"]
        operation = header["OPERATION"]
        
        return f"""<?xml version="1.0" encoding="UTF-8"?>
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:fcub="http://fcubs.ofss.com/service/{service}">
            <soapenv:Header/>
            <soapenv:Body>
                <fcub:{operation.upper()}_FSFS_REQ>
                    <fcub:FCUBS_HEADER>
                        {header_xml}
                    </fcub:FCUBS_HEADER>
                    <fcub:FCUBS_BODY>
                        {body_xml}
                    </fcub:FCUBS_BODY>
                </fcub:{operation.upper()}_FSFS_REQ>
            </soapenv:Body>
        </soapenv:Envelope>
        """

    async def _make_soap_request(
        self,
        service: str,
        operation: str,
        body: Dict[str, Any],
        branch: str = "001"
    ) -> str:
        """Make a SOAP request to CBS."""
        try:
            # Construct the appropriate service URL based on the service type
            if service == "FCUBSCustomerService":
                service_url = f"{settings.CBS_SOAP_URL}/FCUBSCustomerService/FCUBSCustomerService"
            elif service == "FCUBSRTService":
                service_url = f"{settings.CBS_SOAP_URL}/FCUBSRTService/FCUBSRTService"
            elif service == "RTService":
                service_url = f"{settings.CBS_SOAP_URL}/RTService/RTService"
            elif service == "CustomerService":
                service_url = f"{settings.CBS_SOAP_URL}/CustomerService/CustomerService"
            elif service == "AccountService":
                service_url = f"{settings.CBS_SOAP_URL}/AccountService/AccountService"
            else:
                service_url = f"{settings.CBS_SOAP_URL}/{service}/{service}"

            # Create SOAP envelope with proper header and body
            header = self._create_header(service, operation, branch)
            soap_envelope = self._create_soap_envelope(header, body)

            # Log request details
            cbs_logger.log_request(service, operation, soap_envelope)

            # Make the request using aiohttp
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    service_url,
                    data=soap_envelope,
                    headers={
                        "Content-Type": "text/xml;charset=UTF-8",
                        "SOAPAction": f"{service}#{operation}",
                    },
                ) as response:
                    if response.status != 200:
                        cbs_logger.log_error(f"Failed making SOAP request to CBS {service} {operation}: {response.status}")
                        raise CBSConnectionError(f"Failed to connect to CBS: HTTP {response.status}")
                    
                    response_text = await response.text()
                    cbs_logger.log_response(response_text)
                    return response_text

        except aiohttp.ClientError as e:
            cbs_logger.log_error(f"HTTP error during SOAP request: {str(e)}")
            raise CBSConnectionError(f"Failed to connect to CBS: {str(e)}")
        except Exception as e:
            cbs_logger.log_error(f"Unexpected error during SOAP request: {str(e)}")
            raise CBSConnectionError(f"Unexpected error during CBS request: {str(e)}")

    async def verify_cif(self, cif_number: str) -> Dict[str, Any]:
        """Verify customer CIF number and validate status"""
        try:
            # First verify customer details
            body = {
                "FCUBS_BODY": {
                    "Stvws-Stdcifqy-Query-IO": {
                        "KEY_ID": "C",
                        "VALUE": cif_number
                    }
                }
            }
            
            response = await self._make_soap_request("FCUBSCustomerService", "QueryCustomerDetails", body)
            cbs_logger.log_response(response)
            if not response:
                self.logger.error(f"Failed verifying CIF from CBS {cif_number}: No response {response}")
                return {
                    "is_valid": False,
                    "error": "Customer not found"
                }
            
            # Parse the XML response using the new parser
            body, msg_status = CBSXMLParser.parse_response(response, "QUERYCUSTOMERDETAILS")
            
            if "SUCCESS" not in msg_status:
                self.logger.error(f"Failed verifying CIF from CBS {cif_number}: {body}")
                return {
                    "is_valid": False,
                    "error": "Customer not found - No Success Message"
                }

            # Get customer information using the parser
            customer_info = CBSXMLParser.get_customer_info(body)

            
            # Extract customer data with all fields
        
            
            # Check customer status flags
            if customer_info.get("FROZEN_STATUS") == "Y":
                return {
                    "is_valid": False,
                    "error": "Customer account is frozen"
                }
            if customer_info.get("DECEASED_STATUS") == "Y":
                return {
                    "is_valid": False,
                    "error": "Invalid customer status"
                }
            if customer_info.get("BLACKLIST_STATUS") == "Y":
                return {
                    "is_valid": False,
                    "error": "Customer is not eligible for internet banking"
                }

            cbs_logger.log_info(f"---------------------completed customer validation---------------------")

            # Now get customer accounts
            accounts_response = await self.get_account_details(cif_number)
            cbs_logger.log_info(f"Accounts response: {accounts_response}")
            if not accounts_response:
                return {
                    "is_valid": False,
                    "error": f"No active accounts found for customer {cif_number}"
                }
            if not accounts_response["is_valid"]:
                return accounts_response
            cbs_logger.log_info(f"---------------------completed account validation---------------------")

            # Check if at least one account i
            # All validations passed - return all customer fields
            return {
                "is_valid": True,
                "customer_id": customer_info.get("CUSTOMER_ID", ""),
                "email": customer_info.get("EMAIL", ""),
                "first_name": customer_info.get("FIRST_NAME", ""),
                "last_name": customer_info.get("LAST_NAME", ""),
                "gender": customer_info.get("GENDER", ""),
                "title": customer_info.get("TITLE", ""),
                "short_name": customer_info.get("SHORT_NAME", ""),
                "address_line1": customer_info.get("ADDRESS_LINE1", ""),
                "address_line2": customer_info.get("ADDRESS_LINE2", ""),
                "address_line3": customer_info.get("ADDRESS_LINE3", ""),
                "address_line4": customer_info.get("ADDRESS_LINE4", ""),
                "address_country": customer_info.get("ADDRESS_COUNTRY", ""),
                "mobile": customer_info.get("MOBILE_NO", ""),
                "is_verified": customer_info.get("IS_VERIFIED", ""),
                "nationality": customer_info.get("NATIONALITY", ""),
                "unique_id_name": customer_info.get("UNIQUE_ID_NAME", ""),
                "unique_id_value": customer_info.get("UNIQUE_ID_VALUE", ""),
                "created_at": customer_info.get("CREATED_AT", ""),
                "updated_at": customer_info.get("UPDATED_AT", ""),
                "customer_type": customer_info.get("CUSTOMER_TYPE", ""),
                "category": customer_info.get("CATEGORY", ""),
                "accounts": accounts_response["accounts"]
            }
                
            
        except Exception as e:
            cbs_logger.log_error(f"Error verifying CIF {cif_number}: {str(e)}")
            return {
                "is_valid": False,
                "error": str(e)
            }

    async def get_account_details(self, cif_number: str) -> list:
        """Get account details from CBS"""
        try:
            body = {
                "FCUBS_BODY": {
                    "Sttms-Customer-IO": {
                        "CUSTNO": cif_number
                    }
                }
            }
            
            response = await self._make_soap_request("FCUBSCustomerService", "QueryCustAccDetail", body)
            try:
                # Parse XML response using CBSXMLParser
                accounts, msg_status = CBSXMLParser.parse_response(response, "QUERYCUSTACCDETAIL")
                if "SUCCESS" not in msg_status:
                    error = ''
                    return {
                        "is_valid": False,
                        "error": f"Failed getting account details from CBS - Account not found for customer {cif_number}: {response}"
                    }
                if not response:
                    return {
                        "is_valid": False,
                        "error": f"Failed getting account details from CBS - Account not found for customer {cif_number}: {response}"
                    }
                accounts = CBSXMLParser.get_account_info(accounts)
                cbs_logger.log_info(f"accounts: {accounts}")
            except Exception as e:
                cbs_logger.log_error(f"Error parsing XML response for customer acc: {str(e)}")
                return {
                    "is_valid": False,
                    "error": f"Error parsing XML response for customer acc: {str(e)}"
                }
            cbs_logger.log_response({'checking accounts': accounts})
            accounts_list= [{
                "accountNumber": acc.get("CUST_AC_NO"),
                "accountType": acc.get("ACCOUNT_TYPE"),
                "currency": acc.get("CCY"),
                "accountName": acc.get("AC_DESC"),
                "openDate": acc.get("AC_OPEN_DATE"),
                "status": acc.get("ACC_STATUS"),
                "branch": acc.get("BRANCH_CODE"),
                "address": {
                    "line1": acc.get("ADDRESS1", ""),
                    "line2": acc.get("ADDRESS2", ""), 
                    "line3": acc.get("ADDRESS3", ""),
                    "city": acc.get("ADDRESS4", "")
                }
            } for acc in accounts]
            cbs_logger.log_info(f"accounts_list: {accounts_list}")
            return {
                "is_valid": True,
                "accounts": accounts_list
            }
            
        except Exception as e:
            cbs_logger.log_error(f"Error getting account details: {str(e)}")
            return {
                "is_valid": False,
                "error": f"Error getting account details: {str(e)}"
            }

    async def get_cbs_account_balance(self, account_number: str) -> Dict[str, Any]:
        """Get account balance"""
        try:
            branch = self._get_branch_code(account_number)
            body = {
                "Custbal-IO": {
                    "CUST_AC_NO": account_number,
                    "BRHCODE": branch
                }
            }
            cbs_logger.log_info(f"Fetching balance for account: {account_number} on branch {branch}")
            
            response = await self._make_soap_request("FCUBSAccService", "QueryAcctBal", body, branch)
            
            if response:
                balance = response["Custbal-Full"]["Custbal"]
                return {
                    "account_number": balance.CUST_AC_NO,
                    "currency": balance.CCY,
                    "available_balance": Decimal(str(balance.AVLBAL)),
                    "current_balance": Decimal(str(balance.CURBAL)),
                    "branch": branch
                }
            return None
            
        except Exception as e:
            cbs_logger.log_error(f"Error getting account balance: {str(e)}")
            return None

    async def get_transaction_history(
        self, 
        account_number: str, 
        from_date: str, 
        to_date: str
    ) -> Optional[list]:
        """Get account transaction history"""
        try:
            branch = self._get_branch_code(account_number)
            header = self._create_header("FCUBSAccService", "QueryAccTrns", branch)
            body = {
                "AccTrns-IO": {
                    "CUST_AC_NO": account_number,
                    "FROM_DT": from_date,
                    "TO_DT": to_date,
                    "BRHCODE": branch
                }
            }
            
            response = await self._make_soap_request("FCUBSAccService", "QueryAccTrns", body, branch)
            
            if response:
                transactions = response["AccTrns-Full"]["AccTrns"]
                return [{
                    "reference": txn.TXN_REF_NO,
                    "date": txn.VALUE_DT,
                    "amount": Decimal(str(txn.AMOUNT)),
                    "currency": txn.CCY,
                    "type": "debit" if txn.DRCR == "D" else "credit",
                    "description": txn.TXN_DESC,
                    "status": "completed",
                    "branch": branch
                } for txn in transactions]
            return None
            
        except Exception as e:
            cbs_logger.log_error(f"Error getting transaction history: {str(e)}")
            return None

    async def validate_transfer(
        self,
        from_account: str,
        to_account: str,
        amount: Decimal
    ) -> Dict[str, Any]:
        """Validate transfer with Core Banking System"""
        try:
            # First check if accounts exist and are active
            from_acc = await self.get_account_details(from_account)
            to_acc = await self.get_account_details(to_account)
            
            if not from_acc or not to_acc:
                return {
                    "is_valid": False,
                    "requires_otp": False,
                    "message": "One or both accounts not found",
                    "reference": ""
                }
            
            if from_acc["status"] != "ACTIVE" or to_acc["status"] != "ACTIVE":
                return {
                    "is_valid": False,
                    "requires_otp": False,
                    "message": "One or both accounts are not active",
                    "reference": ""
                }
            
            # Check balance
            balance = await self.get_cbs_account_balance(from_account)
            if not balance or balance["available_balance"] < amount:
                return {
                    "is_valid": False,
                    "requires_otp": False,
                    "message": "Insufficient funds",
                    "reference": ""
                }
            
            # Generate reference
            reference = f"TRF{datetime.now().strftime('%Y%m%d%H%M%S')}"
            
            # For amounts above threshold, require OTP
            requires_otp = amount > Decimal("10000")
            
            return {
                "is_valid": True,
                "requires_otp": requires_otp,
                "message": "Transfer validation successful",
                "reference": reference,
                "from_branch": from_acc["branch"],
                "to_branch": to_acc["branch"]
            }
            
        except Exception as e:
            return {
                "is_valid": False,
                "requires_otp": False,
                "message": str(e),
                "reference": ""
            }

    async def execute_transfer(
        self,
        from_account: str,
        to_account: str,
        amount: Decimal,
        reference: str,
        description: str,
        otp: str = None
    ) -> Dict[str, Any]:
        """Execute transfer through Core Banking System"""
        try:
            from_branch = self._get_branch_code(from_account)
            header = self._create_header("FCUBSAccService", "CreateTransaction", from_branch)
            body = {
                "Transaction-IO": {
                    "XREF": reference,
                    "BRN": from_branch,
                    "PRD": "FTCR",  # Fund Transfer Credit
                    "DRCR": "D",    # Debit first account
                    "CUST_AC_NO": from_account,
                    "CUST_NO": "",  # Will be populated from account
                    "CCY": "KES",   # Default to KES
                    "AMOUNT": str(amount),
                    "VALUE_DT": datetime.now().strftime("%Y-%m-%d"),
                    "TXN_DT": datetime.now().strftime("%Y-%m-%d"),
                    "NARRATIVE": description,
                    "RELATED_ACCOUNT": to_account,
                    "MIS_HEAD": ""
                }
            }
            
            if otp:
                body["Transaction-IO"]["OTP"] = otp
            
            response = await self._make_soap_request("FCUBSAccService", "CreateTransaction", body, from_branch)
            
            if response:
                return {
                    "status": "success",
                    "message": "Transfer successful",
                    "transaction_reference": response["Transaction-Full"]["Transaction"].XREF,
                    "from_branch": from_branch,
                    "to_branch": self._get_branch_code(to_account)
                }
            
            return {
                "status": "failed",
                "message": "Transfer failed",
                "transaction_reference": ""
            }
            
        except Exception as e:
            return {
                "status": "failed",
                "message": str(e),
                "transaction_reference": ""
            }

    async def create_amount_block(
        self,
        account: str,
        amount: Decimal,
        reference: str,
        branch: str,
        phone: str
    ) -> Dict[str, Any]:
        """Create amount block in CBS"""
        try:
            body = {
                "FCUBS_BODY": {
                    "Amount-Blocks-Full": {
                        "ACC": account,
                        "AMTBLKNO": reference,
                        "AMT": str(amount),
                        "ABLKTYPE": "F",
                        "REFERENCE_NO": reference,
                        "HPCODE": "MPESA",
                        "HOLDDESC": f"HOLD MPESA {reference}",
                        "BRANCH": branch,
                        "BENEFICIARY_TELEPHONE": phone,
                        "VERIFY_AVL_BAL": "Y"
                    }
                }
            }
            
            response = await self._make_soap_request(
                "FCUBSCustomerService", 
                "CreateAmtBlk", 
                body, 
                branch
            )
            
            if not response:
                return {
                    "status": "failed",
                    "message": "Failed to create amount block"
                }
                
            # Parse response using CBSXMLParser
            body, msg_status = CBSXMLParser.parse_response(response, "CREATEAMTBLK")
            
            if "SUCCESS" in msg_status:
                return {
                    "status": "success",
                    "message": "Amount block created successfully",
                    "reference": reference
                }
                
            return {
                "status": "failed",
                "message": "Failed to create amount block",
                "error": body.get("error_description", "Unknown error")
            }
            
        except Exception as e:
            return {
                "status": "failed",
                "message": str(e)
            }

    async def close_amount_block(
        self,
        account: str,
        reference: str,
        branch: str
    ) -> Dict[str, Any]:
        """Close amount block in CBS"""
        try:
            body = {
                "FCUBS_BODY": {
                    "Amount-Blocks-Full": {
                        "ACC": account,
                        "AMTBLKNO": reference
                    }
                }
            }
            
            response = await self._make_soap_request(
                "FCUBSCustomerService", 
                "CloseAmtBlk", 
                body, 
                branch
            )
            
            if not response:
                return {
                    "status": "failed",
                    "message": "Failed to close amount block"
                }
                
            body, msg_status = CBSXMLParser.parse_response(response, "CLOSEAMTBLK")
            
            if "SUCCESS" in msg_status or "Record Successfully Closed and Authorized" in str(body):
                return {
                    "status": "success",
                    "message": "Amount block closed successfully"
                }
                
            return {
                "status": "failed",
                "message": "Failed to close amount block",
                "error": body.get("error_description", "Unknown error")
            }
            
        except Exception as e:
            return {
                "status": "failed",
                "message": str(e)
            }

    async def reopen_amount_block(
        self,
        account: str,
        reference: str,
        branch: str
    ) -> Dict[str, Any]:
        """Reopen amount block in CBS"""
        try:
            body = {
                "FCUBS_BODY": {
                    "Amount-Blocks-Full": {
                        "ACC": account,
                        "AMTBLKNO": reference
                    }
                }
            }
            
            response = await self._make_soap_request(
                "FCUBSCustomerService", 
                "ReopenAmtBlk", 
                body, 
                branch
            )
            
            if not response:
                return {
                    "status": "failed",
                    "message": "Failed to reopen amount block"
                }
                
            body, msg_status = CBSXMLParser.parse_response(response, "REOPENAMTBLK")
            
            if "SUCCESS" in msg_status:
                return {
                    "status": "success",
                    "message": "Amount block reopened successfully"
                }
                
            return {
                "status": "failed",
                "message": "Failed to reopen amount block",
                "error": body.get("error_description", "Unknown error")
            }
            
        except Exception as e:
            return {
                "status": "failed",
                "message": str(e)
            }

# Create a singleton instance
flexcube_service = FlexcubeService()

# Export service functions
async def verify_cif(cif_number: str) -> Dict[str, Any]:
    """Verify customer CIF number with CBS"""
    return await flexcube_service.verify_cif(cif_number)

async def get_account_details(cif_number: str) -> list:
    """Get account details from CBS"""
    return await flexcube_service.get_account_details(cif_number)

async def get_transaction_history(account_number: str, from_date: str, to_date: str) -> Optional[list]:
    """Get transaction history from CBS"""
    return await flexcube_service.get_transaction_history(account_number, from_date, to_date)

async def validate_transfer(from_account: str, to_account: str, amount: Decimal) -> Dict[str, Any]:
    """Validate transfer with CBS"""
    return await flexcube_service.validate_transfer(from_account, to_account, amount)

async def execute_transfer(from_account: str, to_account: str, amount: Decimal, reference: str, description: str, otp: str = None) -> Dict[str, Any]:
    """Execute transfer through CBS"""
    return await flexcube_service.execute_transfer(from_account, to_account, amount, reference, description, otp)

async def get_account_balance(account_number: str) -> Dict[str, Any]:
    """Get account balance from CBS"""
    return await flexcube_service.get_cbs_account_balance(account_number)

async def create_amount_block(account: str, amount: Decimal, reference: str, branch: str, phone: str) -> Dict[str, Any]:
    return await flexcube_service.create_amount_block(account, amount, reference, branch, phone)

async def close_amount_block(account: str, reference: str, branch: str) -> Dict[str, Any]:
    return await flexcube_service.close_amount_block(account, reference, branch)

async def reopen_amount_block(account: str, reference: str, branch: str) -> Dict[str, Any]:
    return await flexcube_service.reopen_amount_block(account, reference, branch)