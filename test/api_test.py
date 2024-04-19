import sys
from pathlib import Path

# 将外部包的路径添加到模块搜索路径中
external_package_path = Path(__file__).absolute().parent.parent
sys.path.append(str(external_package_path))

from jx3apifun import get_websocket_handler  # noqa: E402


async def main():
    handler = get_websocket_handler()
    await handler.start_connect()
