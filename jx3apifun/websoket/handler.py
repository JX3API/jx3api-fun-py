import inspect
from functools import wraps
from typing import Any, Callable, Coroutine, ParamSpec, TypeVar

from jx3apifun.interface_async import ApiInterfaceAsync
from jx3apifun.model import BaseData

from .caller import ApiCaller, make_request

T = TypeVar("T", bound=BaseData)
P = ParamSpec("P")


class WebsocketHandler(ApiInterfaceAsync):
    """
    websocket handler
    """

    def __init__(self) -> None:
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
            caller = ApiCaller[T]()
            return await caller(request, model)

        return wrapper
