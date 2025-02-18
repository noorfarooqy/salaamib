import aiohttp
import asyncio
from typing import Dict, Any, Optional, List, Tuple
import xml.etree.ElementTree as ET
from datetime import datetime
import logging
import os
from pathlib import Path
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('logs/transactions.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

ENV_FLAG = 'PROD'  # UAT, PROD

class TransactionCreator:
    def __init__(self):
        # CBS Configuration
        self.cbs_source = "SMFBPORTAL"
        self.cbs_user = "USSDSMFB"
        if ENV_FLAG == 'PROD':
            self.cbs_url = "http://10.54.12.70:7004/FCUBSRTService/FCUBSRTService"
        elif ENV_FLAG == 'UAT':
            self.cbs_url = "http://10.54.66.10:7005/FCUBSRTService/FCUBSRTService"
            self.cbs_user = "SYSTEM"
        self.headers = {
            'Content-Type': 'text/xml;charset=UTF-8',
            'SOAPAction': ''
        }

    def _create_transaction_request(
        self,
        xref: str,
        amount: float,
        narrative: str,
        branch: str = "000",
        is_charge: bool = False
    ) -> str:
        """Create SOAP request for transaction creation"""
        return f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:fcub="http://fcubs.ofss.com/service/FCUBSRTService">
   <soapenv:Header/>
   <soapenv:Body>
      <fcub:CREATETRANSACTION_FSFS_REQ>
         <fcub:FCUBS_HEADER>
            <fcub:SOURCE>{self.cbs_source}</fcub:SOURCE>
            <fcub:UBSCOMP>FCUBS</fcub:UBSCOMP>
            <fcub:USERID>{self.cbs_user}</fcub:USERID>
            <fcub:BRANCH>{branch}</fcub:BRANCH>
            <fcub:SERVICE>FCUBSRTService</fcub:SERVICE>
            <fcub:OPERATION>CreateTransaction</fcub:OPERATION>
         </fcub:FCUBS_HEADER>
         <fcub:FCUBS_BODY>
            <fcub:Transaction-Details>
               <fcub:XREF>{xref}</fcub:XREF>
               <fcub:PRD>{'IGMC' if is_charge else 'IGMP'}</fcub:PRD>
               <fcub:BRN>{branch}</fcub:BRN>
               <fcub:TXNBRN>{branch}</fcub:TXNBRN>
               <fcub:TXNCCY>KES</fcub:TXNCCY>
               <fcub:TXNAMT>{amount}</fcub:TXNAMT>
               <fcub:NARRATIVE>{narrative}</fcub:NARRATIVE>
            </fcub:Transaction-Details>
         </fcub:FCUBS_BODY>
      </fcub:CREATETRANSACTION_FSFS_REQ>
   </soapenv:Body>
</soapenv:Envelope>"""

    async def create_transaction(
        self,
        xref: str,
        amount: float,
        narrative: str,
        branch: str = "000",
        is_charge: bool = False
    ) -> Dict[str, Any]:
        """Send transaction creation request to CBS"""
        try:
            request_xml = self._create_transaction_request(xref, amount, narrative, branch, is_charge)
            logger.info(f"Processing {'charge' if is_charge else 'main'} transaction for ref: {xref}")
            
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    self.cbs_url,
                    data=request_xml,
                    headers=self.headers
                ) as response:
                    response_text = await response.text()
                    
                    if response.status != 200:
                        logger.error(f"CBS Error: Status code {response.status} for ref {xref}")
                        logger.error(f"Request URL: {self.cbs_url}")
                        logger.error(f"Request Headers: {self.headers}")
                        logger.error(f"Request Body: {request_xml}")
                        return {
                            'status': 'ERROR',
                            'error': f'CBS returned status code {response.status}'
                        }
                    
                    try:
                        root = ET.fromstring(response_text)
                        
                        # Define namespaces
                        namespaces = {
                            'S': 'http://schemas.xmlsoap.org/soap/envelope/',
                            'ns': 'http://fcubs.ofss.com/service/FCUBSRTService'
                        }
                        
                        # Extract header information using exact path with namespaces
                        header = root.find('.//ns:FCUBS_HEADER', namespaces)
                        msg_status = header.find('ns:MSGSTAT', namespaces).text if header is not None else None
                        
                        # Check for error response using exact path with namespaces
                        error_resp = root.find('.//ns:FCUBS_ERROR_RESP', namespaces)
                        if error_resp is not None:
                            error = error_resp.find('.//ns:ERROR', namespaces)
                            if error is not None:
                                error_code = error.find('ns:ECODE', namespaces).text if error.find('ns:ECODE', namespaces) is not None else None
                                error_desc = error.find('ns:EDESC', namespaces).text if error.find('ns:EDESC', namespaces) is not None else None
                                
                                # Special handling for duplicate transaction error
                                if error_code == 'GW-RTL-008' and error_desc and 'Duplication External Reference No' in error_desc:
                                    logger.info(f"Duplicate transaction detected for {xref}: {error_desc}")
                                    # Extract the reference number from the error message
                                    ref_match = re.search(r'No\(([^)]+)\)', error_desc)
                                    fcc_ref = ref_match.group(1) if ref_match else xref
                                    return {
                                        'status': 'DUPLICATE',
                                        'error_code': error_code,
                                        'error_description': error_desc,
                                        'fcc_ref': fcc_ref
                                    }
                                
                                logger.error(f"CBS Error for {xref}: [{error_code}] {error_desc}")
                                return {
                                    'status': 'ERROR',
                                    'error_code': error_code,
                                    'error_description': error_desc
                                }
                        
                        # Extract warning message if present using exact path with namespaces
                        warning_resp = root.find('.//ns:FCUBS_WARNING_RESP', namespaces)
                        warning_code = None
                        warning_desc = None
                        if warning_resp is not None:
                            warning = warning_resp.find('.//ns:WARNING', namespaces)
                            if warning is not None:
                                warning_code = warning.find('ns:WCODE', namespaces).text if warning.find('ns:WCODE', namespaces) is not None else None
                                warning_desc = warning.find('ns:WDESC', namespaces).text if warning.find('ns:WDESC', namespaces) is not None else None
                        
                        # Extract transaction details using exact path with namespaces
                        txn_details = root.find('.//ns:Transaction-Details', namespaces)
                        fcc_ref = None
                        if txn_details is not None:
                            fcc_ref = txn_details.find('ns:FCCREF', namespaces).text if txn_details.find('ns:FCCREF', namespaces) is not None else None
                        
                        if msg_status == 'SUCCESS':
                            logger.info(f"Successfully created transaction {xref}")
                            if warning_desc:
                                logger.info(f"CBS Warning for {xref}: {warning_desc}")
                            return {
                                'status': 'SUCCESS',
                                'warning_code': warning_code,
                                'warning_description': warning_desc,
                                'fcc_ref': fcc_ref
                            }
                        else:
                            # Check if this is a duplicate transaction based on the error message
                            if msg_status == 'FAILURE' and error_desc and 'Duplication External Reference No' in error_desc:
                                logger.info(f"Duplicate transaction detected for {xref}: {error_desc}")
                                # Extract the reference number from the error message
                                ref_match = re.search(r'No\(([^)]+)\)', error_desc)
                                fcc_ref = ref_match.group(1) if ref_match else xref
                                return {
                                    'status': 'DUPLICATE',
                                    'error_code': error_code,
                                    'error_description': error_desc,
                                    'fcc_ref': fcc_ref
                                }
                            
                            logger.error(f"Transaction failed with status: {msg_status}")
                            logger.error(f"Full Response: {response_text}")
                            return {
                                'status': msg_status or 'ERROR',
                                'warning_code': warning_code,
                                'warning_description': warning_desc,
                                'fcc_ref': fcc_ref,
                                'error': 'Transaction failed'
                            }
                        
                    except Exception as e:
                        logger.error(f"Error parsing response for {xref}: {str(e)}")
                        logger.error(f"Full Response: {response_text}")
                        return {
                            'status': 'ERROR',
                            'error': f'Failed to parse response: {str(e)}'
                        }
                    
        except Exception as e:
            logger.error(f"System Error processing {xref}: {str(e)}")
            logger.exception("Detailed error traceback:")
            return {
                'status': 'ERROR',
                'error': str(e)
            }

class TransactionRecord:
    @staticmethod
    def get_mpesa_charge(amount: float) -> float:
        """Get M-PESA charge based on transaction amount range"""
        if amount <= 100:  # 1-100
            return 0
        elif amount <= 1500:  # 101-1,500
            return 5
        elif amount <= 5000:  # 1,501-5,000
            return 9
        elif amount <= 20000:  # 5,001-20,000
            return 11
        else:  # Above 20,000
            return 13

    def __init__(self, line: str):
        """Parse a line from the transaction reference file"""
        parts = line.strip().split('|')
        if len(parts) >= 7:  # Handle 7 fields
            self.source_reference = parts[0]
            self.mpesa_reference = parts[1]
            self.transaction_amount = round(float(parts[2]), 2)  # Round to 2 decimal places
            
            # Calculate net commission by:
            # 1. Get gross commission
            gross_commission = float(parts[3])
            
            # 2. Deduct M-PESA charges based on transaction amount
            mpesa_charge = self.get_mpesa_charge(self.transaction_amount)
            commission_after_charges = gross_commission - mpesa_charge
            
            # 3. Deduct 15% VAT from remaining amount
            self.commission_amount = round(max(0, commission_after_charges / 1.15), 2)  # Remove VAT and round to 2 decimal places
            
            self.beneficiary = parts[4]  # Now directly the phone number
            self.transaction_reference = None if parts[5] == '-' else parts[5]  # Now the FCC reference
            self.commission_reference = None if parts[6] == '-' else parts[6]
        else:
            raise ValueError(f"Invalid line format: {line}")

    def _parse_response(self, response_text: str) -> Dict[str, Any]:
        """Parse the SOAP response and extract relevant information"""
        try:
            root = ET.fromstring(response_text)
            
            # Define namespaces
            namespaces = {
                'S': 'http://schemas.xmlsoap.org/soap/envelope/',
                'ns': 'http://fcubs.ofss.com/service/FCUBSRTService'
            }
            
            # Extract header information using exact path with namespaces
            header = root.find('.//ns:FCUBS_HEADER', namespaces)
            msg_status = header.find('ns:MSGSTAT', namespaces).text if header is not None else None
            
            # Check for error response using exact path with namespaces
            error_resp = root.find('.//ns:FCUBS_ERROR_RESP', namespaces)
            if error_resp is not None:
                error = error_resp.find('.//ns:ERROR', namespaces)
                if error is not None:
                    error_code = error.find('ns:ECODE', namespaces).text if error.find('ns:ECODE', namespaces) is not None else None
                    error_desc = error.find('ns:EDESC', namespaces).text if error.find('ns:EDESC', namespaces) is not None else None
                    
                    # Special handling for duplicate transaction error
                    if error_code == 'GW-RTL-008' and error_desc and 'Duplication External Reference No' in error_desc:
                        logger.info(f"Duplicate transaction detected: {error_desc}")
                        return {
                            'status': 'DUPLICATE',
                            'error_code': error_code,
                            'error_description': error_desc
                        }
                    
                    logger.error(f"CBS Error: [{error_code}] {error_desc}")
                    return {
                        'status': 'ERROR',
                        'error_code': error_code,
                        'error_description': error_desc
                    }
            
            # Extract warning message if present using exact path with namespaces
            warning_resp = root.find('.//ns:FCUBS_WARNING_RESP', namespaces)
            warning_code = None
            warning_desc = None
            if warning_resp is not None:
                warning = warning_resp.find('.//ns:WARNING', namespaces)
                if warning is not None:
                    warning_code = warning.find('ns:WCODE', namespaces).text if warning.find('ns:WCODE', namespaces) is not None else None
                    warning_desc = warning.find('ns:WDESC', namespaces).text if warning.find('ns:WDESC', namespaces) is not None else None
            
            # Extract transaction details using exact path with namespaces
            txn_details = root.find('.//ns:Transaction-Details', namespaces)
            fcc_ref = None
            if txn_details is not None:
                fcc_ref = txn_details.find('ns:FCCREF', namespaces).text if txn_details.find('ns:FCCREF', namespaces) is not None else None
            
            return {
                'status': msg_status,
                'warning_code': warning_code,
                'warning_description': warning_desc,
                'fcc_ref': fcc_ref
            }
            
        except Exception as e:
            logger.error(f"Error parsing response: {str(e)}")
            return {
                'status': 'ERROR',
                'error': str(e)
            }

    async def create_transaction(
        self,
        xref: str,
        amount: float,
        narrative: str,
        branch: str = "000",
        is_charge: bool = False
    ) -> Dict[str, Any]:
        """Send transaction creation request to CBS"""
        try:
            # Round amount to 2 decimal places
            amount = round(amount, 2)
            request_xml = self._create_transaction_request(xref, amount, narrative, branch, is_charge)
            logger.info(f"Processing {'charge' if is_charge else 'main'} transaction for ref: {xref}")
            
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    self.cbs_url,
                    data=request_xml,
                    headers=self.headers
                ) as response:
                    response_text = await response.text()
                    
                    if response.status != 200:
                        logger.error(f"CBS Error: Status code {response.status} for ref {xref}")
                        # Log request details on error
                        logger.error(f"Request URL: {self.cbs_url}")
                        logger.error(f"Request Headers: {self.headers}")
                        logger.error(f"Request Body: {request_xml}")
                        return {
                            'status': 'ERROR',
                            'error': f'CBS returned status code {response.status}'
                        }
                    
                    result = self._parse_response(response_text)
                    
                    if result.get('status') == 'SUCCESS':
                        logger.info(f"Successfully created transaction {xref}")
                        if result.get('warning_description'):
                            logger.info(f"CBS Warning: {result['warning_description']}")
                    else:
                        # Log full response details on error
                        logger.error(f"Failed to create transaction {xref}")
                        logger.error(f"Error Code: {result.get('error_code')}")
                        logger.error(f"Error Description: {result.get('error_description')}")
                        logger.error(f"Full Response: {response_text}")
                    
                    return result
                    
        except Exception as e:
            logger.error(f"System Error processing {xref}: {str(e)}")
            logger.exception("Detailed error traceback:")
            return {
                'status': 'ERROR',
                'error': str(e)
            }

def read_transaction_refs(file_path: str) -> List[TransactionRecord]:
    """Read transaction references from a text file"""
    try:
        records = []
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip():  # Skip empty lines
                    try:
                        record = TransactionRecord(line)
                        records.append(record)
                    except ValueError as e:
                        logger.error(f"Error parsing line: {e}")
                        continue
        return records
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {str(e)}")
        return []

async def process_transactions(records: List[TransactionRecord]) -> Tuple[int, int, int, int, int]:
    """Process a batch of transactions"""
    creator = TransactionCreator()
    total = len(records)
    main_successful = 0
    main_duplicates = 0
    charge_successful = 0
    charge_duplicates = 0
    failed = 0

    logger.info("=" * 50)
    logger.info("Starting Transaction Creation Process")
    logger.info(f"Total records to process: {total}")
    logger.info("=" * 50)

    logger.info(f"Starting batch transaction process for {total} records")
    for i, record in enumerate(records, 1):
        logger.info(f"Processing [{i}/{total}] MPESA ref: {record.mpesa_reference}")
        
        # Process main transaction
        main_result = await creator.create_transaction(
            record.source_reference,
            record.transaction_amount,
            f"GROUP MPESA TRANSFER TO {record.beneficiary} - REF: {record.mpesa_reference}"
        )

        if main_result['status'] == 'SUCCESS':
            main_successful += 1
            record.transaction_reference = main_result.get('fcc_ref')
            
            # Only process charge if main transaction was successful
            if record.commission_amount > 0:
                charge_result = await creator.create_transaction(
                    f"{record.source_reference}CGA",
                    record.commission_amount,
                    f"GROUP MPESA TRANSFER CHARGE - REF: {record.mpesa_reference}",
                    is_charge=True
                )
                
                if charge_result['status'] == 'SUCCESS':
                    charge_successful += 1
                    record.commission_reference = charge_result.get('fcc_ref')
                elif charge_result['status'] == 'DUPLICATE':
                    charge_duplicates += 1
                    record.commission_reference = charge_result.get('fcc_ref')
                else:
                    failed += 1
                    logger.error(f"Charge transaction failed: {charge_result.get('error_description', 'Unknown error')}")
        
        elif main_result['status'] == 'DUPLICATE':
            main_duplicates += 1
            record.transaction_reference = main_result.get('fcc_ref')
            
            # For duplicates, check if charge exists
            if record.commission_amount > 0:
                charge_result = await creator.create_transaction(
                    f"{record.source_reference}CHG",
                    record.commission_amount,
                    f"GROUP MPESA TRANSFER CHARGE - REF: {record.mpesa_reference}",
                    is_charge=True
                )
                
                if charge_result['status'] == 'SUCCESS':
                    charge_successful += 1
                    record.commission_reference = charge_result.get('fcc_ref')
                elif charge_result['status'] == 'DUPLICATE':
                    charge_duplicates += 1
                    record.commission_reference = charge_result.get('fcc_ref')
                else:
                    failed += 1
                    logger.error(f"Charge transaction failed: {charge_result.get('error_description', 'Unknown error')}")
        else:
            failed += 1
            error_desc = main_result.get('error_description', main_result.get('error', 'Unknown error'))
            logger.error(f"Main transaction failed: {error_desc}")

    logger.info("\n" + "=" * 50)
    logger.info("Batch Processing Summary")
    logger.info(f"Total Processed: {total}")
    logger.info("Main Transactions:")
    logger.info(f"  - Successful: {main_successful}")
    logger.info(f"  - Duplicates: {main_duplicates}")
    logger.info("Charge Transactions:")
    logger.info(f"  - Successful: {charge_successful}")
    logger.info(f"  - Duplicates: {charge_duplicates}")
    logger.info(f"Failed Transactions: {failed}")
    logger.info("=" * 50 + "\n")

    return main_successful, main_duplicates, charge_successful, charge_duplicates, failed

async def main():
    # Create logs directory if it doesn't exist
    Path("logs").mkdir(exist_ok=True)
    
    script_dir = Path(__file__).parent
    file_path = script_dir / "trn_refs.txt"
    
    # Read transaction references from file
    records = read_transaction_refs(str(file_path))
    
    if not records:
        logger.error(f"No transaction records found in {file_path}")
        return
    
    logger.info(f"{'='*50}")
    logger.info(f"Starting Transaction Creation Process")
    logger.info(f"Total records to process: {len(records)}")
    logger.info(f"{'='*50}")
    
    # Process all transactions
    results = await process_transactions(records)
    
    # Log summary
    main_successful, main_duplicates, charge_successful, charge_duplicates, failed = results
    
    logger.info(f"\n{'='*50}")
    logger.info(f"Batch Processing Summary")
    logger.info(f"Total Processed: {len(records)}")
    logger.info(f"Main Transactions Successful: {main_successful}")
    logger.info(f"Main Duplicates: {main_duplicates}")
    logger.info(f"Charge Transactions Successful: {charge_successful}")
    logger.info(f"Charge Duplicates: {charge_duplicates}")
    logger.info(f"Failed: {failed}")
    logger.info(f"{'='*50}\n")

if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main()) 