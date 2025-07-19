#bqbot:event.notice.group_ban 群禁言事件

from __future__ import annotations
from dataclasses import dataclass
from typing import override
from enum import Enum
from . import Notice, NoticeType


class GroupBanType(Enum):
    """群禁言类型"""
    BAN = "ban" # 禁言
    LIFT_BAN = "lift_ban"   # 解除禁言


@dataclass(frozen=True, kw_only=True)
class GroupBan(Notice):
    """群禁言事件"""
    notice_type: NoticeType = NoticeType.GROUP_BAN
    sub_type: GroupBanType # 子类型
    group_id: int  # 群号
    operator_id: int    # 操作者QQ号
    user_id: int  # 被禁言QQ号
    duration: int  # 禁言时长

    @override
    @classmethod
    def _is_suitable(cls, data: dict):
        return super()._is_suitable(data) and data['notice_type'] == cls.notice_type.value

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> GroupBan:
        return cls(
            raw_data=data,
            self_id=data['self_id'],
            time=data['time'],
            notice_type=NoticeType(data['notice_type']),
            sub_type=GroupBanType(data['sub_type']),
            group_id=data['group_id'],
            operator_id=data['operator_id'],
            user_id=data['user_id'],
            duration=data['duration']
        )
