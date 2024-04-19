from typing import (
    Generic,
    ParamSpec,
    Type,
    TypeVar,
    cast,
)

from jx3apifun.const import API_URL
from jx3apifun.exceptions import ResponseDataError
from jx3apifun.model import BaseData, BaseListData, Request
from jx3apifun.permission import is_require_ticket, is_require_token

from .driver import AsyncDriver, SyncDriver

T = TypeVar("T", bound=BaseData)
P = ParamSpec("P")


class ApiCaller(Generic[T]):
    """
    调用api的执行器
    """

    async def call_api_async(self, request: Request, model: Type[T]) -> T:
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
        if isinstance(data, dict):
            return model.model_validate(data)
        elif isinstance(data, list):
            data = cast(list, data)
            list_model = cast(Type[BaseListData], model)
            instance = list_model(items=data)
            return cast(T, instance)

        raise ResponseDataError

    def call_api_sync(self, request: Request, model: Type[T]) -> T:
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
        if isinstance(data, dict):
            return model.model_validate(data)
        elif isinstance(data, list):
            data = cast(list, data)
            list_model = cast(Type[BaseListData], model)
            instance = list_model(items=data)
            return cast(T, instance)

        raise ResponseDataError


def make_request(func_name: str, **kwargs) -> Request:
    """
    生成请求
    """
    api_name = func_name.replace("_", "/")
    url = API_URL + api_name
    return Request(name=func_name, url=url, data=kwargs)
