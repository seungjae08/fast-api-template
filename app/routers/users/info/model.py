from pydantic import BaseModel


class UserInfoRequest(BaseModel):
    user_id: str
