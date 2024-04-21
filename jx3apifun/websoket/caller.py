from typing import (
    Generic,
    ParamSpec,
    Type,
    TypeVar,
    Union,
    cast,
)

from pydantic import TypeAdapter

from jx3apifun.exceptions import RequestError, ResponseDataError
from jx3apifun.logger import LoggerProtocol
from jx3apifun.model import BaseData, Request
from jx3apifun.permission import is_require_ticket, is_require_token

from .driver import WebsocketDriver

T = TypeVar("T", bound=BaseData)
P = ParamSpec("P")
ResponseModel = Union[T, list[T]]


class ApiCaller(Generic[T]):
    """
    调用api的执行器
    """

    logger: LoggerProtocol

    def __init__(self, logger: LoggerProtocol) -> None:
        self.logger = logger

    async def __call__(self, request: Request, model: Type[ResponseModel]) -> T:
        """
        调用api
        """
        driver = WebsocketDriver()
        if not driver.connected:
            raise RequestError("ws服务未连接")
        if is_require_token(request.name):
            driver.check_token(request)
        if is_require_ticket(request.name):
            driver.check_ticket(request)

        self.logger.debug(f"使用ws请求: {request.name}, data: {request.data}")
        response = await driver.request(request)
        if response.code != 200:
            raise ResponseDataError(
                f"请求失败，code: {response.code}, msg: {response.msg}"
            )
        data = response.data
        self.logger.debug(f"接收到ws请求结果: {data}")
        adapter = TypeAdapter(model)
        return cast(T, adapter.validate_python(data))


def make_request(func_name: str, **kwargs) -> Request:
    """
    生成请求
    """
    url = func_name.replace("_", "/")
    return Request(name=func_name, url=url, data=kwargs)
