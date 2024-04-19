from enum import Enum

from pydantic import BaseModel, ConfigDict


class EventType(Enum):
    """事件类型"""

    All = 0
    """全部事件"""
    Welcome = 1000
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
    DiluStart = 1010
    """的卢消息"""
    DiluFresh = 1011
    """的卢刷新"""
    DiluEnd = 1012
    """的卢捕获"""
    DiluJingPai = 1013
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


class EventMsg(BaseModel):
    """事件消息"""

    action: int
    """事件类型"""
    data: dict
    """事件数据"""


class EventModel(BaseModel):
    """
    事件数据模型
    """

    model_config = ConfigDict(extra="allow")
    action: EventType = EventType.All
    """事件类型"""


class EventWelcome(EventModel):
    """
    欢迎消息
    """

    action: EventType = EventType.Welcome
    """事件类型"""


class EventQiyu(EventModel):
    """
    奇遇报时
    """

    action: EventType = EventType.Qiyu
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


class EventZhuaMa(EventModel):
    """
    抓马报时
    """

    action: EventType = EventType.ZhuaMa
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


class EventBuhuo(EventModel):
    """
    捕获马驹
    """

    action: EventType = EventType.Buhuo
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


class EventFuyaoStart(EventModel):
    """
    扶摇开始
    """

    action: EventType = EventType.FuyaoStart
    """事件类型"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    time: int
    """时间戳"""


class EventFuyaoEnd(EventModel):
    """
    扶摇结束
    """

    action: EventType = EventType.FuyaoEnd
    """事件类型"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    name: list[str]
    """角色名列表"""
    time: int
    """时间戳"""


class EventYanhua(EventModel):
    """
    烟花报时
    """

    action: EventType = EventType.Yanhua
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


class EventXuanjing(EventModel):
    """
    玄晶报时
    """

    action: EventType = EventType.Xuanjing
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


class EventZhuihun(EventModel):
    """
    追魂点名
    """

    action: EventType = EventType.Zhuihun
    """事件类型"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    subserver: str
    """子服务器"""
    name: str
    """角色名"""
    time: int
    """时间戳"""


class EventZhuEr(EventModel):
    """
    诸恶事件
    """

    action: EventType = EventType.ZhuEr
    """事件类型"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    map_name: str
    """地图名"""
    time: int
    """时间戳"""


class EventDiluStart(EventModel):
    """
    的卢报时
    """

    action: EventType = EventType.DiluStart
    """事件类型"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    name: str
    """的卢名"""
    time: int
    """时间戳"""


class EventDiluFresh(EventModel):
    """
    的卢刷新
    """

    action: EventType = EventType.DiluFresh
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


class EventDiluEnd(EventModel):
    """
    的卢捕获
    """

    action: EventType = EventType.DiluEnd
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


class EventDiluJingPai(EventModel):
    """
    的卢竞拍
    """

    action: EventType = EventType.DiluJingPai
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


class EventLiangcang(EventModel):
    """
    粮仓被劫
    """

    action: EventType = EventType.Liangcang
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


class EventDajiang(EventModel):
    """
    大将重置
    """

    action: EventType = EventType.Dajiang
    """事件类型"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    name: str
    """据点名"""
    time: int
    """时间戳"""


class EventDaqi(EventModel):
    """
    大旗被夺
    """

    action: EventType = EventType.Daqi
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


class EventJudian(EventModel):
    """
    据点占领（有帮会）
    """

    action: EventType = EventType.Judian
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


class EventJudianNo(EventModel):
    """
    据点占领（无帮会）
    """

    action: EventType = EventType.JudianNo
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


class EventGongxian(EventModel):
    """
    贡献结算
    """

    action: EventType = EventType.Gongxian
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


class EventKaifu(EventModel):
    """
    开服监控
    """

    action: EventType = EventType.Kaifu
    """事件类型"""
    server: str
    """服务器"""
    status: int
    """状态"""


class EventXinwen(EventModel):
    """
    新闻资讯
    """

    action: EventType = EventType.Xinwen
    """事件类型"""
    type: str
    """类型"""
    title: str
    """标题"""
    url: str
    """链接"""
    date: str
    """日期"""


class EventGengxin(EventModel):
    """
    游戏更新
    """

    action: EventType = EventType.Gengxin
    """事件类型"""
    old_version: str
    """旧版本"""
    new_version: str
    """新版本"""
    package_num: int
    """包数量"""
    package_size: str
    """包大小"""


class EventBagua(EventModel):
    """
    八卦速报
    """

    action: EventType = EventType.Bagua
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


class EventGuanai(EventModel):
    """
    关隘预告
    """

    action: EventType = EventType.Guanai
    """事件类型"""
    server: str
    """服务器"""
    castle: str
    """据点名"""
    start: int
    """首领刷新时间戳"""


class EventYuncong(EventModel):
    """
    云从预告
    """

    action: EventType = EventType.Yuncong
    """事件类型"""
    name: str
    """云从名"""
    site: str
    """位置"""
    desc: str
    """描述"""
    time: int
    """时间戳"""
