#bqbot:event.request 请求事件模块

from __future__ import annotations
from enum import Enum
from dataclasses import dataclass
from typing import override
from .. import Event, EventType


class RequestType(Enum):
    """请求事件类型"""
    FRIEND = "friend"   # 好友请求
    GROUP = "group"     # 群请求
    OTHERS = None       # 其他请求


@dataclass(frozen=True, kw_only=True)
class Request(Event):
    """请求事件基类"""
    post_type: EventType = EventType.REQUEST
    request_type: RequestType   # 请求类型
    user_id: int    # 发送请求的 QQ 号
    comment: str    # 验证信息
    flag: str       # 请求句柄

    @override
    @classmethod
    def _is_suitable(cls, data: dict):
        return super()._is_suitable(data) and data['post_type'] == cls.post_type.value

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> Request:
        return cls(
            raw_data=data,
            self_id=data['self_id'],
            time=data['time'],
            post_type=EventType(data['post_type']),
            request_type=RequestType(data.get('request_type')),
            user_id=data['user_id'],
            comment=data['comment'],
            flag=data['flag']
        )
