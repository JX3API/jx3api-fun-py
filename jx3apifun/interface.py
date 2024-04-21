from typing import Literal

from .model import (
    DataActiveCalendar,
    DataActiveCelebrity,
    DataActiveListCalendar,
    DataActiveMonster,
    DataAllNews,
    DataChatMixed,
    DataDetailed,
    DataDuowanStatistical,
    DataExamAnswer,
    DataFraudDetail,
    DataHomeFlower,
    DataHomeTravel,
    DataHorseEvent,
    DataHorseRecord,
    DataIdiomSolitaire,
    DataLuckAdventure,
    DataLuckCollect,
    DataLuckStatistical,
    DataMatchAwesome,
    DataMatchRecent,
    DataMatchSchools,
    DataMember,
    DataMemberRecruit,
    DataMusicKugou,
    DataMusicNetease,
    DataMusicTencent,
    DataRankStatistical,
    DataRoleAchievement,
    DataRoleAttribute,
    DataRoleMonster,
    DataRoleTeamCdList,
    DataSaohua,
    DataSchoolForce,
    DataSchoolMatrix,
    DataSchoolRankStatistical,
    DataSchoolSkills,
    DataSchoolToxic,
    DataServerAntivice,
    DataServerCheck,
    DataServerEvent,
    DataServerMaster,
    DataServerSand,
    DataServerStatus,
    DataSoundConverter,
    DataTieBaItemRecords,
    DataTiebaRandom,
    DataTradeDemon,
    DataTradeRecord,
    DataValuablesCollect,
    DataValuablesStatistical,
    DataWatchCollect,
    DataWatchRecord,
    DataWatchStatistical,
)
from .permission import require_ticket, require_token


class ApiInterface:
    """
    Api的调用接口
    """

    def data_active_calendar(
        self, server: str = "长安城", num: int = 0
    ) -> DataActiveCalendar:
        """
        说明:
            今天、明天、后天、日常任务。

        参数:
            * `server`: 可选的，区服名称，查找该区服的记录
            * `num`: 可选的，预测时间，预测指定时间的日常，默认值 : 0 为当天，1 为明天，以此类推

        注意:
            * 只有 星期三、星期五、星期六、星期日 才有美人画图，星期三、星期五 才有世界首领，若非活动时间不返回相关键与值。
        """
        ...

    def data_active_list_calendar(self, num: int = 15) -> DataActiveListCalendar:
        """
        说明:
            预测每天的日常任务

        参数:
            * `num`: 可选的， 预测时间，预测指定时间范围内的活动，默认值 : 15 为当天，1 为明天

        注意:
            * 只有 星期三、星期五、星期六、星期日 才有美人画图，星期三、星期五 才有世界首领，若非活动时间不返回相关键与值。
        """
        ...

    def data_active_celebrity(self, season: int = 2) -> list[DataActiveCelebrity]:
        """
        说明:
            当前时间的楚天社/云从社进度。

        参数:
            * `season`: 可选的，第几赛季，用于返回楚天社或云从社的判断条件，可选值：1-3
        """
        ...

    def data_exam_answer(self, match: str, limit: int = 10) -> list[DataExamAnswer]:
        """
        说明:
            科举答案

        参数:
            * `match`: 必须的，科举试题，支持首字母，支持模糊查询
            * `limit`: 可选的，设置返回的数量，默认值 10
        """
        ...

    def data_home_flower(
        self, server: str, name: str = "绣球花", map: str = "九寨沟·镜海"
    ) -> DataHomeFlower:
        """
        说明:
            家园鲜花最高价格线路

        参数:
            * `server`: 必须的，区服名称
            * `name`: 可选的，花名，默认值 : 绣球花
            * `map`: 可选的，地图名称，默认值 : 九寨沟·镜海
        """
        ...

    def data_home_furniture(self, name: str) -> DataHomeTravel:
        """
        说明:
            装饰详情

        参数:
            * `name`: 必须的，装饰名称
        """
        ...

    def data_home_travel(self, name: str) -> list[DataHomeTravel]:
        """
        说明:
            器物谱地图产出装饰

        参数:
            * `name`: 必须的，地图名称，查找该地图的家具
        """
        ...

    def data_news_allnews(self, limit: int = 10) -> list[DataAllNews]:
        """
        说明:
            官方最新公告及新闻

        参数:
            * `limit`: 可选的，设置返回的数量，默认值 10
        """
        ...

    def data_news_announce(self, limit: int = 10) -> list[DataAllNews]:
        """
        说明:
            官方最新维护公告

        参数:
            * `limit`: 可选的，单页数量，设置返回的数量，默认值 10
        """
        ...

    def data_school_toxic(self, name: str) -> list[DataSchoolToxic]:
        """
        说明:
            推荐的小药清单

        参数:
            * `name`: 必须的，心法名称
        """
        ...

    def data_server_master(self, name: str) -> DataServerMaster:
        """
        说明:
            简称搜索主次服务器

        参数:
            * `name`: 必须的，区服名称
        """
        ...

    def data_server_check(self, server: str = "长安城") -> DataServerCheck:
        """
        说明:
            服务器当前状态 [ 已开服/维护中 ]

        参数:
            * `server`: 可选的，区服名称，查找该区服的记录

        注意:
            * 未输入区服名称或输入错误区服名称时，将返回全部区服的状态数据，可用于开服监控(支持轮询请求)。
            * 服务器状态为 1 时为已开服，为 0 时为维护中。刷新频率30 秒。
        """
        ...

    def data_server_status(self, server: str) -> DataServerStatus:
        """
        说明:
            服务器当前状态 [ 维护/正常/繁忙/爆满 ]

        参数:
            * `server`: 必须的，区服名称
        """
        ...

    @require_token
    @require_ticket
    def data_save_detailed(self, server: str, roleid: str) -> DataDetailed:
        """
        说明:
            自动更新角色信息。

        参数:
            * `server`: 必须的，区服名称
            * `roleid`: 必须的，角色ID

        注意:
            * 该接口需要使用 token 和 ticket。
        """
        ...

    @require_token
    def data_role_detailed(self, server: str, name: str) -> DataDetailed:
        """
        说明:
            角色详细信息

        参数:
            * `server`: 必须的，区服名称
            * `name`: 必须的，角色名称

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_school_matrix(self, name: str) -> DataSchoolMatrix:
        """
        说明:
            职业阵眼效果

        参数:
            * `name`: 必须的，心法名称

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_school_force(self, name: str) -> list[DataSchoolForce]:
        """
        说明:
            奇穴详细效果

        参数:
            * `name`: 必须的，心法名称

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_school_skills(self, name: str) -> list[DataSchoolSkills]:
        """
        说明:
            技能详细效果

        参数:
            * `name`: 必须的，心法名称

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_tieba_random(
        self,
        subclass: Literal[
            "818",
            "616",
            "鬼网三",
            "鬼网3",
            "树洞",
            "记录",
            "教程",
            "街拍",
            "故事",
            "避雷",
            "吐槽",
            "提问",
        ],
        server: str = "-",
        limit: int = 1,
    ) -> list[DataTiebaRandom]:
        """
        说明:
            禁止轮询，随机搜索贴吧 : 818/616....

        参数:
            * `subclass`: 必须的，子类别
            * `server`: 可选的，区服名称，查找该区服的记录
            * `limit`: 可选的，设置返回的数量，默认值 1

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    @require_ticket
    def data_role_attribute(self, server: str, name: str) -> DataRoleAttribute:
        """
        说明:
            角色装备属性详情

        参数:
            * `server`: 必须的，区服名称
            * `name`: 必须的，角色名称

        注意:
            * 该接口需要使用 token 和 ticket。
        """
        ...

    @require_token
    @require_ticket
    def data_role_teamCdList(self, server: str, name: str) -> DataRoleTeamCdList:
        """
        说明:
            角色副本记录

        参数:
            * `server`: 必须的，区服名称
            * `name`: 必须的，角色名称

        注意:
            * 该接口需要使用 token 和 ticket。
        """
        ...

    @require_token
    @require_ticket
    def data_luck_adventure(self, server: str, name: str) -> list[DataLuckAdventure]:
        """
        说明:
            角色奇遇触发记录(不保证遗漏)

        参数:
            * `server`: 必须的，区服名称
            * `name`: 必须的，奇遇名称，查找该奇遇的全服统计

        注意:
            * 该接口需要使用 token 和 ticket。
        """
        ...

    @require_token
    def data_luck_statistical(
        self, server: str, name: str
    ) -> list[DataLuckStatistical]:
        """
        说明:
            奇遇近期触发统计

        参数:
            * `server`: 必须的，区服名称
            * `name`: 必须的，奇遇名称，查找该奇遇的全服统计

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_luck_server_statistical(
        self, name: str, limit: int = 20
    ) -> list[DataLuckStatistical]:
        """
        说明:
            统计全服近期奇遇记录，不区分区服。

        参数:
            * `name`: 必须的，奇遇名称，查找该奇遇的全服统计
            * `limit`: 可选的，设置返回的数量，默认值 20

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_luck_collect(self, server: str, num: int = 7) -> list[DataLuckCollect]:
        """
        说明:
            统计奇遇近期触发角色记录

        参数:
            * `server`: 必须的，区服名称
            * `num`: 可选的，设置返回的数量，默认值 7

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    @require_ticket
    def data_role_achievement(
        self, server: str, role: str, name: str
    ) -> DataRoleAchievement:
        """
        说明:
            角色成就进度

        参数:
            * `server`: 必须的，区服名称
            * `role`: 必须的，角色名称
            * `name`: 必须的，成就名称

        注意:
            * 该接口需要使用 token 和 ticket。
        """
        ...

    @require_token
    @require_ticket
    def data_match_recent(
        self, server: str, name: str, mode: Literal[22, 33, 55] = 33
    ) -> DataMatchRecent:
        """
        说明:
            角色近期战绩记录

        参数:
            * `server`: 必须的，区服名称
            * `name`: 必须的，角色名称
            * `mode`: 可选的，比赛模式，查找该模式的记录，默认值 : 33

        注意:
            * 该接口需要使用 token 和 ticket。
        """
        ...

    @require_token
    @require_ticket
    def data_match_awesome(
        self, mode: Literal[22, 33, 55] = 33, limit: int = 20
    ) -> list[DataMatchAwesome]:
        """
        说明:
            战绩门派排行数据

        参数:
            * `mode`: 可选的，比赛模式，查找该模式的记录，默认值 : 33
            * `limit`: 可选的，单页数量，设置返回的数量，默认值 : 20

        注意:
            * 该接口需要使用 token 和 ticket。
        """
        ...

    @require_token
    @require_ticket
    def data_match_schools(
        self, mode: Literal[22, 33, 55] = 33
    ) -> list[DataMatchSchools]:
        """
        说明:
            比赛统计门派数据

        参数:
            * `mode`: 可选的，比赛模式，查找该模式的记录，默认值 : 33

        注意:
            * 该接口需要使用 token 和 ticket。
        """
        ...

    @require_token
    def data_member_recruit(
        self, server: str, keyword: str = "", table: int = 1
    ) -> DataMemberRecruit:
        """
        说明:
            团队招募信息

        参数:
            * `server`: 必须的，区服名称
            * `keyword`: 可选的，关键字，模糊匹配记录，用=关键字完全匹配记录；
            * `table`: 可选的，指定表记录，1=本服+跨服，2=本服，3=跨服，默认值：1

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_member_teacher(self, server: str, keyword: str = "") -> DataMember:
        """
        说明:
            客户端师徒系统，师傅招募信息

        参数:
            * `server`: 必须的，区服名称
            * `keyword`: 可选的，关键字，查找该关键字的记录；

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_member_student(self, server: str, keyword: str = "") -> DataMember:
        """
        说明:
            客户端师徒系统，徒弟招募信息

        参数:
            * `server`: 必须的，区服名称
            * `keyword`: 可选的，关键字，查找该关键字的记录；

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_server_sand(self, server: str) -> DataServerSand:
        """
        说明:
            沙盘数据

        参数:
            * `server`: 必须的，区服名称

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_server_event(
        self, name: Literal["恶人谷", "浩气盟"] = "恶人谷", limit: int = 100
    ) -> list[DataServerEvent]:
        """
        说明:
            全服阵营大事件

        参数:
            * `name`: 必须的，阵营名称，查找该阵营的记录；
            * `limit`: 可选的，单页数量，设置返回数量，默认值 : 100；

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_trade_demon(
        self, server: str = "", limit: int = 10
    ) -> list[DataTradeDemon]:
        """
        说明:
            金价比例信息

        参数:
            * `server`: 可选的，区服名称
            * `limit`: 可选的，单页数量，设置返回的数量，默认值 : 10。

        注意:
            * 该接口需要使用 token。
            * 未输入区服名称或输入错误区服名称时，将返回全部区服的金币比例信息。
        """
        ...

    @require_token
    def data_trade_record(self, name: str) -> DataTradeRecord:
        """
        说明:
            黑市物品价格统计

        参数:
            * `name`: 必须的，外观名称，查找该外观的记录；

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_tieba_item_records(
        self, name: str, server: str = "-", limit: int = 1
    ) -> list[DataTieBaItemRecords]:
        """
        说明:
            来自贴吧的外观记录。

        参数:
            * `name`: 必须的，外观名称，查找该外观的记录；
            * `server`: 可选的，区服名称，查找该区服的记录，默认值：- 为全区服；
            * `limit`: 可选的，设置返回的数量，默认值 : 1。

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_valuables_statistical(
        self, server: str, name: str, limit: int = 20
    ) -> list[DataValuablesStatistical]:
        """
        说明:
            统计副本掉落的贵重物品。

        参数:
            * `server`: 必须的，区服名称，查找该区服的记录；
            * `name`: 必须的，物品名称，查找该物品的记录；
            * `limit`: 可选的，单页数量，设置返回的数量，默认值：20；

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_valuables_server_statistical(
        self, name: str, limit: int = 30
    ) -> list[DataValuablesStatistical]:
        """
        说明:
            统计当前赛季副本掉落的特殊物品。

        参数:
            * `name`: 必须的，物品名称，查找该物品的记录；
            * `limit`: 可选的，单页数量，设置返回的数量，默认值：30；

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_valuables_collect(
        self, server: str, num: int = 7
    ) -> list[DataValuablesCollect]:
        """
        说明:
            副本掉落的特殊物品汇总

        参数:
            * `server`: 必须的，区服名称，查找该区服的记录；
            * `num`: 可选的，设置返回的数量，默认值 7

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_server_antivice(self) -> list[DataServerAntivice]:
        """
        说明:
            诛恶事件历史记录(不允许轮询)

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_rank_statistical(
        self, server: str, table: str, name: str
    ) -> list[DataRankStatistical]:
        """
        说明:
            客户端战功榜与风云录

        参数:
            * `server`: 必须的，区服名称，查找该区服的记录；
            * `table`: 必须的，榜单类型
            * `name`: 必须的，榜单名称

        `table` 与 `name` 的关联:
            * `table` : 个人，`name` : 名士五十强 老江湖五十强 兵甲藏家五十强 名师五十强 阵营英雄五十强 薪火相传五十强 庐园广记一百强
            * `table` : 帮会，`name` : 浩气神兵宝甲五十强 恶人神兵宝甲五十强 浩气爱心帮会五十强 恶人爱心帮会五十强
            * `table` : 阵营，`name` : 赛季恶人五十强 赛季浩气五十强 上周恶人五十强 上周浩气五十强 本周恶人五十强 本周浩气五十强
            * `table` : 试炼，`name` : 万花 七秀 少林 纯阳 天策 五毒 唐门 明教 苍云 长歌 藏剑 丐帮 霸刀 蓬莱 凌雪 衍天 药宗 刀宗

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_rank_server_statistical(
        self, table: str, name: str
    ) -> list[DataRankStatistical]:
        """
        说明:
            客户端战功榜与风云录，查看全服

        参数:
            * `table`: 必须的，榜单类型
            * `name`: 必须的，榜单名称

        `table` 与 `name` 的关联:
            * `table` : 个人，`name` : 名士五十强 老江湖五十强 兵甲藏家五十强 名师五十强 阵营英雄五十强 薪火相传五十强 庐园广记一百强
            * `table` : 帮会，`name` : 浩气神兵宝甲五十强 恶人神兵宝甲五十强 浩气爱心帮会五十强 恶人爱心帮会五十强
            * `table` : 阵营，`name` : 赛季恶人五十强 赛季浩气五十强 上周恶人五十强 上周浩气五十强 本周恶人五十强 本周浩气五十强
            * `table` : 试炼，`name` : 万花 七秀 少林 纯阳 天策 五毒 唐门 明教 苍云 长歌 藏剑 丐帮 霸刀 蓬莱 凌雪 衍天 药宗 刀宗

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    @require_ticket
    def data_school_rank_statistical(
        self, school: str = "ALL", server: str = "ALL"
    ) -> list[DataSchoolRankStatistical]:
        """
        说明:
            游戏资历榜单

        参数:
            * `school`: 可选的，门派简称，查找该心法的记录，默认值 : ALL；
            * `server`: 可选的，区服名称，查找该区服的记录，默认值 : ALL；

        注意:
            * 该接口需要使用 token 和 ticket。
        """
        ...

    @require_token
    def data_duowan_statistical(
        self, server: str = "ALL"
    ) -> list[DataDuowanStatistical]:
        """
        说明:
            服务器的统战歪歪。

        参数:
            * `server`: 可选的，区服名称，查找该区服的记录，默认值 : ALL；

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_active_monster(self) -> DataActiveMonster:
        """
        说明:
            本周百战异闻录刷新的首领以及特殊效果。

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_horse_records(self, server: str = "") -> list[DataHorseRecord]:
        """
        说明:
            客户端的卢刷新记录。

        参数:
            * `server`: 可选的，区服名称，查找该区服的记录；

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_horse_event(self, server: str) -> DataHorseEvent:
        """
        说明:
            客户端马场刷新记录。

        参数:
            * `server`: 必须的，区服名称，查找该区服的记录；

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_watch_record(self, server: str, name: str) -> list[DataWatchRecord]:
        """
        说明:
            烟花赠送与接收的历史记录，不保证遗漏。

        参数:
            * `server`: 必须的，区服名称
            * `name`: 必须的，角色名称

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_watch_statistical(
        self, server: str, name: str, limit: int = 20
    ) -> list[DataWatchStatistical]:
        """
        说明:
            统计烟花记录。

        参数:
            * `server`: 必须的，区服名称
            * `name`: 必须的，角色名称
            * `limit`: 可选的，设置返回的数量，默认值 20

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_watch_collect(self, server: str, num: int = 7) -> list[DataWatchCollect]:
        """
        说明:
            汇总烟花记录。

        参数:
            * `server`: 必须的，区服名称
            * `num`: 可选的，设置返回的数量，默认值 7

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_watch_rank_statistical(
        self,
        server: str,
        column: Literal["sender", "recipient", "name"],
        this_time: int,
        that_time: int,
    ) -> list[DataWatchCollect]:
        """
        说明:
            烟花排行榜

        参数:
            * `server`: 必须的，区服名称，查找该区服的记录
            * `column`: 必须的，可选范围：[sender recipient name]
            * `this_time`: 必须的，统计开始的时间，与结束的时间不得超过3个月
            * `that_time`: 必须的，统计结束的时间，与开始的时间不得超过3个月

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_chat_mixed(self, name: str, text: str) -> DataChatMixed:
        """
        说明:
            智障聊天

        参数:
            * `name`: 必须的，机器人的名称；
            * `text`: 必须的，聊天的完整内容；

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_music_tencent(self, name: str) -> list[DataMusicTencent]:
        """
        说明:
            搜索腾讯音乐歌曲编号。

        参数:
            * `name`: 必须的，歌曲名称；

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_music_netease(self, name: str) -> list[DataMusicNetease]:
        """
        说明:
            搜索网易云音乐歌曲编号。

        参数:
            * `name`: 必须的，歌曲名称；

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_music_kugou(self, name: str) -> list[DataMusicKugou]:
        """
        说明:
            搜索酷狗音乐歌曲编号。

        参数:
            * `name`: 必须的，歌曲名称；

        注意:
            * 该接口需要使用 token。
        """
        ...

    @require_token
    def data_fraud_detail(self, uin: int) -> DataFraudDetail:
        """
        说明:
            搜索贴吧的行骗记录

        参数:
            * `uin`: 必须的，用户QQ号，查找是否存在行骗记录；

        注意:
            * 该接口需要使用 token。
        """
        ...

    def data_idiom_solitaire(self, name: str) -> DataIdiomSolitaire:
        """
        说明:
            校对成语并返回相关成语

        参数:
            * `name`: 必须的，查找对应词语。
        """
        ...

    def data_saohua_random(self) -> DataSaohua:
        """
        说明:
            门派骚话
        """
        ...

    def data_saohua_content(self) -> DataSaohua:
        """
        说明:
            召唤一条舔狗日记。
        """
        ...

    def data_sound_converter(
        self,
        appkey: str,
        access: str,
        secret: str,
        text: str,
        voice: str = "Aitong",
        format: str = "mp3",
        sample_rate: int = 16000,
        volume: int = 50,
        speech_rate: int = 0,
        pitch_rate: int = 0,
    ) -> DataSoundConverter:
        """
        说明:
            阿里云语音合成（TTS）

        参数:
            * `appkey`: 必须的，阿里云appkey
            * `access`: 必须的，阿里云access
            * `secret`: 必须的，阿里云secret
            * `text`: 必须的，合成文本
            * `voice`: 可选的，发音人，默认值 [Aitong]
            * `format`: 可选的，编码格式，范围 [PCM][WAV][MP3]，默认值 [MP3]
            * `sample_rate`: 可选的，采样率，默认值 [16000]
            * `volume`: 可选的，音量，范围 [0～100]，默认值 [50]
            * `speech_rate`: 可选的，语速，范围 [-500～500]，默认值 [0]
            * `pitch_rate`: 可选的，音调，范围 [-500～500]，默认值[0]
        """
        ...

    @require_token
    def data_role_monster(self, server: str, name: str) -> DataRoleMonster:
        """
        说明:
            查看个人百战信息。

        参数:
            * `server`: 必须的，区服名称
            * `name`: 必须的，角色名称

        注意:
            * 该接口需要使用 token。
        """
        ...
