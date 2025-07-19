#bqbot:message_sengment.location 位置

from __future__ import annotations
from dataclasses import dataclass
from typing import override, Optional
from . import MessageSegment, MessageSegmentType


@dataclass(init=False)
class Location(MessageSegment):
    """位置"""
    type: MessageSegmentType = MessageSegmentType.LOCATION
    lat: str    # 纬度
    lon: str    # 经度
    title: Optional[str]     # 标题
    content: Optional[str]   # 内容描述

    def __init__(self,
                 lat: str,
                 lon: str, *,
                 title: Optional[str] = None,
                 content: Optional[str] = None,
                 raw_data: dict|None = None):
        super().__init__(raw_data=raw_data)
        self.lat = lat
        self.lon = lon
        self.title = title
        self.content = content

    @override
    def to_dict(self) -> dict:
        return self.raw_data or {
            "type": self.type.value,
            "data": {
                "lat": self.lat,
                "lon": self.lon,
                "title": self.title,
                "content": self.content
            }
        }

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> Location:
        return cls(
            raw_data=data,
            lat=data['data']['lat'],
            lon=data['data']['lon'],
            title=data['data']['title'],
            content=data['data']['content']
        )
