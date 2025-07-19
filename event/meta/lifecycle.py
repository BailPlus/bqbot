#bqbot:event.meta.lifecycle 生命周期事件

from dataclasses import dataclass
from typing import override
from enum import Enum
from . import MetaEventType, MetaEvent
from .. import EventType


class ConnectionStatus(Enum):
    """连接状态
ENABLE和DISABLE仅在http POST中有效，CONNECT仅在ws中有效"""
    ENABLE = "enable"   # 启动实现端
    DISABLE = "disable" # 停止实现端
    CONNECT = "connect" # 连接成功


@dataclass(frozen=True, kw_only=True)
class Lifecycle(MetaEvent):
    """心跳事件"""
    meta_event_type: MetaEventType = MetaEventType.LIFECYCLE
    sub_type: ConnectionStatus

    @override
    @classmethod
    def _is_suitable(cls, data: dict) -> bool:
        return super()._is_suitable(data) and data.get("meta_event_type") == cls.meta_event_type.value

    @override
    @classmethod
    def _from_dict(cls, data: dict):
        return cls(
            raw_data=data,
            self_id=data['self_id'],
            time=data['time'],
            sub_type=ConnectionStatus(data.get('sub_type'))
        )
