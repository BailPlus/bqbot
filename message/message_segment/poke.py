#bqbot:message_sengment.poke 戳一戳

from __future__ import annotations
from dataclasses import dataclass
from typing import override, Optional
from . import MessageSegment, MessageSegmentType


@dataclass(init=False)
class Poke(MessageSegment):
    """戳一戳"""
    type: MessageSegmentType = MessageSegmentType.POKE
    poke_type: str  # 戳一戳类型
    id: str # 戳一戳id
    name: Optional[str]   # 戳一戳名称

    def __init__(self,
                 type: str,
                 id: str, *,
                 name: Optional[str] = None,
                 raw_data: dict|None = None):
        super().__init__(raw_data=raw_data)
        self.poke_type = type
        self.id = id
        self.name = name

    @override
    def to_dict(self) -> dict:
        return self.raw_data or {
            "type": self.type.value,
            "data": {
                "type": self.poke_type,
                "id": self.id,
                "name": self.name
            }
        }

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> Poke:
        return cls(
            raw_data=data,
            type=data['data']['type'],
            id=data['data']['id'],
            name=data['data']['name']
        )
