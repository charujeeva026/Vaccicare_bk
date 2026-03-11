import os
import sys
import traceback

# Add the project root to sys.path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

try:
    from main import app

except Exception as error:
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse

    error_message = str(error)
    tb = traceback.format_exc()

    app = FastAPI()

    @app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
    async def catch_all(path: str):
        return JSONResponse(
            status_code=200,
            content={
                "error": "Startup Crash",
                "exception": error_message,
                "traceback": tb,
                "cwd": os.getcwd(),
                "path": sys.path
            }
        )