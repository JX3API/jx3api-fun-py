from pathlib import Path

from msgspec import Struct, json


class Config(Struct):
    api_token: str
    api_ticket: str
    ws_token: str


def load_config(file_path: str) -> Config:
    file = Path(file_path)
    if not file.exists():
        raise FileNotFoundError(f"config file not found: {file_path}")
    with open(file, "r", encoding="utf-8") as f:
        config_str = f.read()
    return json.decode(config_str, type=Config)
