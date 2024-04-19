import asyncio
from typing import Any, Callable, Coroutine, Generic, TypeVar

from .event import EventModel, EventType

T = TypeVar("T", bound=EventModel)


class Register(Generic[T]):
    """
    事件注册器
    """

    handler_map: dict[EventType, list[Callable[[T], Coroutine[Any, Any, None]]]] = {}
    """handler map"""

    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def register(
        self, action: EventType, func: Callable[[T], Coroutine[Any, Any, None]]
    ) -> None:
        """
        注册事件
        """
        if action not in self.handler_map:
            self.handler_map[action] = []
        self.handler_map[action].append(func)

    async def run_handler(self, event: T) -> None:
        """
        运行事件
        """
        if event.action == EventType.All:
            # TODO: 未知事件处理
            print(f"未知事件: {event}")
            return
        try:
            await self.run_handler_simple(event)
            await self.run_handler_all(event)
        except Exception as e:
            print(e)

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
