from .http import AsyncApiHandler, SyncApiHandler
from .jx3api import Jx3Api
from .websoket import WebsocketHandler

api_instance = Jx3Api()
"""
jx3api管理器实例, 用于管理jx3api的各种接口
"""


def get_websocket_handler() -> WebsocketHandler:
    """
    获取websocket接口处理器
    """
    return api_instance.websocket_handler


def get_sync_handler() -> SyncApiHandler:
    """
    获取同步接口处理器
    """
    return api_instance.sync_handler


def get_async_handler() -> AsyncApiHandler:
    """
    获取异步接口处理器
    """
    return api_instance.async_handler


def set_ticket(ticket: str) -> None:
    """
    设置ticket
    """
    api_instance.set_tiket(ticket)


def set_token(token: str) -> None:
    """
    设置token
    """
    api_instance.set_token(token)
