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

### Websocket接口

websocket底层使用websockets包，只提供异步接口，配合asyncio使用。

#### 连接websocket

```python
from jx3apifun import get_websocket_handler

handler = get_websocket_handler()

await handler.start_connect()
```

#### 断开连接

```python
from jx3apifun import get_websocket_handler

handler = get_websocket_handler()

await handler.close_connect()
```

#### 调用接口

使用websocket通信来查询接口，需要先连接ws才行。

```python
from jx3apifun import get_websocket_handler

handler = get_websocket_handler()

await handler.active_calendar(server="梦江南")
```

#### 注册事件

注册websocket事件

```python
from jx3apifun import get_websocket_handler
from jx3apifun.websocket.event import EventQiyu, EventType, EventModel

handler = get_websocket_handler()

# 注册奇遇事件
@handler.register_event(EventType.Qiyu)
async def _(event: EventQiyu)-> None:
    # do something
    pass

# 注册全部事件
@handler.register_event(EventType.All)
async def _(event: EventModel)-> None:
    # do something
    pass
```

注意：

- 注册事件类型必须和event的数据模型相同，否则报错（及EventType.Qiyu的event注释是EventQiyu
- 可以注册全部事件（但不推荐，因为event字段不确定），注册全部事件event标注为基类EventModel
- 每个事件可以注册多个处理器

### 日志模块

sdk默认不提供日志打印，如果想要查看模块的日志信息，可以自己实现满足 `LoggerProtocol` 的logger，并使用接口 `set_logger` 来设置日志记录器。

注意：

- 设置的日志需要满足 `LoggerProtocol` 协议，需要有 `info`、`debug`、`warning`、`error`4个接口。
- 如果你使用logging或者loguru，可以直接使用 `set_logger` 接口来设置，但是为了满足协议，需要使用 `logger_wrapper` 进行转换

自定义的日志实现例子如下：

```python
from jx3apifun import set_logger

class ConsoleLogger:
    
    def info(self, message: str, *args, **kwargs) -> None:
        """
        信息日志
        """
        print(f"[INFO] {message}")

    def debug(self, message: str, *args, **kwargs) -> None:
        """
        调试日志
        """
        print(f"[DEBUG] {message}")

    def warning(self, message: str, *args, **kwargs) -> None:
        """
        警告日志
        """
        print(f"[WARNING] {message}")

    def error(self, message: str, *args, **kwargs) -> None:
        """
        错误日志
        """
        print(f"[ERROR] {message}")
        
logger = ConsoleLogger()
set_logger(logger)
```

如果使用logging或者loguru，则可以是以下方式方式：

```python
from jx3apifun import set_logger, logger_wrapper

# logging
import logging

logger = logging.getLogger("xxx")
set_logger(logger_wrapper(logger))

# loguru
from loguru import logger

set_logger(logger_wrapper(logger))
```

