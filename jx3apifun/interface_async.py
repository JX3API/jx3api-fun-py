from .model import (
    DataActiveCalendar,
    DataActiveCelebrity,
    DataActiveListCalendar,
    DataAllNews,
    DataExamAnswer,
    DataHomeFlower,
    DataHomeFurniture,
    DataHomeTravel,
    DataSchoolToxic,
    DataServerCheck,
    DataServerMaster,
    DataServerStatus,
)
from .permission import require_ticket, require_token


class ApiInterfaceAsync:
    """
    Api的调用接口
    """

    async def data_active_calendar(
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

    async def data_active_list_calendar(self, num: int = 15) -> DataActiveListCalendar:
        """
        说明:
            预测每天的日常任务

        参数:
            * `num`: 可选的， 预测时间，预测指定时间范围内的活动，默认值 : 15 为当天，1 为明天

        注意:
            * 只有 星期三、星期五、星期六、星期日 才有美人画图，星期三、星期五 才有世界首领，若非活动时间不返回相关键与值。
        """
        ...

    async def data_active_celebrity(self, season: int = 2) -> DataActiveCelebrity:
        """
        说明:
            当前时间的楚天社/云从社进度。

        参数:
            * `season`: 可选的，第几赛季，用于返回楚天社或云从社的判断条件，可选值：1-3
        """
        ...

    async def data_exam_answer(self, match: str, limit: int = 10) -> DataExamAnswer:
        """
        说明:
            科举答案

        参数:
            * `match`: 必须的，科举试题，支持首字母，支持模糊查询
            * `limit`: 可选的，设置返回的数量，默认值 10
        """
        ...

    async def data_home_flower(
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

    async def data_home_furniture(self, name: str) -> DataHomeFurniture:
        """
        说明:
            装饰详情

        参数:
            * `name`: 必须的，装饰名称
        """
        ...

    async def data_home_travel(self, name: str) -> DataHomeTravel:
        """
        说明:
            器物谱地图产出装饰

        参数:
            * `name`: 必须的，地图名称，查找该地图的家具
        """
        ...

    async def data_news_allnews(self, limit: int = 10) -> DataAllNews:
        """
        说明:
            官方最新公告及新闻

        参数:
            * `limit`: 可选的，设置返回的数量，默认值 10
        """
        ...

    async def data_news_announce(self, limit: int = 10) -> DataAllNews:
        """
        说明:
            官方最新维护公告

        参数:
            * `limit`: 可选的，单页数量，设置返回的数量，默认值 10
        """
        ...

    async def data_school_toxic(self, name: str) -> DataSchoolToxic:
        """
        说明:
            推荐的小药清单

        参数:
            * `name`: 必须的，心法名称
        """
        ...

    async def data_server_master(self, name: str) -> DataServerMaster:
        """
        说明:
            简称搜索主次服务器

        参数:
            * `name`: 必须的，区服名称
        """
        ...

    async def data_server_check(self, server: str = "长安城") -> DataServerCheck:
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

    async def data_server_status(self, server: str) -> DataServerStatus:
        """
        说明:
            服务器当前状态 [ 维护/正常/繁忙/爆满 ]

        参数:
            * `server`: 必须的，区服名称
        """
        ...
