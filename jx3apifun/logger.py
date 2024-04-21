from typing import Protocol


class LoggerProtocol(Protocol):
    """
    日志协议
    """

    def info(self, message: str, *args, **kwargs) -> None:
        """
        信息日志
        """
        ...

    def debug(self, message: str, *args, **kwargs) -> None:
        """
        调试日志
        """
        ...

    def warning(self, message: str, *args, **kwargs) -> None:
        """
        警告日志
        """
        ...

    def error(self, message: str, *args, **kwargs) -> None:
        """
        错误日志
        """
        ...


class DefaultLogger:
    """
    默认日志器
    """

    def info(self, message: str, *args, **kwargs) -> None:
        """
        信息日志
        """
        ...

    def debug(self, message: str, *args, **kwargs) -> None:
        """
        调试日志
        """
        ...

    def warning(self, message: str, *args, **kwargs) -> None:
        """
        警告日志
        """
        ...

    def error(self, message: str, *args, **kwargs) -> None:
        """
        错误日志
        """
        ...
