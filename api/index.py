import os
import sys
import traceback

# Add the root directory to sys.path so it can find main.py and other modules
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)

try:
    from main import app
except Exception as e:
    from fastapi import FastAPI
    import json
    from fastapi.responses import JSONResponse
    
    app = FastAPI()
    
    @app.get("/")
    async def root_error():
        return await catch_all("")

    @app.get("/{path:path}")
    async def catch_all(path: str):
        error_info = {
            "error": "Startup Failed",
            "exception": str(e),
            "traceback": traceback.format_exc(),
            "root_dir": root_dir,
            "sys_path": sys.path,
            "cwd": os.getcwd()
        }
        return JSONResponse(status_code=500, content=error_info)