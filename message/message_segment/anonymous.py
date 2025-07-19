#bqbot:message_sengment.anonymous 匿名

from __future__ import annotations
from dataclasses import dataclass
from typing import override
from . import MessageSegment, MessageSegmentType


@dataclass(init=False)
class Anonymous(MessageSegment):
    """匿名"""
    type: MessageSegmentType = MessageSegmentType.ANONYMOUS
    ignore: bool = False    # 无法匿名时是否继续发送

    def __init__(self, *,
                 ignore: bool = False,
                 raw_data: dict|None = None):
        super().__init__(raw_data=raw_data)
        self.ignore = ignore

    @override
    def to_dict(self) -> dict:
        return self.raw_data or {
            "type": self.type.value,
            "data": {
                "ignore": self.ignore
            }
        }

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> Anonymous:
        return cls(
            raw_data=data,
            ignore=data.get("ignore", False)
        )
