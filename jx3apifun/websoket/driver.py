import asyncio

import websockets
from websockets.client import WebSocketClientProtocol

from jx3apifun.const import WS_RUL
from jx3apifun.exceptions import TicketError, TokenError
from jx3apifun.model import Request, Response


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

    def check_token(self, request: Request) -> Request:
        """
        检查token
        """
        if self.token == "":
            raise TokenError
        request.data["token"] = self.token
        return request

    def check_ticket(self, request: Request) -> Request:
        """
        检查ticket
        """
        if self.ticket == "":
            raise TicketError
        request.data["ticket"] = self.ticket
        return request

    async def request(self, request: Request) -> Response:
        """
        send request
        """
        if not self.connected:
            await self.start_connect()

        await self.ws.send(request.data)
        return Response(code=200, data=[], msg="", time=0)

    async def start_connect(self) -> None:
        """
        start connect
        """
        if self.connected:
            return
        self.ws = await websockets.connect(WS_RUL)
        self.connected = True
        asyncio.create_task(self.__connection_handler())

    async def close_connect(self) -> None:
        """
        close connection
        """
        self.connected = False
        await self.ws.close()

    async def __connection_handler(self) -> None:
        """
        connection handler
        """
        while self.connected:
            try:
                _ = await self.ws.recv()

            except websockets.ConnectionClosed:
                self.connected = False
                break
