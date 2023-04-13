from fastapi import APIRouter
from .users import routers as users_routers


routers = APIRouter(prefix="/api")

routers.include_router(users_routers)
