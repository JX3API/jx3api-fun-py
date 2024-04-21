from .http import AsyncApiHandler, AsyncDriver, SyncApiHandler, SyncDriver
from .logger import LoggerProtocol
from .websoket import Register, WebsocketDriver, WebsocketHandler


class Jx3Api:
    """
    jx3api管理器，用于管理jx3api的各种接口
    """

    sync_handler: SyncApiHandler = SyncApiHandler()
    """同步接口处理器"""
    sync_driver: SyncDriver = SyncDriver()
    """同步驱动器"""
    async_handler: AsyncApiHandler = AsyncApiHandler()
    """异步接口处理器"""
    async_driver: AsyncDriver = AsyncDriver()
    """异步驱动器"""
    websocket_handler: WebsocketHandler = WebsocketHandler()
    """websocket接口处理器"""
    websocket_driver: WebsocketDriver = WebsocketDriver()
    """websocket驱动器"""

    def __new__(cls) -> "Jx3Api":
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def set_logger(self, logger: LoggerProtocol) -> None:
        """
        设置日志器
        """
        register = Register()
        register.set_logger(logger)
        self.sync_handler.set_logger(logger)
        self.sync_driver.set_logger(logger)
        self.async_handler.set_logger(logger)
        self.async_driver.set_logger(logger)
        self.websocket_handler.set_logger(logger)
        self.websocket_driver.set_logger(logger)

    def set_tiket(self, ticket: str) -> None:
        """
        设置ticket
        """
        self.sync_driver.set_ticket(ticket)
        self.async_driver.set_ticket(ticket)
        self.websocket_driver.set_ticket(ticket)

    def set_token(self, token: str) -> None:
        """
        设置token
        """
        self.sync_driver.set_token(token)
        self.async_driver.set_token(token)
        self.websocket_driver.set_token(token)

    def set_ws_token(self, token: str) -> None:
        """
        设置ws token
        """
        self.websocket_driver.set_ws_token(token)
