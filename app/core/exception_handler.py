from app.core.exceptions import AppException
import uuid
from fastapi import Request
from fastapi.responses import JSONResponse
import logging

async def global_exception_handler(request: Request, exc: Exception):
    trace_id = str(uuid.uuid4())

    logging.error(f"Exception occurred: {exc}", extra={
            "trace_id": trace_id,
            "method": request.method,
        })

    if isinstance(exc, AppException):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": {
                    "message": exc.message,
                    "trace_id": trace_id
                }
            }
        )

    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "error_code": "INTERNAL_ERROR",
                "message": str(exc),
                "trace_id": trace_id
            }
        }
    )