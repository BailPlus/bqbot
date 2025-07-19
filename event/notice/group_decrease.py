#bqbot:event.notice.group_decrease 群成员减少事件

from __future__ import annotations
from dataclasses import dataclass
from typing import override
from enum import Enum
from . import Notice, NoticeType


class GroupDecreaseType(Enum):
    """群成员减少类型"""
    LEAVE = "leave" # 退群
    KICK = "kick"   # 群成员被踢
    KICK_ME = "kick_me" # bot自己被踢


@dataclass(frozen=True, kw_only=True)
class GroupDecrease(Notice):
    """群成员减少事件"""
    notice_type: NoticeType = NoticeType.GROUP_DECREASE
    sub_type: GroupDecreaseType # 子类型
    group_id: int  # 群号
    operator_id: int    # 操作者QQ号
    user_id: int  # 离开者QQ号

    @override
    @classmethod
    def _is_suitable(cls, data: dict):
        return super()._is_suitable(data) and data['notice_type'] == cls.notice_type.value
    
    @override
    @classmethod
    def _from_dict(cls, data: dict) -> GroupDecrease:
        return cls(
            raw_data=data,
            self_id=data['self_id'],
            time=data['time'],
            notice_type=NoticeType(data['notice_type']),
            sub_type=GroupDecreaseType(data['sub_type']),
            group_id=data['group_id'],
            operator_id=data['operator_id'],
            user_id=data['user_id']
        )
