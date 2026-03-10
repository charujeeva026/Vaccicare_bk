import os
import sys

# Add the project root to sys.path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

try:
    from main import app
except Exception as e:
    import traceback
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse
    
    app = FastAPI()
    
    @app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
    async def catch_all(path: str):
        return JSONResponse(
            status_code=200, # Use 200 so we can actually see the error page
            content={
                "error": "Startup Crash",
                "exception": str(e),
                "traceback": traceback.format_exc(),
                "cwd": os.getcwd(),
                "path": sys.path
            }
        )