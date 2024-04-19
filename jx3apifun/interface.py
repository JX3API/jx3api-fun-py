from typing import Literal

from .model import (
    DataActiveCalendar,
    DataActiveCelebrity,
    DataActiveListCalendar,
    DataAllNews,
    DataDetailed,
    DataEquip,
    DataExamAnswer,
    DataHomeFlower,
    DataHomeFurniture,
    DataHomeTravel,
    DataLuckAdventure,
    DataLuckCollect,
    DataLuckStatistical,
    DataRoleAchievement,
    DataRoleTeamCdList,
    DataSchoolForce,
    DataSchoolMatrix,
    DataSchoolSkills,
    DataSchoolToxic,
    DataServerCheck,
    DataServerMaster,
    DataServerStatus,
    DataTiebaRandom,
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

    def data_active_celebrity(self, season: int = 2) -> DataActiveCelebrity:
        """
        说明:
            当前时间的楚天社/云从社进度。

        参数:
            * `season`: 可选的，第几赛季，用于返回楚天社或云从社的判断条件，可选值：1-3
        """
        ...

    def data_exam_answer(self, match: str, limit: int = 10) -> DataExamAnswer:
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

    def data_home_furniture(self, name: str) -> DataHomeFurniture:
        """
        说明:
            装饰详情

        参数:
            * `name`: 必须的，装饰名称
        """
        ...

    def data_home_travel(self, name: str) -> DataHomeTravel:
        """
        说明:
            器物谱地图产出装饰

        参数:
            * `name`: 必须的，地图名称，查找该地图的家具
        """
        ...

    def data_news_allnews(self, limit: int = 10) -> DataAllNews:
        """
        说明:
            官方最新公告及新闻

        参数:
            * `limit`: 可选的，设置返回的数量，默认值 10
        """
        ...

    def data_news_announce(self, limit: int = 10) -> DataAllNews:
        """
        说明:
            官方最新维护公告

        参数:
            * `limit`: 可选的，单页数量，设置返回的数量，默认值 10
        """
        ...

    def data_school_toxic(self, name: str) -> DataSchoolToxic:
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
    def data_school_force(self, name: str) -> DataSchoolForce:
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
    def data_school_skills(self, name: str) -> DataSchoolSkills:
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
    ) -> DataTiebaRandom:
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
    def data_role_attribute(self, server: str, name: str) -> DataEquip:
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
    def data_luck_adventure(self, server: str, name: str) -> DataLuckAdventure:
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
    def data_luck_statistical(self, server: str, name: str) -> DataLuckStatistical:
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
    ) -> DataLuckStatistical:
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
    def data_luck_collect(self, server: str, num: int = 7) -> DataLuckCollect:
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
    def data_match_recent(self, name: str, mode: Literal[22, 33, 55] = 33):
        """
        说明:
            角色近期战绩记录

        参数:
            * `name`: 必须的，角色名称
            * `mode`: 可选的，模式选择，默认值 33

        注意:
            * 该接口需要使用 token 和 ticket。
        """
        ...
