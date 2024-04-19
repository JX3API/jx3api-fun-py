from typing import Any, Callable, Coroutine, ParamSpec, TypeVar, Union

from .model import BaseData

T = TypeVar("T", bound=BaseData)
P = ParamSpec("P")

tp = Union[Callable[P, T], Callable[P, Coroutine[Any, Any, T]]]


token_func_set: set[str] = set()
ticket_func_set: set[str] = set()


def require_token(func: tp) -> tp:
    """
    此接口需要token
    """
    token_func_set.add(func.__name__)
    return func


def require_ticket(func: tp) -> tp:
    """
    此接口需要ticket
    """
    ticket_func_set.add(func.__name__)
    return func


def is_require_token(name: str) -> bool:
    """
    接口是否需要token
    """
    return name in token_func_set


def is_require_ticket(name: str) -> bool:
    """
    接口是否需要ticket
    """
    return name in ticket_func_set
