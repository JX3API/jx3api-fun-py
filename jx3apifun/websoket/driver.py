import asyncio
import json
from typing import cast

import websockets
from websockets.client import WebSocketClientProtocol

from jx3apifun.const import WS_RUL, WSAPI_TIMEOUT
from jx3apifun.exceptions import TicketError, TokenError
from jx3apifun.logger import AbsLogger, LoggerProtocol
from jx3apifun.model import Request, Response

from .collator import Collator
from .event import EventModel, EventType
from .register import Register
from .store import ResultStore


class WebsocketDriver:
    """
    websocket driver
    """

    logger: LoggerProtocol = AbsLogger()
    """logger"""
    token: str = ""
    """token"""
    ticket: str = ""
    """ticket"""
    store: ResultStore = ResultStore()
    """store object"""
    collator: Collator = Collator()
    """collator object"""
    register: Register = Register()
    """register object"""
    ws: WebSocketClientProtocol = WebSocketClientProtocol()
    """connection object"""
    connected: bool = False
    """connection status"""

    def __new__(cls) -> "WebsocketDriver":
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def set_logger(self, logger: LoggerProtocol) -> None:
        """
        set logger
        """
        self.logger = logger

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
        echo = self.store.get_seq()
        data = {"action": request.url, "data": request.data, "echo": echo}
        data_str = json.dumps(data)
        await self.ws.send(data_str)
        result = await self.store.fetch(echo, WSAPI_TIMEOUT)
        return Response.model_validate(result)

    async def start_connect(self) -> None:
        """
        start connect
        """
        if self.connected:
            return
        self.ws = await websockets.connect(WS_RUL)
        self.connected = True
        asyncio.create_task(self.handle_connection())

    async def close_connect(self) -> None:
        """
        关闭连接
        """
        self.connected = False
        await self.ws.close()

    async def handle_connection(self) -> None:
        """
        处理连接
        """
        while self.connected:
            try:
                data = await self.ws.recv()
                self.logger.debug(f"ws接收到消息：{data}")
                if isinstance(data, str):
                    self.handle_message(data)

            except websockets.ConnectionClosed:
                self.connected = False
                break

    def handle_message(self, message: str) -> None:
        """
        处理消息
        """
        data = json.loads(message)
        if data.get("echo") is not None:
            self.store.add_result(data)
        else:
            event = self.message_to_event(data)
            self.handle_event(event)

    def handle_event(self, event: EventModel) -> None:
        """
        处理事件
        """
        asyncio.create_task(self.register.run_handler(event))

    def message_to_event(self, message: dict) -> EventModel:
        """
        消息转事件
        """
        action = message.get("action")
        try:
            action = EventType(action)
        except ValueError:
            action = EventType.All
        if action == EventType.Welcome:
            data = {"message": message.get("message")}
        else:
            data = message.get("data")
        data = cast(dict, data)
        data["action"] = action
        model = self.collator.get_model(action)
        return model.model_validate(data)
