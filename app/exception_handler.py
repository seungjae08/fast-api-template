from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.modules.errors import InvalidUserId


def add_exception_handler(app: FastAPI):
    @app.exception_handler(RequestValidationError)
    async def request_validation_handler(request: Request, exc):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "content": "invalid request format"
            }
        )

    @app.exception_handler(Exception)
    async def exception_handler(request: Request, exc):
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "content": "internal server error"
            }
        )

    @app.exception_handler(InvalidUserId)
    async def invalid_user_id_exception_handler(request: Request, exc: InvalidUserId):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "content": "invalid user id",
                "user_id": exc.user_id
            }
        )
