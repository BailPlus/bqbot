#bqbot:message_sengment.video 视频

from __future__ import annotations
from dataclasses import dataclass
from typing import override, Optional
from . import MessageSegment, MessageSegmentType


@dataclass(init=False)
class Video(MessageSegment):
    """视频"""
    type: MessageSegmentType = MessageSegmentType.VIDEO
    file: str   # 视频文件名
    url: Optional[str] = None   # 视频URL
    cache: bool = True  # 是否缓存
    proxy: bool = True  # 是否使用代理
    timeout: Optional[int] = None   # 发送时下载视频超时时间

    def __init__(self,
                 file: str, *,
                 url: Optional[str] = None,
                 cache: bool = True,
                 proxy: bool = True,
                 timeout: Optional[int] = None,
                raw_data: dict | None = None):
        super().__init__(raw_data)
        self.file = file
        self.url = url
        self.cache = cache
        self.proxy = proxy
        self.timeout = timeout

    @override
    def to_dict(self) -> dict:
        return self.raw_data or {
            "type": self.type.value,
            "data": {
                "file": self.file,
                "url": self.url,
                "cache": self.cache,
                "proxy": self.proxy,
                "timeout": self.timeout,
            }
        }

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> Video:
        return cls(
            raw_data=data,
            file=data['data']['file'],
            url=data['data'].get('url'),
            cache=data['data'].get('cache', True),
            proxy=data['data'].get('proxy', True),
            timeout=data['data'].get('timeout')
        )
