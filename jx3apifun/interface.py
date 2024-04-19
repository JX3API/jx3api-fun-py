from .model import DataActiveCurrentRes
from .permission import require_ticket, require_token


class ApiInterface:
    """
    Api的调用接口
    """

    @require_ticket
    @require_token
    def data_active_current(self, server="长安城", num=0) -> DataActiveCurrentRes:
        """
        日常活动接口
        """
        ...
