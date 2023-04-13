from fastapi import APIRouter
from .info.controller import  get_user_info


routers = APIRouter(prefix="/users")

routers.add_api_route(
    "/info",
    get_user_info,
    methods=["post"]
)