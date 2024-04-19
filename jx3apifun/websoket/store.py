import asyncio
import sys
from typing import Any, Dict, Optional, cast


class ResultStore:
    def __init__(self) -> None:
        self._seq: int = 1
        self._futures: Dict[int, asyncio.Future] = {}

    @property
    def current_seq(self) -> int:
        return self._seq

    def get_seq(self) -> int:
        s = self._seq
        self._seq = (self._seq + 1) % sys.maxsize
        return s

    def add_result(self, result: Dict[str, Any]) -> None:
        echo = result.get("echo")
        echo = cast(int, echo)
        if future := self._futures.get(echo):
            future.set_result(result)

    async def fetch(self, seq: int, timeout: Optional[float]) -> Dict[str, Any]:
        future = asyncio.get_event_loop().create_future()
        self._futures[seq] = future
        try:
            return await asyncio.wait_for(future, timeout)
        finally:
            del self._futures[seq]
