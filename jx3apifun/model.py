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


class DataDetailed(BaseData):
    """
    更新角色信息
    """

    zoneName: str
    """区服名称"""
    serverName: str
    """服务器名称"""
    roleName: str
    """角色名称"""
    roleId: str
    """角色id"""
    globalRoleId: str
    """全局角色id"""
    forceName: str
    """门派名称"""
    forceId: str
    """门派id"""
    bodyName: str
    """体型名称"""
    bodyId: str
    """体型id"""
    tongName: Optional[str] = None
    """帮派名称"""
    tongId: Optional[str] = None
    """帮派id"""
    campName: str
    """阵营名称"""
    campId: str
    """阵营id"""
    personName: str
    """人物名称"""
    personId: str
    """人物id"""
    personAvatar: str
    """人物头像"""


class OneSchoolMatrixDescs(BaseModel):
    """
    单个职业阵眼描述
    """

    desc: str
    """描述"""
    level: int
    """等级"""
    name: str
    """名称"""


class DataSchoolMatrix(BaseData):
    """
    职业阵眼效果
    """

    name: str
    """名称"""
    skillName: str
    """阵法名称"""
    descs: list[OneSchoolMatrixDescs]
    """描述列表"""


class OneDataSchoolForceData(BaseModel):
    """
    单个奇穴数据
    """

    name: str
    """名称"""
    type: int = Field(alias="class")
    """分类"""
    desc: str
    """描述"""
    icon: str
    """图标"""
    kind: str
    """类型"""
    subKind: str
    """子类型"""


class OneDataSchoolForce(BaseModel):
    """
    单个门派奇穴
    """

    level: int
    """等级"""
    data: list[OneDataSchoolForceData]
    """数据"""


class DataSchoolForce(BaseListData):
    """
    门派奇穴
    """

    items: list[OneDataSchoolForce]
    """奇穴列表"""


class OneDataSchoolSkills(BaseModel):
    """
    单个门派技能
    """

    name: str
    """名称"""
    simpleDesc: str
    """简单描述"""
    desc: str
    """描述"""
    specialDesc: str
    """特殊描述"""
    interval: str
    """间隔"""
    consumption: str
    """消耗"""
    distance: str
    """距离"""
    icon: str
    """图标"""
    kind: str
    """类型"""
    subKind: str
    """子类型"""
    releaseType: str
    """释放类型"""
    weapon: str
    """武器"""


class DataSchoolSkills(BaseListData):
    """
    门派技能
    """

    items: list[OneDataSchoolSkills]
    """技能列表"""


class OneDataTiebaRandom(BaseModel):
    """
    贴吧帖子
    """

    id: int
    """id"""
    subclass: str
    """子类别"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    name: str
    """名称"""
    title: str
    """标题"""
    url: int
    """链接"""
    date: str
    """日期"""


class DataTiebaRandom(BaseListData):
    """
    贴吧帖子列表
    """

    items: list[OneDataTiebaRandom]
    """帖子列表"""


class OneFiveStone(BaseModel):
    """
    五行石数据
    """

    name: str
    """名称"""
    level: str
    """等级"""
    max: str
    """最大值"""
    min: str
    """最小值"""
    icon: str
    """图标"""
    kind: str
    """类型"""
    subKind: str
    """子类型"""
    desc: str
    """描述"""
    percent: bool
    """百分比"""


class OneColorStoneAttr(BaseModel):
    """
    五彩石属性
    """

    max: str
    """最大值"""
    min: str
    """最小值"""
    desc: str
    """描述"""
    percent: bool
    """百分比"""


class ColorStone(BaseModel):
    """
    五彩石数据
    """

    id: str
    """id"""
    name: str
    """名称"""
    type: str = Field(alias="class")
    """分类"""
    level: str
    """等级"""
    icon: str
    """图标"""
    kind: str
    """类型"""
    subKind: str
    """子类型"""
    attribute: list[OneColorStoneAttr]
    """属性"""


class OneModifyType(BaseModel):
    """
    属性类型
    """

    name: str
    """名称"""
    max: str
    """最大值"""
    min: str
    """最小值"""
    desc: str
    """描述"""
    percent: bool
    """百分比"""


class OnePerManentEnchantAttri(BaseModel):
    """
    附魔属性
    """

    desc: str
    """描述"""


class OnePerManentEnchant(BaseModel):
    """
    附魔数据
    """

    id: str
    """id"""
    name: str
    """名称"""
    level: str
    """等级"""
    icon: str
    """图标"""
    attrib: list[OnePerManentEnchantAttri]
    """属性"""


class BaseTypeAttri(BaseModel):
    """
    基础属性
    """

    GeneratedBase: str
    """基础属性"""
    GeneratedMagic: str
    """魔法属性"""
    HorseBase: str
    """坐骑属性"""
    HorseMagic: str
    """坐骑魔法属性"""
    Type: str
    """类型"""
    percent: bool
    """百分比"""


class Base1Type(BaseModel):
    """
    基础属性
    """

    Attrib: BaseTypeAttri
    """属性"""
    Base1Max: str
    """最大值"""
    Base1Min: str
    """最小值"""
    Desc: str
    """描述"""


class Base2Type(BaseModel):
    """
    基础属性
    """

    Attrib: BaseTypeAttri
    """属性"""
    Base2Max: str
    """最大值"""
    Base2Min: str
    """最小值"""
    Desc: str
    """描述"""


class OneEquip(BaseModel):
    """
    装备数据
    """

    name: str
    """名称"""
    type: str = Field(alias="class")
    """分类"""
    icon: str
    """图标"""
    kind: str
    """类型"""
    subKind: str
    """子类型"""
    quality: str
    """品质"""
    strengthLevel: str
    """强化等级"""
    maxStrengthLevel: str
    """最大强化等级"""
    color: str
    """颜色"""
    desc: str
    """描述"""
    source: Optional[str] = None
    """来源"""
    fiveStone: list[OneFiveStone]
    """五行石"""
    colorStone: ColorStone
    """五彩石"""
    modifyType: list[OneModifyType]
    """属性"""
    permanentEnchant: list[OnePerManentEnchant]
    """附魔"""
    Base1Type: Base1Type
    """基础属性1"""
    Base2Type: Base2Type
    """基础属性2"""


class DataEquip(BaseListData):
    """
    装备数据
    """

    items: list[OneEquip]
    """装备列表"""


class BossProgress(BaseModel):
    """
    Boss进度
    """

    finished: bool
    """是否完成"""
    icon: str
    """图标"""
    index: str
    """序号"""
    name: str
    """名称"""
    progressId: str
    """进度id"""


class OneTeamMapData(BaseModel):
    """
    单个副本数据
    """

    mapIcon: str
    """地图图标"""
    mapId: str
    """地图id"""
    mapName: str
    """地图名称"""
    mapType: str
    """地图类型"""
    bossCount: int
    """Boss数量"""
    bossFinished: int
    """Boss完成数量"""
    bossProgress: list[BossProgress]
    """Boss进度"""


class DataRoleTeamCdList(DataDetailed):
    """
    角色副本CD列表
    """

    data: list[OneTeamMapData]
    """副本数据"""


class DataLuckAdventure(BaseData):
    """
    角色奇遇触发记录(不保证遗漏)
    """

    zone: str
    """区服"""
    server: str
    """服务器"""
    name: str
    """名称"""
    event: str
    """奇遇名"""
    level: int
    """等级"""
    status: int
    """状态"""
    time: int
    """时间"""


class DataLuckStatistical(BaseListData):
    """
    奇遇近期触发统计
    """

    items: list[DataLuckAdventure]
    """奇遇列表"""


class DataLuckCollectData(BaseModel):
    """
    奇遇汇总数据
    """

    name: str
    """触发人"""
    time: int
    """触发时间"""


class OneDataLuckCollect(BaseModel):
    """
    单个奇遇汇总
    """

    server: str
    """服务器"""
    event: str
    """奇遇名"""
    count: int
    """数量"""
    data: DataLuckCollectData
    """数据"""


class DataLuckCollect(BaseListData):
    """
    奇遇汇总
    """

    items: list[OneDataLuckCollect]
    """奇遇列表"""


class DataRoleAchievementData(BaseModel):
    """
    角色成就数据
    """

    id: int
    """id"""
    icon: str
    """图标"""
    likes: int
    """点赞数"""
    name: str
    """奇遇名称"""
    upClass: str = Field(alias="class")
    """类型"""
    subClass: str
    """子类型"""
    desc: str
    """描述"""
    detail: str
    """详情"""
    maps: list
    """地图"""
    isFinished: bool
    """是否完成"""
    isFav: bool
    """是否收藏"""
    type: str
    """类型"""
    currentValue: int
    """当前值"""
    triggerValue: int
    """触发值"""
    subset: list
    """子集"""
    rewardItem: Optional[str] = None
    """奖励物品"""
    rewardPoint: int
    """奖励点数"""
    rewardPrefix: str
    """奖励前缀"""
    rewardSuffix: str
    """奖励后缀"""


class DataRoleAchievement(DataDetailed):
    """
    角色成就进度
    """

    data: list[DataRoleAchievementData]
    """成就列表"""


class OneDataMatchPerformance(BaseModel):
    """
    战绩表现
    """

    mmr: int
    """MMR"""
    grade: int
    """评分"""
    ranking: str
    """排名"""
    winCount: int
    """胜场"""
    totalCount: int
    """总场次"""
    mvpCount: int
    """MVP次数"""
    pvpType: str
    """PVP类型"""
    winRate: int
    """胜率"""


class DataMatchPerformance(BaseModel):
    """
    战绩表现
    """

    match22: Optional[OneDataMatchPerformance] = Field(alias="2v2", default=None)
    """2v2表现"""
    match33: Optional[OneDataMatchPerformance] = Field(alias="3v3", default=None)
    """3v3表现"""
    match55: Optional[OneDataMatchPerformance] = Field(alias="5v5", default=None)
    """5v5表现"""


class DataMatchHistory(BaseModel):
    """
    战绩历史
    """

    zone: str
    """区服"""
    server: str
    """服务器"""
    avgGrade: int
    """平均评分"""
    totalMmr: int
    """总MMR"""
    mmr: int
    """MMR"""
    kungfu: str
    """心法"""
    pvpType: int
    """PVP类型"""
    won: bool
    """是否胜利"""
    mvp: bool
    """是否MVP"""
    startTime: int
    """开始时间"""
    endTime: int
    """结束时间"""


class DataMatchTrend(BaseModel):
    """
    战绩走势
    """

    matchDate: int
    """比赛日期"""
    mmr: int
    """MMR"""
    winRate: float
    """胜率"""


class DataMatchRecent(DataDetailed):
    """
    角色近期战绩记录
    """

    performance: DataMatchPerformance
    """战绩表现"""
    history: list[DataMatchHistory]
    """战绩历史"""
    trend: list[DataMatchTrend]
    """战绩走势"""


class DataMatchAwesome(BaseData):
    """
    名剑排行
    """

    zoneName: str
    """区服名称"""
    serverName: str
    """服务器名称"""
    roleName: str
    """角色名称"""
    forceName: str
    """门派名称"""
    avatarUrl: str
    """头像链接"""
    rankNum: str
    """排名"""
    score: str
    """分数"""
    upNum: str
    """上升名次"""
    winRate: str
    """胜率"""


class OneDataMatchSchools(BaseModel):
    """
    名剑统计
    """

    name: str
    """门派名称"""
    this: int
    """当前排名"""
    last: int
    """上次排名"""


class DataMatchSchools(BaseListData):
    """
    比赛统计门派数据
    """

    items: list[OneDataMatchSchools]
    """门派列表"""


class OneDataMemberRecruit(BaseModel):
    """
    团队招募信息
    """

    crossServer: bool
    """是否跨服"""
    activityId: int
    """活动id"""
    activity: str
    """活动名"""
    level: int
    """等级"""
    leader: str
    """团长"""
    pushId: int
    """推送id"""
    roomID: str
    """房间id"""
    roleId: int
    """角色id"""
    createTime: int
    """创建时间"""
    number: int
    """当前人数"""
    maxNumber: int
    """最大人数"""
    label: list[str]
    """标签"""
    content: str
    """内容"""


class DataMemberRecruit(BaseListData):
    """
    团队招募信息
    """

    items: list[OneDataMemberRecruit]
    """招募列表"""


class OneDataMember(BaseModel):
    """
    师父列表数据
    """

    roleId: int
    """角色id"""
    roleName: str
    """角色名"""
    roleLevel: int
    """角色等级"""
    campName: str
    """阵营名"""
    tongName: Optional[str] = None
    """帮派名"""
    tongMasterName: Optional[str] = None
    """帮主名"""
    bodyId: int
    """体型id"""
    bodyName: str
    """体型名"""
    forceId: int
    """门派id"""
    forceName: str
    """门派名"""
    comment: str
    """宣言"""
    time: int
    """时间"""


class DataMember(BaseListData):
    """
    师徒列表数据
    """

    items: list[OneDataMember]
    """师徒列表"""


class OneDataServerSand(BaseModel):
    """
    服务器沙盘数据
    """

    tongId: int
    """帮派id"""
    tongName: str
    """帮派名"""
    castleId: int
    """城池id"""
    castleName: str
    """城池名"""
    masterId: int
    """帮主id"""
    masterName: str
    """帮主名"""
    campId: int
    """阵营id"""
    campName: str
    """阵营名"""


class DataServerSand(BaseData):
    """
    服务器沙盘数据
    """

    zone: str
    """区服"""
    server: str
    """服务器"""
    reset: int
    """重置时间"""
    update: int
    """更新时间"""
    data: list[OneDataServerSand]
    """沙盘数据"""


class OneDataServerEvent(BaseModel):
    """
    全服阵营大事件
    """

    id: int
    """id"""
    camp_name: str
    """阵营名"""
    fenxian_zone_name: str
    """分线区服名"""
    fenxian_server_name: str
    """分线服务器名"""
    friend_zone_name: str
    """友方区服名"""
    friend_server_name: str
    """友方服务器名"""
    role_name: str
    """角色名"""
    add_time: int
    """添加时间"""


class DataServerEvent(BaseListData):
    """
    全服阵营大事件
    """

    items: list[OneDataServerEvent]
    """事件列表"""


class OneDataTradeDemon(BaseModel):
    """
    金价比例数据
    """

    id: int
    """id"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    tieba: str
    """贴吧数据"""
    wanbaolou: str
    """万宝楼数据"""
    dd373: str
    """373数据"""
    uu898: str
    """898数据"""
    from_5173: str = Field(alias="5173")
    """5173数据"""
    from_7881: str = Field(alias="7881")
    """7881数据"""
    time: int
    """时间"""
    date: str
    """日期"""


class DataTradeDemon(BaseListData):
    """
    金价比例数据
    """

    items: list[OneDataTradeDemon]
    """比例列表"""


class OneDataTieBaItemRecords(BaseModel):
    """
    贴吧物品记录
    """

    id: int
    """id"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    name: str
    """名称"""
    url: int
    """帖子链接"""
    context: str
    """内容"""
    reply: int
    """回复数"""
    token: str
    """token"""
    floor: int
    """楼层"""
    time: int
    """时间"""


class DataTieBaItemRecords(BaseListData):
    """
    贴吧物品记录
    """

    items: list[OneDataTieBaItemRecords]
    """记录列表"""


class OneDataValuablesStatistical(BaseModel):
    """
    物品统计
    """

    id: int
    """id"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    name: str
    """名称"""
    role_name: str
    """角色名"""
    map_name: str
    """地图名"""
    time: int
    """时间"""


class DataValuablesStatistical(BaseListData):
    """
    物品统计
    """

    items: list[OneDataValuablesStatistical]
    """统计列表"""


class OneDataValuablesCollect(BaseModel):
    """
    掉落汇总数据
    """

    name: str
    """名称"""
    count: int
    """数量"""
    data: OneDataValuablesStatistical
    """数据"""


class DataValuablesCollect(BaseListData):
    """
    掉落汇总
    """

    items: list[OneDataValuablesCollect]
    """汇总列表"""


class OneDataServerAntivice(BaseModel):
    """
    诛恶事件数据
    """

    id: int
    """id"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    map_name: str
    """地图名"""
    time: int
    """时间"""


class DataServerAntivice(BaseListData):
    """
    诛恶事件数据
    """

    items: list[OneDataServerAntivice]
    """事件列表"""


class OneDataRankStatistical(BaseModel):
    """
    风云榜单数据
    """

    id: int
    """id"""
    type: str = Field(alias="class")
    """类型"""
    zone: str
    """区服"""
    server: str
    """服务器"""
    name: str
    """名称"""
    school: str
    """门派"""
    index: int
    """排名"""
    level: int
    """等级"""
    camp_name: str
    """阵营"""
    tong_name: Optional[str] = None
    """帮派"""
    score: int
    """分数"""
    datetime: str
    """时间"""


class DataRankStatistical(BaseListData):
    """
    风云榜单数据
    """

    items: list[OneDataRankStatistical]
    """榜单列表"""


class OneDataSchoolRankStatistical(BaseModel):
    """
    资历榜单数据
    """

    name: str
    """名称"""
    role: str
    """角色"""
    school: str
    """门派"""
    server: str
    """服务器"""
    zone: str
    """区服"""
    value: int
    """值"""
    avatar: str
    """头像"""


class DataSchoolRankStatistical(BaseListData):
    """
    资历榜单数据
    """

    items: list[OneDataSchoolRankStatistical]
    """榜单列表"""


class OneDataDuowanStatistical(BaseModel):
    """
    单个频道数据
    """

    campName: str
    """阵营名"""
    sid: int
    """sid"""
    logoUrl: str
    """logoUrl"""
    users: int
    """用户数"""
    snick: str
    """snick"""
    limit: int
    """limit"""
    logo: int
    """logo"""
    asid: int
    """asid"""


class DataDuowanStatisticalData(BaseModel):
    server: str
    """服务器"""
    data: list[OneDataDuowanStatistical]
    """数据"""


class DataDuowanStatistical(BaseListData):
    """
    多玩数据
    """

    items: list[DataDuowanStatisticalData]
    """榜单列表"""
