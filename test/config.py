from pathlib import Path

from pydantic import BaseModel


class Config(BaseModel):
    api_token: str
    api_ticket: str
    ws_token: str


def load_config(file_path: str) -> Config:
    file = Path(file_path)
    if not file.exists():
        raise FileNotFoundError(f"config file not found: {file_path}")
    with open(file, "r", encoding="utf-8") as f:
        config_str = f.read()
    return Config.model_validate_json(config_str)
