#!/usr/bin/env python3
"""
MPESA Settlement Script
-----------------------
This script processes MPESA transactions by reading data from a text file
and executing SOAP requests to create transactions in Flexcube.

Input file format:
xref|prod|branch|acc|amount|narrative[|block_reference]
"""

import os
import sys
import asyncio
import logging
import aiohttp
import xml.etree.ElementTree as ET
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple
import argparse
from pathlib import Path

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.cbs import (
    close_amount_block,
    reopen_amount_block,
    flexcube_service
)

# Ensure logs directory exists
logs_dir = Path("logs")
logs_dir.mkdir(exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(f"logs/mpesa_settlement_{datetime.now().strftime('%Y%m%d')}.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('mpesa_settlement')

class MPESATransaction:
    """Class to represent a single MPESA transaction."""
    
    def __init__(self, line: str):
        """
        Initialize transaction with data from a line in the input file.
        Format: xref|prod|branch|acc|amount|narrative[|block_reference]
        """
        parts = line.strip().split('|')
        if len(parts) < 6:
            raise ValueError(f"Invalid transaction format: {line}")
        
        self.xref = parts[0]
        self.prod = parts[1]
        self.branch = parts[2]
        self.account = parts[3]
        self.narrative = parts[5]
        
        try:
            self.amount = float(parts[4])
        except ValueError:
            raise ValueError(f"Invalid amount: {parts[4]}")
            
        # Handle narrative and optional block reference
        if len(parts) > 6:
            self.block_reference = parts[6]
        else:
            self.block_reference = None
        
        # Transaction response data
        self.status = "pending"
        self.message = ""
        self.transaction_reference = None
        self.fcc_reference = None  # Added FCC reference field
        self.error_code = None
        self.error_description = None
        self.warning_code = None
        self.warning_description = None

    def __str__(self) -> str:
        return (f"Transaction: {self.xref}, Product: {self.prod}, Branch: {self.branch}, "
                f"Account: {self.account}, Amount: {self.amount}, Narrative: {self.narrative}, "
                f"Block Reference: {self.block_reference}")

class MPESASettlementProcessor:
    """Class to process MPESA settlement transactions."""
    
    def __init__(self, cbs_url: str, source: str, ubscomp: str, userid: str):
        """Initialize with CBS configuration."""
        self.cbs_url = cbs_url
        self.source = source
        self.ubscomp = ubscomp
        self.userid = userid
        self.timeout = aiohttp.ClientTimeout(total=60)  # 60 seconds timeout

    async def execute_transaction(self, transaction: MPESATransaction) -> Dict[str, Any]:
        """Execute a transaction by sending a SOAP request to CBS."""
        try:
            # If transaction has a block reference, close it first
            if transaction.block_reference:
                close_result = await close_amount_block(
                    transaction.account,
                    transaction.block_reference,
                    transaction.branch,
                    self.cbs_url+'/FCUBSCustomerService/FCUBSCustomerService'
                )
                
                if close_result["status"] != "success":
                    logger.error(f"Failed to close amount block: {close_result}")
                    transaction.status = "failed"
                    transaction.message = f"Failed to close amount block: {close_result['message']}"
                    return {
                        "status": "ERROR",
                        "error": close_result["message"]
                    }
            
            # Create transaction body
            body = {
                "FCUBS_BODY": {
                    "Transaction-Details": {
                        "XREF": transaction.xref,
                        "PRD": transaction.prod,
                        "BRN": transaction.branch,
                        "TXNBRN": transaction.branch,
                        "TXNACC": transaction.account,
                        "TXNCCY": "KES",
                        "TXNAMT": f"{transaction.amount:.2f}",
                        "NARRATIVE": transaction.narrative
                    }
                }
            }

            # Execute the transaction using FlexcubeService
            response = await flexcube_service._make_soap_request(
                service="FCUBSRTService",
                operation="CreateTransaction",
                body=body,
                branch=transaction.branch,
                service_url=self.cbs_url+'/FCUBSRTService/FCUBSRTService'
            )
            
            # Parse response
            result = self._parse_response(response)
            
            # If transaction failed and we had a block, reopen it
            if result["status"] != "SUCCESS" and transaction.block_reference:
                await reopen_amount_block(
                    transaction.account,
                    transaction.block_reference,
                    transaction.branch,
                    self.cbs_url+'/FCUBSCustomerService/FCUBSCustomerService'
                )
            
            # Update transaction status
            if result["status"] == "SUCCESS":
                transaction.status = "success"
                transaction.message = "Transaction created successfully"
                transaction.transaction_reference = result.get("fcc_ref")
                transaction.fcc_reference = result.get("fcc_ref")  # Store FCC reference
            else:
                transaction.status = "failed"
                transaction.message = result.get("error_description", "Transaction failed")
                transaction.error_code = result.get("error_code")
                transaction.error_description = result.get("error_description")
            
            return result
                    
        except Exception as e:
            # If any error occurs and we had a block, reopen it
            if transaction.block_reference:
                await reopen_amount_block(
                    transaction.account,
                    transaction.block_reference,
                    transaction.branch
                )
            
            error_msg = f"Error executing transaction {transaction.xref}: {str(e)}"
            logger.error(error_msg)
            logger.exception("Detailed error traceback:")
            transaction.status = "failed"
            transaction.message = error_msg
            return {
                "status": "ERROR",
                "error": error_msg
            }

    def _parse_response(self, response_text: str) -> Dict[str, Any]:
        """Parse the SOAP response from CBS."""
        logger.info(f"Parsing response: {response_text}")
        try:
            root = ET.fromstring(response_text)
            
            # Define namespaces
            namespaces = {
                'S': 'http://schemas.xmlsoap.org/soap/envelope/',
                'ns': 'http://fcubs.ofss.com/service/FCUBSRTService'
            }
            
            # Extract header information
            header = root.find('.//ns:FCUBS_HEADER', namespaces)
            msg_status = header.find('ns:MSGSTAT', namespaces).text if header is not None and header.find('ns:MSGSTAT', namespaces) is not None else None
            
            # Check for error response
            error_resp = root.find('.//ns:FCUBS_ERROR_RESP', namespaces)
            error_code = None
            error_desc = None
            if error_resp is not None:
                error = error_resp.find('.//ns:ERROR', namespaces)
                if error is not None:
                    error_code = error.find('ns:ECODE', namespaces).text if error.find('ns:ECODE', namespaces) is not None else None
                    error_desc = error.find('ns:EDESC', namespaces).text if error.find('ns:EDESC', namespaces) is not None else None
            
            # Check for warning response
            warning_resp = root.find('.//ns:FCUBS_WARNING_RESP', namespaces)
            warning_code = None
            warning_desc = None
            if warning_resp is not None:
                warning = warning_resp.find('.//ns:WARNING', namespaces)
                if warning is not None:
                    warning_code = warning.find('ns:WCODE', namespaces).text if warning.find('ns:WCODE', namespaces) is not None else None
                    warning_desc = warning.find('ns:WDESC', namespaces).text if warning.find('ns:WDESC', namespaces) is not None else None
            
            # Extract transaction details
            txn_details = root.find('.//ns:Transaction-Details-IO', namespaces) or root.find('.//ns:Transaction-Details', namespaces)
            fcc_ref = None
            if txn_details is not None:
                fcc_ref = txn_details.find('ns:FCCREF', namespaces).text if txn_details.find('ns:FCCREF', namespaces) is not None else None
                if fcc_ref is None:
                    fcc_ref = txn_details.find('ns:FCC_REF', namespaces).text if txn_details.find('ns:FCC_REF', namespaces) is not None else None
            
            # Check for duplicate transaction based on error message
            if msg_status == 'FAILURE' and error_desc and 'Duplication External Reference No' in error_desc:
                logger.info(f"Duplicate transaction detected: {error_desc}")
                # Try to extract the reference number from the error message
                import re
                ref_match = re.search(r'No\(([^)]+)\)', error_desc)
                extracted_fcc_ref = ref_match.group(1) if ref_match else None
                
                return {
                    'status': 'DUPLICATE',
                    'error_code': error_code,
                    'error_description': error_desc,
                    'fcc_ref': extracted_fcc_ref or fcc_ref
                }
            
            if msg_status == 'SUCCESS':
                return {
                    'status': 'SUCCESS',
                    'warning_code': warning_code,
                    'warning_description': warning_desc,
                    'fcc_ref': fcc_ref
                }
            else:
                logger.error(f"Transaction failed with status: {msg_status}")
                logger.error(f"Error: {error_code} - {error_desc}")
                return {
                    'status': msg_status or 'FAILURE',
                    'error_code': error_code,
                    'error_description': error_desc,
                    'fcc_ref': fcc_ref
                }
                
        except Exception as e:
            logger.error(f"Error parsing response: {str(e)}")
            logger.error(f"Response text: {response_text}")
            return {
                'status': 'ERROR',
                'error': f'Failed to parse response: {str(e)}'
            }

def read_transactions(file_path: str) -> List[MPESATransaction]:
    """Read transactions from a file."""
    transactions = []
    
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        return []
    
    try:
        with open(file_path, 'r') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue  # Skip empty lines and comments
                    
                if line_num == 1 and 'xref|prod|branch|acc|amount|narrative' in line.lower():
                    continue  # Skip header line
                
                try:
                    transaction = MPESATransaction(line)
                    transactions.append(transaction)
                except ValueError as e:
                    logger.error(f"Line {line_num}: {str(e)}")
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {str(e)}")
    
    return transactions

async def process_transactions(
    transactions: List[MPESATransaction],
    processor: MPESASettlementProcessor,
    max_concurrent: int = 5
) -> Dict[str, int]:
    """Process all transactions with concurrency control."""
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def process_with_semaphore(transaction):
        async with semaphore:
            return await processor.execute_transaction(transaction)
    
    # Execute all transactions concurrently
    tasks = [process_with_semaphore(txn) for txn in transactions]
    await asyncio.gather(*tasks)
    
    # Count results
    results = {
        "total": len(transactions),
        "success": sum(1 for txn in transactions if txn.status == "success"),
        "duplicate": sum(1 for txn in transactions if txn.status == "duplicate"),
        "failed": sum(1 for txn in transactions if txn.status == "failed"),
        "unknown": sum(1 for txn in transactions if txn.status not in ["success", "duplicate", "failed"])
    }
    
    return results

def write_results(transactions: List[MPESATransaction], output_file: str) -> None:
    """Write processing results to an output file."""
    try:
        with open(output_file, 'w') as file:
            # Write header
            file.write("xref|prod|branch|account|amount|narrative|status|message|transaction_reference|fcc_reference|error_code|error_description|warning_code|warning_description\n")
            
            # Write transaction results
            for txn in transactions:
                file.write(f"{txn.xref}|{txn.prod}|{txn.branch}|{txn.account}|{txn.amount:.2f}|"
                          f"{txn.narrative}|{txn.status}|{txn.message}|{txn.transaction_reference or ''}|"
                          f"{txn.fcc_reference or ''}|{txn.error_code or ''}|{txn.error_description or ''}|"
                          f"{txn.warning_code or ''}|{txn.warning_description or ''}\n")
        
        logger.info(f"Results written to {output_file}")
    except Exception as e:
        logger.error(f"Error writing results to {output_file}: {str(e)}")

async def main():
    parser = argparse.ArgumentParser(description="MPESA Settlement Processing Script")
    parser.add_argument("input_file", help="Path to the input file with transaction data")
    parser.add_argument("--output", "-o", help="Path to write the results", 
                        default=f"mpesa_settlement_results_{datetime.now().strftime('%Y%m%d')}.txt")
    parser.add_argument("--url", help="CBS SOAP URL", 
                        default=os.environ.get("CBS_SOAP_URL", "http://10.54.12.70:7004/FCUBSRTService/FCUBSRTService"))
    parser.add_argument("--source", help="Source system", 
                        default=os.environ.get("CBS_SOURCE", "SMFBPORTAL"))
    parser.add_argument("--ubscomp", help="UBS Component", 
                        default=os.environ.get("CBS_UBSCOMP", "FCUBS"))
    parser.add_argument("--userid", help="User ID", 
                        default=os.environ.get("CBS_USERID", "USSDSMFB"))
    parser.add_argument("--concurrent", "-c", type=int, help="Maximum concurrent requests", default=5)
    parser.add_argument("--env", help="Environment (UAT or PROD)", choices=["UAT", "PROD"], default="PROD")
    
    args = parser.parse_args()
    
    # Adjust URL based on environment
    default_userid = "SYSTEM"
    default_url = ""
    if args.env == "PROD":
        default_userid = "USSDSMFB"
        default_url = "http://10.54.12.70:7004"
        logger.info("[*] Using PROD environment for CBS "+default_url)
    
    cbs_url = default_url
    # cbs_userid = args.userid if args.userid != "USSDSMFB" else default_userid
    
    logger.info(f"Starting MPESA settlement processing from file: {args.input_file}")
    logger.info(f"Environment: {args.env}, CBS URL: {cbs_url}")
    
    # Read transactions from file
    transactions = read_transactions(args.input_file)
    logger.info(f"Loaded {len(transactions)} transactions")
    
    if not transactions:
        logger.error("No valid transactions found. Exiting.")
        return
    
    # Initialize processor
    processor = MPESASettlementProcessor(
        cbs_url=cbs_url,
        source=args.source,
        ubscomp=args.ubscomp,
        userid=default_userid
    )
    
    # Process transactions
    logger.info(f"Processing transactions with max concurrency: {args.concurrent}")
    results = await process_transactions(transactions, processor, max_concurrent=args.concurrent)
    
    # Write results to output file
    write_results(transactions, args.output)
    
    # Log summary
    logger.info(f"Processing complete. Summary: " + 
                f"Total: {results['total']}, " +
                f"Success: {results['success']}, " +
                f"Duplicate: {results['duplicate']}, " +
                f"Failed: {results['failed']}, " +
                f"Unknown: {results['unknown']}")

if __name__ == "__main__":
    asyncio.run(main()) 