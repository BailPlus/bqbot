#bqbot:message_sengment.json json消息

from __future__ import annotations
from dataclasses import dataclass
from typing import override
from . import MessageSegment, MessageSegmentType


@dataclass(init=False)
class Json(MessageSegment):
    """json消息"""
    type: MessageSegmentType = MessageSegmentType.JSON
    data: str

    def __init__(self, data: str, *, raw_data: dict|None = None):
        super().__init__(raw_data=raw_data)
        self.data = data

    @override
    def to_dict(self) -> dict:
        return self.raw_data or {
            "type": self.type.value,
            "data": {
                "data": self.data
            }
        }

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> Json:
        return cls(
            raw_data=data,
            data=data['data']['data']
        )
