#bqbot:event.meta.heart_beat 心跳事件

from dataclasses import dataclass
from typing import override
from . import MetaEventType, MetaEvent
from .. import EventType


@dataclass(frozen=True, kw_only=True)
class BotStatus:
    """Bot状态"""
    online: bool
    good: bool


@dataclass(frozen=True, kw_only=True)
class Heartbeat(MetaEvent):
    """心跳事件"""
    type: EventType = EventType.META_EVENT
    meta_event_type: MetaEventType = MetaEventType.HEARTBEAT
    interval: int
    status: BotStatus

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
            interval=data['interval'],
            status=BotStatus(
                online=data['status']['online'],
                good=data['status']['good']
            )
        )
