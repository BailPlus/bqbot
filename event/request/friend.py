#bqbot:event.request.friend 好友请求事件模块

from __future__ import annotations
from typing import override
from dataclasses import dataclass
from . import Request, RequestType
from .. import EventType


@dataclass(frozen=True, kw_only=True)
class FriendRequest(Request):
    """好友请求事件"""
    request_type = RequestType.FRIEND

    @override
    @classmethod
    def _is_suitable(cls, data: dict) -> bool:
        return super()._is_suitable(data) and data.get("request_type") == cls.request_type.value

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> FriendRequest:
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
