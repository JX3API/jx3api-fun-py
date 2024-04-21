import inspect
from functools import wraps
from typing import Any, Callable, Coroutine, ParamSpec, TypeVar, Union

from jx3apifun.interface import ApiInterface
from jx3apifun.interface_async import ApiInterfaceAsync
from jx3apifun.logger import DefaultLogger, LoggerProtocol
from jx3apifun.model import BaseData

from .caller import ApiCaller, make_request

T = TypeVar("T", bound=BaseData)
P = ParamSpec("P")
ResponseModel = Union[T, list[T]]


class SyncApiHandler(ApiInterface):
    """
    同步接口处理器
    """

    logger: LoggerProtocol = DefaultLogger()

    def __init__(self) -> None:
        obj = ApiInterface()
        methods_list = [method for method in dir(obj) if callable(getattr(obj, method))]
        for method in methods_list:
            if method.startswith("_"):
                continue
            func = getattr(obj, method)
            setattr(self, method, self.__sync_caller__(func))

    @staticmethod
    def __sync_caller__(func: Callable[P, ResponseModel]) -> Callable[P, ResponseModel]:
        """
        同步调用接口
        """

        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> ResponseModel:
            signature = inspect.signature(func)
            bound = signature.bind(*args, **kwargs)
            bound.apply_defaults()
            if "self" in bound.arguments:
                bound.arguments.pop("self")
            request = make_request(func.__name__, **bound.arguments)
            model = signature.return_annotation
            caller = ApiCaller()
            return caller.call_api_sync(request, model)

        return wrapper

    def set_logger(self, logger: LoggerProtocol) -> None:
        """
        设置日志器
        """
        self.logger = logger


class AsyncApiHandler(ApiInterfaceAsync):
    """
    异步接口处理器
    """

    logger: LoggerProtocol = DefaultLogger()

    def __init__(self) -> None:
        obj = ApiInterfaceAsync()
        methods_list = [method for method in dir(obj) if callable(getattr(obj, method))]
        for method in methods_list:
            if method.startswith("_"):
                continue
            func = getattr(obj, method)
            setattr(self, method, self.__async_caller__(func))

    def __async_caller__(
        self, func: Callable[P, Coroutine[Any, Any, ResponseModel]]
    ) -> Callable[P, Coroutine[Any, Any, ResponseModel]]:
        """
        异步调用接口
        """

        @wraps(func)
        async def wrapper(*args: P.args, **kwargs: P.kwargs) -> ResponseModel:
            signature = inspect.signature(func)
            bound = signature.bind(*args, **kwargs)
            bound.apply_defaults()
            if "self" in bound.arguments:
                bound.arguments.pop("self")
            request = make_request(func.__name__, **bound.arguments)
            model = signature.return_annotation
            caller = ApiCaller()
            return await caller.call_api_async(request, model)

        return wrapper

    def set_logger(self, logger: LoggerProtocol) -> None:
        """
        设置日志器
        """
        self.logger = logger
