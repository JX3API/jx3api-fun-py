import asyncio
import logging
import sys
from pathlib import Path

# 将外部包的路径添加到模块搜索路径中
external_package_path = Path(__file__).absolute().parent.parent
sys.path.append(str(external_package_path))

from jx3apifun import get_websocket_handler, logger_wrapper, set_logger  # noqa: E402
from jx3apifun.websoket.event import EventModel, EventType  # noqa: E402

handler = get_websocket_handler()
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("jx3apifun")
set_logger(logger_wrapper(logger))


@handler.register_event(EventType.All)
async def handle_all_event(event: EventModel) -> None:
    logger.info(f"收到ws事件: {event}")


async def main():
    await handler.start_connect()
    await asyncio.sleep(5)
    result = await handler.data_active_calendar()
    logger.info(f"收到ws结果：{result}")
    while True:
        try:
            await asyncio.sleep(1)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    asyncio.run(main())
