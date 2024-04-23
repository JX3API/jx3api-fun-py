from enum import Enum
from typing import ClassVar

from msgspec import Struct


class EventType(Enum):
    """事件类型"""

    All = 0
    """全部事件"""
    Welcome = 10000
    """欢迎消息"""
    Qiyu = 1001
    """奇遇报时"""
    ZhuaMa = 1002
    """抓马报时"""
    Buhuo = 1003
    """捕获马驹"""
    FuyaoStart = 1004
    """扶摇开始"""
    FuyaoEnd = 1005
    """扶摇结束，点名"""
    Yanhua = 1006
    """烟花报时"""
    Xuanjing = 1007
    """玄晶报时"""
    Zhuihun = 1008
    """追魂点名"""
    ZhuEr = 1009
    """诸恶事件"""
    DiluFresh = 1010
    """的卢刷新"""
    DiluEnd = 1011
    """的卢捕获"""
    DiluJingPai = 1012
    """的卢竞拍"""
    Liangcang = 1101
    """粮仓被劫"""
    Dajiang = 1102
    """大将重置"""
    Daqi = 1103
    """大旗被夺"""
    Judian = 1104
    """据点占领（有帮会）"""
    JudianNo = 1105
    """据点占领（无帮会）"""
    Gongxian = 1106
    """贡献结算"""
    Kaifu = 2001
    """开服监控"""
    Xinwen = 2002
    """新闻资讯"""
    Gengxin = 2003
    """游戏更新"""
    Bagua = 2004
    """八卦速报"""
    Guanai = 2005
    """关隘预告"""
    Yuncong = 2006
    """云从预告"""


class EventModel(Struct, forbid_unknown_fields=False):
    """
    事件数据模型
    """

    action: ClassVar[EventType] = EventType.All
    """事件类型"""


class EventWelcome(EventModel, kw_only=True):
    """
    欢迎消息
    """

    action: ClassVar[EventType] = EventType.Welcome
    """事件类型"""
    message: str
    """消息"""


class EventQiyu(EventModel, kw_only=True):
    """
    奇遇报时
    """

    action: ClassVar[EventType] = EventType.Qiyu
    """事件类型"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    name: str
    """角色名"""
    event: str
    """奇遇名"""
    level: int
    """奇遇等级"""
    time: int
    """时间戳"""


class EventZhuaMa(EventModel, kw_only=True):
    """
    抓马报时
    """

    action: ClassVar[EventType] = EventType.ZhuaMa
    """事件类型"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    map_name: str
    """地图名"""
    min_time: int
    """最小时间"""
    max_time: int
    """最大时间"""
    time: int
    """时间戳"""


class EventBuhuo(EventModel, kw_only=True):
    """
    捕获马驹
    """

    action: ClassVar[EventType] = EventType.Buhuo
    """事件类型"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    name: str
    """角色名"""
    map_name: str
    """地图名"""
    horse: str
    """马驹名"""
    time: int
    """时间戳"""


class EventFuyaoStart(EventModel, kw_only=True):
    """
    扶摇开始
    """

    action: ClassVar[EventType] = EventType.FuyaoStart
    """事件类型"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    time: int
    """时间戳"""


class EventFuyaoEnd(EventModel, kw_only=True):
    """
    扶摇结束
    """

    action: ClassVar[EventType] = EventType.FuyaoEnd
    """事件类型"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    name: list[str]
    """角色名列表"""
    time: int
    """时间戳"""


class EventYanhua(EventModel, kw_only=True):
    """
    烟花报时
    """

    action: ClassVar[EventType] = EventType.Yanhua
    """事件类型"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    name: str
    """烟花名"""
    map_name: str
    """地图名"""
    sender: str
    """发送者"""
    recipient: str
    """接收者"""
    time: int
    """时间戳"""


class EventXuanjing(EventModel, kw_only=True):
    """
    玄晶报时
    """

    action: ClassVar[EventType] = EventType.Xuanjing
    """事件类型"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    role_name: str
    """获得者"""
    map_name: str
    """地图名"""
    name: str
    """玄晶名"""
    time: int
    """时间戳"""


class EventZhuihun(EventModel, kw_only=True):
    """
    追魂点名
    """

    action: ClassVar[EventType] = EventType.Zhuihun
    """事件类型"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    subserver: str
    """子服务器"""
    name: str
    """角色名"""
    realm: str
    """跨服名"""
    time: int
    """时间戳"""


class EventZhuEr(EventModel, kw_only=True):
    """
    诸恶事件
    """

    action: ClassVar[EventType] = EventType.ZhuEr
    """事件类型"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    map_name: str
    """地图名"""
    time: int
    """时间戳"""


class EventDiluFresh(EventModel, kw_only=True):
    """
    的卢刷新
    """

    action: ClassVar[EventType] = EventType.DiluFresh
    """事件类型"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    map_name: str
    """地图名"""
    name: str
    """的卢名"""
    time: int
    """时间戳"""


class EventDiluEnd(EventModel, kw_only=True):
    """
    的卢捕获
    """

    action: ClassVar[EventType] = EventType.DiluEnd
    """事件类型"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    role_name: str
    """获得者"""
    camp_name: str
    """阵营名"""
    map_name: str
    """地图名"""
    level: str
    """等级"""
    name: str
    """的卢名"""
    time: int
    """时间戳"""


class EventDiluJingPai(EventModel, kw_only=True):
    """
    的卢竞拍
    """

    action: ClassVar[EventType] = EventType.DiluJingPai
    """事件类型"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    role_name: str
    """竞拍者"""
    camp_name: str
    """阵营名"""
    name: str
    """的卢名"""
    amount: str
    """竞拍金额"""
    time: int
    """时间戳"""


class EventLiangcang(EventModel, kw_only=True):
    """
    粮仓被劫
    """

    action: ClassVar[EventType] = EventType.Liangcang
    """事件类型"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    castle: str
    """据点名"""
    camp_name: str
    """阵营名"""
    time: int
    """时间戳"""


class EventDajiang(EventModel, kw_only=True):
    """
    大将重置
    """

    action: ClassVar[EventType] = EventType.Dajiang
    """事件类型"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    name: str
    """据点名"""
    time: int
    """时间戳"""


class EventDaqi(EventModel, kw_only=True):
    """
    大旗被夺
    """

    action: ClassVar[EventType] = EventType.Daqi
    """事件类型"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    camp_name: str
    """阵营名"""
    map_name: str
    """地图名"""
    castle: str
    """据点名"""
    time: int
    """时间戳"""


class EventJudian(EventModel, kw_only=True):
    """
    据点占领（有帮会）
    """

    action: ClassVar[EventType] = EventType.Judian
    """事件类型"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    camp_name: str
    """阵营名"""
    tong_name: str
    """帮会名"""
    castle: str
    """据点名"""
    time: int
    """时间戳"""


class EventJudianNo(EventModel, kw_only=True):
    """
    据点占领（无帮会）
    """

    action: ClassVar[EventType] = EventType.JudianNo
    """事件类型"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    camp_name: str
    """阵营名"""
    castle: str
    """据点名"""
    time: int
    """时间戳"""


class EventGongxian(EventModel, kw_only=True):
    """
    贡献结算
    """

    action: ClassVar[EventType] = EventType.Gongxian
    """事件类型"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    camp_name: str
    """阵营名"""
    tong_list: list[str]
    """帮会列表"""
    time: int
    """时间戳"""


class EventKaifu(EventModel, kw_only=True):
    """
    开服监控
    """

    action: ClassVar[EventType] = EventType.Kaifu
    """事件类型"""
    server: str
    """服务器"""
    status: int
    """状态"""


class EventXinwen(EventModel, kw_only=True):
    """
    新闻资讯
    """

    action: ClassVar[EventType] = EventType.Xinwen
    """事件类型"""
    type: str
    """类型"""
    title: str
    """标题"""
    url: str
    """链接"""
    date: str
    """日期"""


class EventGengxin(EventModel, kw_only=True):
    """
    游戏更新
    """

    action: ClassVar[EventType] = EventType.Gengxin
    """事件类型"""
    old_version: str
    """旧版本"""
    new_version: str
    """新版本"""
    package_num: int
    """包数量"""
    package_size: str
    """包大小"""


class EventBagua(EventModel, kw_only=True):
    """
    八卦速报
    """

    action: ClassVar[EventType] = EventType.Bagua
    """事件类型"""
    subclass: str
    """子类"""
    server: str
    """服务器"""
    name: str
    """角色名"""
    title: str
    """标题"""
    url: str
    """链接"""
    date: str
    """日期"""


class EventGuanai(EventModel, kw_only=True):
    """
    关隘预告
    """

    action: ClassVar[EventType] = EventType.Guanai
    """事件类型"""
    server: str
    """服务器"""
    castle: str
    """据点名"""
    start: int
    """首领刷新时间戳"""


class EventYuncong(EventModel, kw_only=True):
    """
    云从预告
    """

    action: ClassVar[EventType] = EventType.Yuncong
    """事件类型"""
    name: str
    """云从名"""
    site: str
    """位置"""
    desc: str
    """描述"""
    time: int
    """时间戳"""
