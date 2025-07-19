#bqbot:config 配置模块

from dataclasses import dataclass
from .connection import Connection

@dataclass(frozen=True)
class Config:
    connection: Connection
