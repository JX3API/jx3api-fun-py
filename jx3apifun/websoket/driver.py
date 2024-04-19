import websockets
from websockets.client import WebSocketClientProtocol

from jx3apifun.const import WS_RUL


class WebsocketDriver:
    """
    websocket driver
    """

    token: str = ""
    """token"""
    ticket: str = ""
    """ticket"""
    ws: WebSocketClientProtocol = WebSocketClientProtocol()
    """connection object"""
    connected: bool = False
    """connection status"""

    def __new__(cls) -> "WebsocketDriver":
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def set_token(self, token: str) -> None:
        """
        set token
        """
        self.token = token

    def set_ticket(self, ticket: str) -> None:
        """
        set ticket
        """
        self.ticket = ticket

    async def start_connect(self) -> None:
        """
        start connect
        """
        self.ws = await websockets.connect(WS_RUL)
        self.connected = True

    async def close(self) -> None:
        """
        close connection
        """
        self.connected = False
        await self.ws.close()

    async def connection_handler(self) -> None:
        """
        connection handler
        """
        while self.connected:
            try:
                _ = await self.ws.recv()

            except websockets.ConnectionClosed:
                self.connected = False
                break
