#bqbot:message_sengment.contact 联系人分享

from __future__ import annotations
from dataclasses import dataclass
from typing import override
from enum import Enum
from . import MessageSegment, MessageSegmentType


class ContactType(Enum):
    """联系人分享类型"""
    QQ = "qq"
    GROUP = "group"

@dataclass(init=False)
class Contact(MessageSegment):
    """联系人分享"""
    type: MessageSegmentType = MessageSegmentType.CONTACT
    contact_type: ContactType
    id: str   # 推荐的qq/群号

    def __init__(self,
                 contact_type: ContactType|str,
                 id: str, *,
                 raw_data: dict|None = None):
        super().__init__(raw_data=raw_data)
        self.contact_type = ContactType(contact_type)
        self.id = id

    @override
    def to_dict(self) -> dict:
        return self.raw_data or {
            "type": self.type.value,
            "data": {
                "contact_type": self.contact_type.value,
                "id": self.id
            }
        }

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> Contact:
        return cls(
            raw_data=data,
            contact_type=ContactType(data['data']['type']),
            id=data['data']['id']
        )
