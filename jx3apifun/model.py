from typing import Optional, Union

from pydantic import BaseModel


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


class DataActiveCurrentRes(BaseData):
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


class SimpeExamAnswerRes(BaseData):
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


class DataExamAnswerRes(BaseListData):
    """
    题目答案列表模型
    """

    items: list[SimpeExamAnswerRes]
    """题目列表"""
