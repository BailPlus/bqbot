#bqbot:message_sengment.record 语音

from __future__ import annotations
from dataclasses import dataclass
from typing import override, Optional
from . import MessageSegment, MessageSegmentType


@dataclass(init=False)
class Record(MessageSegment):
    """语音"""
    type: MessageSegmentType = MessageSegmentType.RECORD
    file: str   # 语音文件名
    magic: bool = False # 是否为变声
    url: Optional[str] = None   # 语音URL
    cache: bool = True  # 是否缓存
    proxy: bool = True  # 是否使用代理
    timeout: Optional[int] = None   # 发送时下载语音超时时间

    def __init__(self, 
                 file: str, *, 
                 magic: bool = False,
                 url: Optional[str] = None,
                 cache: bool = True,
                 proxy: bool = True,
                 timeout: Optional[int] = None,
                 raw_data: dict | None = None):
        super().__init__(raw_data)
        self.file = file
        self.magic = magic
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
                "magic": self.magic,
                "url": self.url,
                "cache": self.cache,
                "proxy": self.proxy,
                "timeout": self.timeout
            }
        }

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> Record:
        return cls(
            raw_data=data,
            file=data['data']['file'],
            magic=bool(data['data'].get('magic')),
            url=data['data'].get('url'),
            cache=data['data'].get('cache', True),
            proxy=data['data'].get('proxy', True),
            timeout=data['data'].get('timeout')
        )
