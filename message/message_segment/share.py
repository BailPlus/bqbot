#bqbot:message_sengment.share 链接分享

from __future__ import annotations
from dataclasses import dataclass
from typing import override, Optional
from . import MessageSegment, MessageSegmentType


@dataclass(init=False)
class Share(MessageSegment):
    """链接分享"""
    type: MessageSegmentType = MessageSegmentType.SHARE
    url: str  # 链接
    title: str # 标题
    content: Optional[str]   # 内容描述
    image: Optional[str]     # 图片url

    def __init__(self,
                 url: str,
                 title: str, *,
                 content: Optional[str] = None,
                 image: Optional[str] = None,
                 raw_data: dict|None = None):
        super().__init__(raw_data=raw_data)
        self.url = url
        self.title = title
        self.content = content
        self.image = image

    @override
    def to_dict(self) -> dict:
        return self.raw_data or {
            "type": self.type.value,
            "data": {
                "url": self.url,
                "title": self.title,
                "content": self.content,
                "image": self.image
            }
        }

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> Share:
        return cls(
            raw_data=data,
            url=data['data']['url'],
            title=data['data']['title'],
            content=data['data']['content'],
            image=data['data']['image']
        )
