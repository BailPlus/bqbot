#bqbot:message_sengment.reply 回复消息

from __future__ import annotations
from dataclasses import dataclass
from typing import override
from . import MessageSegment, MessageSegmentType


@dataclass(init=False)
class Reply(MessageSegment):
    """回复消息"""
    type: MessageSegmentType = MessageSegmentType.REPLY
    id: str   # 回复的消息id

    def __init__(self, id: str, *, raw_data: dict|None = None):
        super().__init__(raw_data=raw_data)
        self.id = id

    @override
    def to_dict(self) -> dict:
        return self.raw_data or {
            "type": self.type.value,
            "data": {
                "id": self.id
            }
        }

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> Reply:
        return cls(
            raw_data=data,
            id=data['data']['id']
        )
