from httpx import AsyncClient, Client
from msgspec import json

from jx3apifun.exceptions import NetworkError, TicketError, TokenError
from jx3apifun.logger import DefaultLogger, LoggerProtocol
from jx3apifun.model import Request, Response


class SyncDriver:
    """
    同步接口驱动器
    """

    logger: LoggerProtocol = DefaultLogger()
    """日志器"""
    client: Client = Client()
    """客户端"""
    token: str = ""
    """token"""
    ticket: str = ""
    """ticket"""

    def __new__(cls) -> "SyncDriver":
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def set_logger(self, logger: LoggerProtocol) -> None:
        """
        设置日志器
        """
        self.logger = logger

    def set_token(self, token: str) -> None:
        """
        设置token
        """
        self.token = token

    def set_ticket(self, ticket: str) -> None:
        """
        设置ticket
        """
        self.ticket = ticket

    def check_token(self, request: Request) -> Request:
        """
        检查token
        """
        if self.token == "":
            raise TokenError("token is empty")
        request.data["token"] = self.token
        return request

    def check_ticket(self, request: Request) -> Request:
        """
        检查ticket
        """
        if self.ticket == "":
            raise TicketError("ticket is empty")
        request.data["ticket"] = self.ticket
        return request

    def request(self, request: Request) -> Response:
        """
        发送请求
        """
        try:
            response = self.client.post(request.url, data=request.data)
            if response.status_code != 200:
                raise NetworkError("网络请求错误")

            return json.decode(response.content, type=Response)

        except Exception as e:
            raise NetworkError from e


class AsyncDriver:
    """
    异步接口驱动器
    """

    logger: LoggerProtocol = DefaultLogger()
    """日志器"""
    client: AsyncClient = AsyncClient()
    """客户端"""
    token: str = ""
    """token"""
    ticket: str = ""
    """ticket"""

    def __new__(cls) -> "AsyncDriver":
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def set_logger(self, logger: LoggerProtocol) -> None:
        """
        设置日志器
        """
        self.logger = logger

    def set_token(self, token: str) -> None:
        """
        设置token
        """
        self.token = token

    def set_ticket(self, ticket: str) -> None:
        """
        设置ticket
        """
        self.ticket = ticket

    def check_token(self, request: Request) -> Request:
        """
        检查token
        """
        if self.token == "":
            raise TokenError("token为空")
        request.data["token"] = self.token
        return request

    def check_ticket(self, request: Request) -> Request:
        """
        检查ticket
        """
        if self.ticket == "":
            raise TicketError("ticket为空")
        request.data["ticket"] = self.ticket
        return request

    async def request(self, request: Request) -> Response:
        """
        发送请求
        """

        try:
            response = await self.client.post(request.url, data=request.data)
            if response.status_code != 200:
                raise NetworkError("网络请求错误")

            return json.decode(response.content, type=Response)

        except Exception as e:
            raise NetworkError from e
