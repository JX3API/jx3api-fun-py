from .http import AsyncApiHandler, AsyncDriver, SyncApiHandler, SyncDriver
from .websoket import WebsocketHandler


class Jx3Api:
    """
    jx3api管理器，用于管理jx3api的各种接口
    """

    async_handler: AsyncApiHandler = AsyncApiHandler()
    """异步接口处理器"""
    sync_handler: SyncApiHandler = SyncApiHandler()
    """同步接口处理器"""
    websocket_handler: WebsocketHandler = WebsocketHandler()
    """websocket接口处理器"""
    async_driver: AsyncDriver = AsyncDriver()
    """异步驱动器"""
    sync_driver: SyncDriver = SyncDriver()
    """同步驱动器"""

    def __new__(cls) -> "Jx3Api":
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
            cls._instance.__init__()
        return cls._instance

    def set_tiket(self, ticket: str) -> None:
        """
        设置ticket
        """
        self.sync_driver.set_ticket(ticket)
        self.async_driver.set_ticket(ticket)

    def set_token(self, token: str) -> None:
        """
        设置token
        """
        self.sync_driver.set_token(token)
        self.async_driver.set_token(token)
