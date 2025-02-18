import aiohttp
import asyncio
from typing import Dict, Any, Optional, List
import xml.etree.ElementTree as ET
from datetime import datetime
import logging
import os
from pathlib import Path

# Configure logging with a more professional format
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('logs/reversal.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

ENV_FLAG = 'PROD' # UAT, PROD

class TransactionReversal:
    def __init__(self):
        # CBS Production Configuration
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
        
    def _create_reversal_request(self, fcc_ref: str, branch: str = "003") -> str:
        """Create SOAP request for transaction reversal"""
        return f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:fcub="http://fcubs.ofss.com/service/FCUBSRTService">
   <soapenv:Header/>
   <soapenv:Body>
      <fcub:REVERSETRANSACTION_FSFS_REQ>
         <fcub:FCUBS_HEADER>
            <fcub:SOURCE>{self.cbs_source}</fcub:SOURCE>
            <fcub:UBSCOMP>FCUBS</fcub:UBSCOMP>
            <fcub:USERID>{self.cbs_user}</fcub:USERID>
            <fcub:BRANCH>{branch}</fcub:BRANCH>
            <fcub:SERVICE>FCUBSRTService</fcub:SERVICE>
            <fcub:OPERATION>ReverseTransaction</fcub:OPERATION>
         </fcub:FCUBS_HEADER>
         <fcub:FCUBS_BODY>
            <fcub:Transaction-Details>
               <fcub:FCCREF>{fcc_ref}</fcub:FCCREF>
            </fcub:Transaction-Details>
         </fcub:FCUBS_BODY>
      </fcub:REVERSETRANSACTION_FSFS_REQ>
   </soapenv:Body>
</soapenv:Envelope>"""

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
            
            if msg_status == 'SUCCESS':
                logger.info(f"Successfully reversed transaction {fcc_ref}")
                if warning_desc:
                    logger.info(f"CBS Warning: {warning_desc}")
                return {
                    'status': 'SUCCESS',
                    'warning_code': warning_code,
                    'warning_description': warning_desc,
                    'fcc_ref': fcc_ref
                }
            else:
                # Check if this is an already reversed transaction
                if error_desc and 'Transaction is already Reversed' in error_desc:
                    logger.info(f"Transaction already reversed: {fcc_ref}")
                    return {
                        'status': 'ALREADY_REVERSED',
                        'error_code': error_code,
                        'error_description': error_desc,
                        'fcc_ref': fcc_ref
                    }
                
                logger.error(f"Reversal failed with status: {msg_status}")
                logger.error(f"Full Response: {response_text}")
                return {
                    'status': msg_status or 'ERROR',
                    'warning_code': warning_code,
                    'warning_description': warning_desc,
                    'fcc_ref': fcc_ref,
                    'error': 'Reversal failed'
                }
            
        except Exception as e:
            logger.error(f"Error parsing response: {str(e)}")
            logger.error(f"Full Response: {response_text}")
            return {
                'status': 'ERROR',
                'error': f'Failed to parse response: {str(e)}'
            }

    async def reverse_transaction(self, fcc_ref: str, branch: str = "003") -> Dict[str, Any]:
        """Send transaction reversal request to CBS"""
        try:
            request_xml = self._create_reversal_request(fcc_ref, branch)
            logger.info(f"Processing reversal for FCC ref: {fcc_ref} on branch {branch}")
            
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    self.cbs_url,
                    data=request_xml,
                    headers=self.headers
                ) as response:
                    if response.status != 200:
                        logger.error(f"CBS Error: Status code {response.status} for FCC ref {fcc_ref}")
                        return {
                            'status': 'ERROR',
                            'error': f'CBS returned status code {response.status}'
                        }
                    
                    response_text = await response.text()
                    
                    # Parse and return response
                    result = self._parse_response(response_text)
                    if result['status'] == 'SUCCESS':
                        logger.info(f"Successfully reversed transaction {fcc_ref}")
                        if result.get('warning_description'):
                            logger.info(f"CBS Warning: {result['warning_description']}")
                    else:
                        logger.error(f"Failed to reverse {fcc_ref}: {result.get('error_description', 'Unknown error')}")
                    
                    return result
                    
        except Exception as e:
            logger.error(f"System Error processing {fcc_ref}: {str(e)}")
            return {
                'status': 'ERROR',
                'error': str(e)
            }

def read_fcc_refs(file_path: str) -> List[str]:
    """Read FCC references from a text file"""
    try:
        with open(file_path, 'r') as file:
            # Read lines and remove whitespace, empty lines
            return [line.strip() for line in file if line.strip()]
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {str(e)}")
        return []

async def process_reversals(fcc_refs: List[str], branch: str = "003"):
    """Process multiple reversals"""
    reversal = TransactionReversal()
    results = []
    total = len(fcc_refs)
    
    logger.info(f"Starting batch reversal process for {total} transactions")
    
    for index, fcc_ref in enumerate(fcc_refs, 1):
        try:
            logger.info(f"Processing [{index}/{total}] FCC ref: {fcc_ref}")
            result = await reversal.reverse_transaction(fcc_ref, branch)
            results.append({
                'fcc_ref': fcc_ref,
                'result': result
            })
            
            # Log transaction details if successful
            if result['status'] == 'SUCCESS':
                txn_details = result.get('transaction_details', {})
                logger.info(
                    f"Transaction Details:\n"
                    f"  Reference: {txn_details.get('reference')}\n"
                    f"  Amount: {txn_details.get('currency')} {txn_details.get('amount')}\n"
                    f"  Description: {txn_details.get('narrative')}"
                )
            
            # Add a small delay between requests
            await asyncio.sleep(1)
            
        except Exception as e:
            logger.error(f"Failed processing {fcc_ref}: {str(e)}")
            results.append({
                'fcc_ref': fcc_ref,
                'result': {'status': 'ERROR', 'error': str(e)}
            })
    
    return results

async def main():
    # Create logs directory if it doesn't exist
    Path("logs").mkdir(exist_ok=True)
    
    script_dir = Path(__file__).parent
    file_path = script_dir / "fcc_refs.txt"
    branch = "003"
    
    # Read FCC references from file
    fcc_refs = read_fcc_refs(str(file_path))
    
    if not fcc_refs:
        logger.error(f"No FCC references found in {file_path}")
        return
    
    logger.info(f"{'='*50}")
    logger.info(f"Starting Transaction Reversal Process")
    logger.info(f"Total transactions to process: {len(fcc_refs)}")
    logger.info(f"{'='*50}")
    
    # Process all reversals
    results = await process_reversals(fcc_refs, branch)
    
    # Log summary
    success_count = sum(1 for r in results if r['result']['status'] == 'SUCCESS')
    failed_count = len(results) - success_count
    
    logger.info(f"\n{'='*50}")
    logger.info(f"Batch Processing Summary")
    logger.info(f"Total Processed: {len(results)}")
    logger.info(f"Successful: {success_count}")
    logger.info(f"Failed: {failed_count}")
    logger.info(f"{'='*50}\n")

if __name__ == "__main__":
    # Run the async main function
    asyncio.run(main()) 