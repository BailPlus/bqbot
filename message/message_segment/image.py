#bqbot:message_sengment.image 图片

from __future__ import annotations
from dataclasses import dataclass
from typing import override, Optional
from . import MessageSegment, MessageSegmentType


@dataclass(init=False)
class Image(MessageSegment):
    """图片"""
    type: MessageSegmentType = MessageSegmentType.IMAGE
    file: str   # 图片文件名
    flash: Optional[str] = None  # 是否为闪照
    url: Optional[str] = None   # 图片URL
    cache: bool = True  # 是否缓存
    proxy: bool = True  # 是否使用代理
    timeout: Optional[int] = None   # 发送时下载图片超时时间

    def __init__(self, 
                 file: str, *,
                 flash: Optional[str] = None,
                 url: Optional[str] = None,
                 cache: bool = True,
                 proxy: bool = True,
                 timeout: Optional[int] = None,
                 raw_data: dict | None = None):
        super().__init__(raw_data)
        self.file = file
        self.flash = flash
        self.url = url
        self.cache = cache
        self.proxy = proxy
        self.timeout = timeout

    @property
    def is_flash(self) -> bool:
        """是否为闪照"""
        return self.flash == "flash"
        
    @override
    def to_dict(self) -> dict:
        return self.raw_data or {
            "type": self.type.value,
            "data": {
                "file": self.file,
                "type": self.flash,
                "url": self.url,
                "cache": self.cache,
                "proxy": self.proxy,
                "timeout": self.timeout,
            }
        }

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> Image:
        return cls(
            raw_data=data,
            file=data['data']['file'],
            flash=data['data'].get('type'),
            url=data['data'].get('url'),
            cache=data['data'].get('cache', True),
            proxy=data['data'].get('proxy', True),
            timeout=data['data'].get('timeout')
        )
