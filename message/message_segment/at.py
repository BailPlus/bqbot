#bqbot:message_sengment.at 艾特某人

from __future__ import annotations
from dataclasses import dataclass
from typing import override
from . import MessageSegment, MessageSegmentType


@dataclass(init=False)
class At(MessageSegment):
    """艾特某人"""
    type: MessageSegmentType = MessageSegmentType.AT
    qq: str   # 艾特对象或`all`

    def __init__(self, qq: str, *, raw_data: dict|None = None):
        super().__init__(raw_data=raw_data)
        self.qq = qq

    @override
    def to_dict(self) -> dict:
        return self.raw_data or {
            "type": self.type.value,
            "data": {
                "qq": self.qq
            }
        }

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> At:
        return cls(
            raw_data=data,
            qq=data['data']['qq']
        )
