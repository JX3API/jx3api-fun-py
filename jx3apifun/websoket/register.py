import asyncio
import inspect
import traceback
from typing import Any, Callable, Coroutine, Generic, TypeVar

from jx3apifun.exceptions import EventParamError
from jx3apifun.logger import DefaultLogger, LoggerProtocol

from .event import EventModel, EventType

T = TypeVar("T", bound=EventModel)


class Register(Generic[T]):
    """
    事件注册器
    """

    logger: LoggerProtocol = DefaultLogger()
    """logger"""
    handler_map: dict[EventType, list[Callable[[T], Coroutine[Any, Any, None]]]] = {}
    """handler map"""

    def __new__(cls) -> "Register":
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def set_logger(self, logger: LoggerProtocol) -> None:
        """
        设置日志器
        """
        self.logger = logger

    def register(
        self, action: EventType, func: Callable[[T], Coroutine[Any, Any, None]]
    ) -> None:
        """
        注册事件
        """
        self.check_parameter(action, func)
        if action not in self.handler_map:
            self.handler_map[action] = []
        self.handler_map[action].append(func)

    def check_parameter(
        self, action: EventType, func: Callable[[T], Coroutine[Any, Any, None]]
    ) -> None:
        """
        校验参数
        """
        signature = inspect.signature(func)
        parameters = signature.parameters
        if len(parameters) != 1:
            raise EventParamError(
                f"事件处理函数[{func.__name__}]中，注册事件参数数量错误."
            )
        param_type = list(parameters.values())[0].annotation
        if not issubclass(param_type, EventModel):
            raise EventParamError(
                f"事件处理函数[{func.__name__}]中，注册事件参数类型错误."
            )
        if action != param_type.action:
            raise EventParamError(
                f"事件处理函数[{func.__name__}]中，注册的事件[{action}]和传递的事件参数[{param_type}]不匹配."
            )

    async def run_handler(self, event: T) -> None:
        """
        运行事件
        """
        if event.action == EventType.All:
            self.logger.error(f"ws接收到未知事件：{event}")
            return
        try:
            await self.run_handler_simple(event)
            await self.run_handler_all(event)
        except Exception:
            self.logger.error(f"ws事件处理发生错误: {traceback.format_exc()}")

    async def run_handler_simple(self, event: T) -> None:
        """
        对于单个事件运行
        """
        if coros := [func(event) for func in self.handler_map.get(event.action, [])]:
            await asyncio.gather(*coros)

    async def run_handler_all(self, event: EventModel) -> None:
        """
        对于所有事件运行
        """
        if coros := [func(event) for func in self.handler_map.get(EventType.All, [])]:
            await asyncio.gather(*coros)
