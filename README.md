# Jx3api for fun
一款女生自用的jx3api sdk，本仓库主要是为了整活儿，正经使用应该选择受姐姐的[jx3api](https://github.com/JX3API/jx3api-py)。

## 安装

###  pypi

```bash
pip install --no-cache -U jx3apifun
```

### github（不推荐）

```bash
pip install --no-cache -U git+https://github.com/JX3API/jx3api-fun-py.git
```

## 使用说明

### 初始化（设置token和ticket）

```python
from jx3apifun import set_token, set_ticket

set_token("token")
set_ticket("ticket")
```

### 同步接口

```python
from jx3apifun import get_sync_handler

handler = get_sync_handler()

handler.active_calendar(server="梦江南")
```

### 异步接口

```python
from jx3apifun import get_async_handler

handler = get_async_handler()

await handler.active_calendar(server="梦江南")
```

### Websocket接口（未实现）

注意事项：还没写（

```python
from jx3apifun import get_websocket_handler

handler = get_websocket_handler()

还没写
```



