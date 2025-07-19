#bqbot:event.request.group 群请求事件模块

from __future__ import annotations
from typing import override
from dataclasses import dataclass
from enum import Enum
from . import Request, RequestType
from .. import EventType


class GroupRequestType(Enum):
    """群请求类型"""
    ADD = "add"     # 有人加群
    INVITE = "nvite"    # bot被邀请
    OTHERS = None   # 其他


@dataclass(frozen=True, kw_only=True)
class GroupRequest(Request):
    """群请求事件"""
    request_type = RequestType.GROUP
    sub_type: GroupRequestType  # 群请求类型
    group_id: int   # 群号

    @override
    @classmethod
    def _is_suitable(cls, data: dict) -> bool:
        return super()._is_suitable(data) and data.get("request_type") == cls.request_type.value

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> GroupRequest:
        return cls(
            raw_data=data,
            self_id=data['self_id'],
            time=data['time'],
            post_type=EventType(data['post_type']),
            request_type=RequestType(data.get('request_type')),
            sub_type=GroupRequestType(data.get('sub_type')),
            group_id=data['group_id'],
            user_id=data['user_id'],
            comment=data['comment'],
            flag=data['flag']
        )
