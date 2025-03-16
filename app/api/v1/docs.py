from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
import markdown2
import pathlib

router = APIRouter()

@router.get("/system", response_class=HTMLResponse, tags=["Documentation"])
async def get_system_documentation():
    """
    Get the system documentation in HTML format.
    This endpoint is non-secured and accessible to anyone.
    """
    try:
        # Read the markdown file
        docs_path = pathlib.Path("SYSTEM_README.md")
        if not docs_path.exists():
            raise HTTPException(status_code=404, detail="Documentation not found")
        
        markdown_content = docs_path.read_text(encoding='utf-8')
        
        # Convert markdown to HTML with styling
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Salaam Internet Banking - System Documentation</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                pre {{
                    background-color: #f5f5f5;
                    padding: 15px;
                    border-radius: 5px;
                    overflow-x: auto;
                }}
                code {{
                    font-family: 'Courier New', Courier, monospace;
                }}
                h1, h2, h3, h4 {{
                    color: #333;
                }}
                a {{
                    color: #0066cc;
                    text-decoration: none;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
                .container {{
                    background-color: white;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }}
            </style>
        </head>
        <body>
            <div class="container">
                {markdown2.markdown(markdown_content, extras=['fenced-code-blocks', 'tables'])}
            </div>
        </body>
        </html>
        """
        
        return HTMLResponse(content=html_content)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading documentation: {str(e)}") 