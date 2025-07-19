#bqbot:message_sengment.rps 猜拳

from __future__ import annotations
from dataclasses import dataclass
from typing import override
from . import MessageSegment, MessageSegmentType


@dataclass(init=False)
class Rps(MessageSegment):
    """猜拳"""
    type: MessageSegmentType = MessageSegmentType.RPS

    def __init__(self, *, raw_data: dict|None = None):
        super().__init__(raw_data=raw_data)

    @override
    def to_dict(self) -> dict:
        return self.raw_data or {
            "type": self.type.value,
            "data": {}
        }

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> Rps:
        return cls(
            raw_data=data,
        )
