import sys
from pathlib import Path

# 将外部包的路径添加到模块搜索路径中
external_package_path = Path(__file__).absolute().parent.parent
sys.path.append(str(external_package_path))

from jx3apifun import get_sync_handler, set_ticket, set_token  # noqa: E402

handler = get_sync_handler()
set_ticket("ticket")
set_token("token")

data = handler.data_active_current()

print(data)
