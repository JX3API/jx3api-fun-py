from typing import (
    Generic,
    ParamSpec,
    Type,
    TypeVar,
    Union,
)

from pydantic import TypeAdapter

from jx3apifun.const import API_URL
from jx3apifun.model import BaseData, Request
from jx3apifun.permission import is_require_ticket, is_require_token

from .driver import AsyncDriver, SyncDriver

T = TypeVar("T", bound=BaseData)
P = ParamSpec("P")
ResponseModel = Union[T, list[T]]


class ApiCaller(Generic[T]):
    """
    调用api的执行器
    """

    async def call_api_async(
        self, request: Request, model: Type[ResponseModel]
    ) -> ResponseModel:
        """
        异步调用api
        """
        driver = AsyncDriver()
        if is_require_token(request.name):
            driver.check_token(request)
        if is_require_ticket(request.name):
            driver.check_ticket(request)

        response = await driver.request(request)
        data = response.data
        adapter = TypeAdapter(model)
        return adapter.validate_python(data)

    def call_api_sync(
        self, request: Request, model: Type[ResponseModel]
    ) -> ResponseModel:
        """
        同步调用api
        """
        driver = SyncDriver()
        if is_require_token(request.name):
            driver.check_token(request)
        if is_require_ticket(request.name):
            driver.check_ticket(request)

        response = driver.request(request)
        data = response.data
        adapter = TypeAdapter(model)
        return adapter.validate_python(data)


def make_request(func_name: str, **kwargs) -> Request:
    """
    生成请求
    """
    api_name = func_name.replace("_", "/")
    url = API_URL + api_name
    return Request(name=func_name, url=url, data=kwargs)
