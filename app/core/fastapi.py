from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from app.app.api.v1_router import router as api_v1_router
from app.core.schemas import CommonError, CommonErrorError, AppRequestValidationError, \
    AppRequestValidationErrorError
from app.core.settings import Settings


def add_exception_handlers(app):
    @app.exception_handler(HTTPException)
    async def app_exception_handler(request: Request, exc: HTTPException):
        content = CommonError(
            error=CommonErrorError(
                detail_code=exc.__class__.__name__,
                detail=exc.detail))

        return JSONResponse(
            status_code=exc.status_code,
            content=content.dict()
        )

    @app.exception_handler(RequestValidationError)
    async def request_validation_handler(request: Request, exc: RequestValidationError):
        content = AppRequestValidationError(
            error=AppRequestValidationErrorError(
                detail_code=RequestValidationError.__name__,
                detail=exc.errors()
            )
        )
        return JSONResponse(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            content=content.dict()
        )


def get_application(settings: Settings) -> FastAPI:
    _app = FastAPI(title=settings.PROJECT_NAME,
                   responses={'400': {"model": CommonError},
                              '422': {"model": AppRequestValidationError},
                              '500': {"model": CommonError}}
                   )

    if settings.BACKEND_CORS_ORIGINS:
        _app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    _app.include_router(api_v1_router, prefix="/api")

    add_exception_handlers(_app)

    return _app
