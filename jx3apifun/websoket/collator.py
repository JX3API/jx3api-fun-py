import inspect
from typing import Type

from . import event


class Collator:
    """
    事件模型管理器
    """

    model_map: dict[event.EventType, Type[event.EventModel]]

    def __init__(self) -> None:
        self.model_map = {}
        for _, obj in inspect.getmembers(event):
            if inspect.isclass(obj) and issubclass(obj, event.EventModel):
                if obj == event.EventModel:
                    continue
                self.model_map[obj.action] = obj

    def get_model(self, action: event.EventType) -> Type[event.EventModel]:
        """
        获取事件模型
        """
        return self.model_map.get(action, event.EventModel)
