from typing import List

from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel


class CommonErrorError(BaseModel):
    detail_code: str
    detail: str


class CommonError(BaseModel):
    error: CommonErrorError


class AppRequestValidationErrorDetail(BaseModel):
    loc: List[str]
    msg: str
    type: str


class AppRequestValidationErrorError(BaseModel):
    detail_code: str = RequestValidationError.__name__
    # TODO: 정의된 클래스가 없어서 직접 만든게 껄쩍지근함.
    detail: List[AppRequestValidationErrorDetail]


class AppRequestValidationError(BaseModel):
    error: AppRequestValidationErrorError


