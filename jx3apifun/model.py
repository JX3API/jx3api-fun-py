from typing import Optional, Union

from pydantic import BaseModel, Field


class Request(BaseModel):
    """
    发送请求模型
    """

    name: str
    """请求函数名"""
    url: str
    """请求地址"""
    data: dict
    """请求参数"""


class Response(BaseModel):
    """
    返回值模型
    """

    code: int
    """返回码"""
    msg: str
    """返回信息"""
    time: int
    """时间"""
    data: Union[dict, list]
    """返回数据"""


class BaseData(BaseModel):
    """
    基础数据模型
    """

    ...


class BaseListData(BaseData):
    """
    基础列表数据模型
    """

    items: list[BaseData]
    """数据列表"""


class DataActiveCalendar(BaseData):
    """
    日常活动接口返回值模型
    """

    date: str
    """日期"""
    week: str
    """星期"""
    war: str
    """大战"""
    battle: str
    """战场"""
    orecar: str
    """矿车任务"""
    leader: Optional[str] = None
    """世界首领"""
    school: str
    """门派任务"""
    rescue: str
    """驰援任务"""
    draw: Optional[str] = None
    """美人画图"""
    luck: list[str]
    """福源"""
    card: list[str]
    """卡牌"""
    team: list[str]
    """周常"""


class ToDayData(BaseModel):
    """
    当天日期
    """

    date: str
    """日期"""
    week: str
    """星期"""
    year: str
    """年"""
    month: str
    """月"""
    day: str
    """日"""


class DataActiveListCalendar(BaseData):
    """
    日常活动列表接口返回值模型
    """

    today: ToDayData
    """当天日期"""
    data: list[DataActiveCalendar]
    """日常活动列表"""


class DataActiveCelebrity(BaseData):
    """
    当前时间的楚天社/云从社进度
    """

    map_name: str
    """地图名称"""
    event: str
    """事件"""
    site: str
    """地点"""
    desc: str
    """描述"""
    icon: str
    """图标"""
    time: str
    """时间"""


class SimpeExamAnswer(BaseData):
    """
    单个题目答案模型
    """

    id: int
    """题目id"""
    question: str
    """问题"""
    answer: str
    """答案"""
    correctness: int
    """正确性"""
    index: int
    """序号"""
    pinyin: str
    """拼音"""


class DataExamAnswer(BaseListData):
    """
    题目答案列表模型
    """

    items: list[SimpeExamAnswer]
    """题目列表"""


class DataHomeFlower(BaseData):
    """
    家园花卉接口返回值模型
    """

    model_config = {"extra": "allow"}


class DataHomeFurniture(BaseData):
    """
    家园装饰接口返回值模型
    """

    id: int
    """id"""
    name: str
    """装饰名"""
    type: int
    """类型"""
    color: int
    """颜色"""
    source: str
    """来源"""
    architecture: int
    """建筑"""
    limit: int
    """限制"""
    quality: int
    """品质"""
    view: int
    """视角"""
    practical: int
    """实用"""
    hard: int
    """硬度"""
    geomantic: int
    """风水"""
    interesting: int
    """趣味"""
    produce: Optional[str] = None
    """产出"""
    image: str
    """图片"""
    tip: str
    """提示"""


class DataHomeTravel(BaseListData):
    """
    器物谱接口返回值模型
    """

    items: list[DataHomeFurniture]
    """器物列表"""


class OneDataAllNews(BaseModel):
    """
    单个新闻模型
    """

    id: int
    """id"""
    value: int
    """值"""
    type: str
    """类型"""
    title: str
    """标题"""
    date: str
    """日期"""
    url: str
    """链接"""


class DataAllNews(BaseListData):
    """
    所有新闻模型
    """

    items: list[OneDataAllNews]
    """新闻列表"""


class OneDataSchoolToxic(BaseModel):
    """
    单个小药模型
    """

    id: int
    """id"""
    type: str = Field(alias="class")
    """类型"""
    name: str
    """名称"""
    toxic: str
    """小药名"""
    attribute: str
    """属性"""
    status: int
    """状态"""
    datetime: str
    """时间"""


class DataSchoolToxic(BaseListData):
    """
    所有小药模型
    """

    items: list[OneDataSchoolToxic]
    """小药列表"""


class DataServerMaster(BaseData):
    """
    主服信息
    """

    id: str
    """id"""
    zone: str
    """区服"""
    type: str
    """类型"""
    name: str
    """名称"""
    column: str
    """列"""
    center: str
    """中心"""
    duowan: dict
    """多玩"""
    abbreviation: list[str]
    """别名"""
    subordinate: list[str]
    """下属"""


class DataServerCheck(BaseData):
    """
    服务器检查
    """

    id: int
    """id"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    status: int
    """状态"""
    time: int
    """时间"""


class DataServerStatus(BaseData):
    """
    服务器状态
    """

    zone: str
    """区服"""
    server: str
    """服务器"""
    status: str
    """状态"""
