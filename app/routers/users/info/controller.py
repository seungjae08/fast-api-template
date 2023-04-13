from .model import UserInfoRequest
from fastapi.responses import JSONResponse
from app.modules.errors import InvalidUserId


async def get_user_info(user_info_request: UserInfoRequest):
    if user_info_request.user_id == "test_user_info":
        return JSONResponse(user_info_request.dict())
    else:
        raise InvalidUserId(user_id=user_info_request.user_id)