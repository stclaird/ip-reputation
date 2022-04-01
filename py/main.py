from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from v1.http_error import http_error_handler
from v1.routes import router as api_router
from config import General


def get_application() -> FastAPI:
    description = "<br><h2>**IP Reputation APP**</h2>"
    tags_metadata = [
        {
            "name": "Info",
            "description": " Operations for monitoring Api",
        }
    ]

    middleware = [Middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'],
                             allow_headers=['*'])]

    application = FastAPI(
        openapi_tags=tags_metadata,
        title=General.SERVICE_NAME,
        debug=General.DEBUG, 
        version=General.VERSION,
        middleware=middleware,
        description=description
    )

    application.add_exception_handler(HTTPException, http_error_handler)
    application.include_router(api_router, prefix=General.API_PREFIX)

    return application


api = get_application()