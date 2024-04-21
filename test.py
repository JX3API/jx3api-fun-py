from test.api_test import sync_test
from test.config import load_config

from jx3apifun import set_ticket, set_token, set_ws_token

if __name__ == "__main__":
    config = load_config("config.json")
    set_ticket(config.api_ticket)
    set_token(config.api_token)
    set_ws_token(config.ws_token)
    sync_test()
