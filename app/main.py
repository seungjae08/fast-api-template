from fastapi import FastAPI, Request
from starlette.middleware.base import RequestResponseEndpoint
from .modules.logger import initialize_logging
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
    initialize_logging(logging_name="template", level="INFO")


add_exception_handler(app)


@app.middleware("http")
async def logging_middleware(request: Request, call_next: RequestResponseEndpoint):
    pass


def _init_router():
    from .routers.routers import routers

    app.include_router(routers)
