#bqbot:event.meta 元事件模块

from __future__ import annotations
from enum import Enum
from dataclasses import dataclass
from typing import override
from .. import Event, EventType


class MetaEventType(Enum):
    """元事件类型"""
    HEARTBEAT = "heartbeat" # 心跳
    LIFECYCLE = "lifecycle" # 生命周期


@dataclass(frozen=True, kw_only=True)
class MetaEvent(Event):
    """元事件"""
    post_type: EventType = EventType.META_EVENT
    meta_event_type: MetaEventType

    @override
    @classmethod
    def _is_suitable(cls, data: dict) -> bool:
        return super()._is_suitable(data) and data.get("post_type") == cls.post_type.value

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> MetaEvent:
        return cls(
            raw_data=data,
            self_id=data['self_id'],
            time=data['time'],
            meta_event_type=MetaEventType(
                data.get("meta_event_type")
            )
        )
