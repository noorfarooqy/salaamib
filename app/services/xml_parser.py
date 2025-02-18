from typing import Dict, Any, Optional, Tuple
from xml.etree import ElementTree as ET
from app.services.logger import CBSLogger

cbs_logger = CBSLogger()
class CBSXMLParser:
    """Parser for CBS XML responses"""
    
    @staticmethod
    def parse_xml_element(elem: ET.Element) -> Dict[str, Any]:
        """Recursively parse XML element into dictionary"""
        result = {}
        for child in elem:
            tag = child.tag.split('}')[-1]
            if len(child) > 0:
                cbs_logger.log_info(f"child: {child}")
                if tag in result:
                    # If tag already exists, convert to list if not already
                    if not isinstance(result[tag], list):
                        result[tag] = [result[tag]]
                    result[tag].append(CBSXMLParser.parse_xml_element(child))
                else:
                    result[tag] = CBSXMLParser.parse_xml_element(child)
            elif child.text and child.text.strip():
                if tag in result:
                    # If tag already exists, convert to list if not already
                    if not isinstance(result[tag], list):
                        result[tag] = [result[tag]]
                    result[tag].append(child.text.strip())
                else:
                    result[tag] = child.text.strip()
        return result

    @classmethod
    def parse_response(cls, xml_text: str, operation: str) -> Tuple[Dict[str, Any], str]:
        """
        Parse CBS XML response and extract body and message status
        
        Args:
            xml_text: The XML response text from CBS
            operation: The operation name (e.g. 'QUERYCUSTOMERDETAILS')
            
        Returns:
            Tuple containing:
            - Dictionary of parsed response body
            - Message status string
        """
        try:
            root = ET.fromstring(xml_text)
            response = cls.parse_xml_element(root)
            
            # Extract body and message status
            body = response.get("Body", {})
            cbs_logger.log_info(f"Parsed CBS response body: {body}")
            
            # Get operation-specific response
            operation_response = body.get(f"{operation}_IOFS_RES", {})
            msg_status = str(operation_response.get("FCUBS_HEADER", {}).get("MSGSTAT", ""))
            
            return body, msg_status
            
        except Exception as e:
            cbs_logger.error(f"Error parsing CBS XML response: {str(e)}")
            return {}, ""

    @classmethod
    def get_customer_info(cls, body: Dict[str, Any]) -> Dict[str, Any]:
        """Extract customer information from parsed body"""
        try:
            return (body.get("QUERYCUSTOMERDETAILS_IOFS_RES", {})
                   .get("FCUBS_BODY", {})
                   .get("Stvws-Stdcifqy-Query-Full", {})
                   .get("Stvws-Stdcifqy", {}))
        except Exception as e:
            cbs_logger.error(f"Error extracting customer info: {str(e)}")
            return {}

    @classmethod
    def get_account_info(cls, body: Dict[str, Any]) -> Dict[str, Any]:
        """Extract account information from parsed body"""
        try:
            accounts =  (body.get("QUERYCUSTACCDETAIL_IOFS_RES", {})
                   .get("FCUBS_BODY", {})
                   .get("Sttms-Customer-Full", {})
                   .get("Stvws-Stdaccqy", {}))
            cbs_logger.log_info({'accounts': accounts})
            if not isinstance(accounts, list):
                accounts = [accounts]
            return accounts
        except Exception as e:
            cbs_logger.error(f"Error extracting account info: {str(e)}")
            return {} 