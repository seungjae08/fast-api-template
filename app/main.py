from fastapi import FastAPI
from .exception_handler import add_exception_handler


app = FastAPI(
    title="fast-api-template",
    description="fast api template project",
    openapi_url="/api/openapi.json",
    docs_url="/api/openapi",
)


@app.on_event("startup")
async def startup_event():
    _init_router()


add_exception_handler(app)


def _init_router():
    from .routers.routers import routers

    app.include_router(routers)
