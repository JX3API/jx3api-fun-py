import inspect
from functools import wraps
from typing import Any, Callable, Coroutine, ParamSpec, TypeVar

from jx3apifun.interface_async import ApiInterfaceAsync
from jx3apifun.logger import AbsLogger, LoggerProtocol
from jx3apifun.model import BaseData

from .caller import ApiCaller, make_request
from .driver import WebsocketDriver
from .event import EventModel, EventType
from .register import Register

T = TypeVar("T", bound=BaseData)
P = ParamSpec("P")

M = TypeVar("M", bound=EventModel)


class WebsocketHandler(ApiInterfaceAsync):
    """
    websocket handler
    """

    register: Register
    """register"""
    logger: LoggerProtocol
    """logger"""

    def __init__(self) -> None:
        self.logger = AbsLogger()
        self.register = Register()

        obj = ApiInterfaceAsync()
        methods_list = [method for method in dir(obj) if callable(getattr(obj, method))]
        for method in methods_list:
            if method.startswith("_"):
                continue
            func = getattr(obj, method)
            setattr(self, method, self.__async_caller__(func))

    def __async_caller__(
        self, func: Callable[P, Coroutine[Any, Any, T]]
    ) -> Callable[P, Coroutine[Any, Any, T]]:
        """
        异步调用接口
        """

        @wraps(func)
        async def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            signature = inspect.signature(func)
            bound = signature.bind(*args, **kwargs)
            bound.apply_defaults()
            if "self" in bound.arguments:
                bound.arguments.pop("self")
            request = make_request(func.__name__, **bound.arguments)
            model = signature.return_annotation
            caller = ApiCaller[T](self.logger)
            return await caller(request, model)

        return wrapper

    def set_logger(self, logger: LoggerProtocol) -> None:
        """
        设置日志器
        """
        self.logger = logger
        self.register.set_logger(logger)

    async def start_connect(self) -> None:
        """
        开启ws连接
        """

        driver = WebsocketDriver()
        await driver.start_connect()

    async def close_connect(self) -> None:
        """
        关闭ws连接
        """

        driver = WebsocketDriver()
        await driver.close_connect()

    def register_event(self, type: EventType):
        """
        注册事件
        """

        def wrapper(
            func: Callable[[M], Coroutine[Any, Any, None]],
        ) -> Callable[[M], Coroutine[Any, Any, None]]:
            """
            包装器
            """
            self.register.register(type, func)
            return func

        return wrapper
