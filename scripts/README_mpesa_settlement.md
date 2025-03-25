# MPESA Settlement Script

This script processes MPESA settlement transactions by reading transaction details from a text file and executing SOAP requests to Flexcube to create transactions.

## Features

- Reads transaction data from pipe-delimited (|) text files
- Handles multiple transactions concurrently for better performance
- Provides detailed logging of all operations
- Produces a comprehensive report of results
- Supports both UAT and PROD environments
- Handles duplicate transactions gracefully

## Prerequisites

- Python 3.7 or higher
- Required Python packages:
  - aiohttp
  - asyncio

## Installation

1. Ensure you have Python 3.7+ installed
2. Install required packages:
   ```
   pip install aiohttp
   ```
3. Make the script executable:
   ```
   chmod +x mpesa_settlement.py
   ```

## Input File Format

The input file should be a pipe-delimited text file with the following format:

```
xref|prod|branch|acc|amount|narrative
MPESA2024001|CDCR|001|1234567890001|5000.00|MPESA SETTLEMENT FOR TXN123456
MPESA2024002|CDCR|001|1234567890002|7500.50|MPESA SETTLEMENT FOR TXN123457
```

Fields:
- **xref**: Unique transaction reference
- **prod**: Product code (e.g., CDCR)
- **branch**: Branch code
- **acc**: Account number
- **amount**: Transaction amount (decimal)
- **narrative**: Transaction description

## Usage

Basic usage:

```
python mpesa_settlement.py input_file.txt
```

Advanced options:

```
python mpesa_settlement.py input_file.txt --env UAT --concurrent 10 --output results.txt
```

### Command Line Arguments

- `input_file`: Path to the input file with transaction data (required)
- `--output`, `-o`: Path to write the results (default: auto-generated filename)
- `--url`: CBS SOAP URL (default: environment-specific)
- `--source`: Source system (default: SMFBPORTAL)
- `--ubscomp`: UBS Component (default: FCUBS)
- `--userid`: User ID (default: environment-specific)
- `--concurrent`, `-c`: Maximum concurrent requests (default: 5)
- `--env`: Environment (UAT or PROD, default: PROD)

## Output

The script generates two outputs:

1. **Log file**: Detailed processing logs in the `logs` directory
2. **Results file**: A pipe-delimited file containing:
   - All input fields
   - Transaction status (success, duplicate, failed)
   - Status message
   - Transaction reference
   - Error details if applicable
   - Warning details if applicable

## Example

```bash
# Process transactions from prod environment
python mpesa_settlement.py mpesa_transactions_sample.txt --env PROD

# Process transactions from UAT environment
python mpesa_settlement.py mpesa_transactions_sample.txt --env UAT --concurrent 10
```

## Troubleshooting

If you encounter issues:

1. Check the log file in the `logs` directory for details
2. Ensure the input file follows the correct format
3. Verify connectivity to the CBS server
4. Check credentials and permissions for the CBS user

## Environment Variables

Instead of command-line arguments, you can use environment variables:

- `CBS_SOAP_URL`: URL for the CBS SOAP service
- `CBS_SOURCE`: Source system
- `CBS_UBSCOMP`: UBS component
- `CBS_USERID`: User ID for CBS 