#bqbot:message_sengment.face 表情

from __future__ import annotations
from dataclasses import dataclass
from typing import override
from . import MessageSegment, MessageSegmentType


@dataclass(init=False)
class Face(MessageSegment):
    """表情"""
    type: MessageSegmentType = MessageSegmentType.FACE
    id: str # 表情id

    def __init__(self, id: str, *, raw_data: dict | None = None):
        super().__init__(raw_data)
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
    def _from_dict(cls, data: dict) -> Face:
        return cls(
            raw_data=data,
            id=data['data']['id']
        )
