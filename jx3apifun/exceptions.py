class JX3APIException(Exception):
    """Base class for exceptions in this module."""

    pass


class NetworkError(JX3APIException):
    """网络异常"""

    pass


class ResponseDataError(JX3APIException):
    """返回数据异常"""

    pass


class TokenError(JX3APIException):
    """token检测异常"""

    pass


class TicketError(JX3APIException):
    """ticket检测异常"""

    pass
