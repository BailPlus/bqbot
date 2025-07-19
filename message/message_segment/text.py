#bqbot:message_sengment.text 文本

from __future__ import annotations
from dataclasses import dataclass
from typing import override
from . import MessageSegment, MessageSegmentType


@dataclass(init=False)
class Text(MessageSegment):
    """文本"""
    type: MessageSegmentType = MessageSegmentType.TEXT
    text: str   # 文本内容

    def __init__(self, text: str, *, raw_data: dict|None = None):
        super().__init__(raw_data=raw_data)
        self.text = text

    @override
    def to_dict(self) -> dict:
        return self.raw_data or {
            "type": self.type.value,
            "data": {
                "text": self.text
            }
        }

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> Text:
        return cls(
            raw_data=data,
            text=data['data']['text']
        )
