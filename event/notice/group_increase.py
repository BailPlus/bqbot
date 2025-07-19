#bqbot:event.notice.group_increase 群成员增加事件

from __future__ import annotations
from dataclasses import dataclass
from typing import override
from enum import Enum
from . import Notice, NoticeType


class GroupIncreaseType(Enum):
    """群成员增加类型"""
    APPROVE = "approve" # 通过申请
    INVITE = "invite"   # 管理员邀请


@dataclass(frozen=True, kw_only=True)
class GroupIncrease(Notice):
    """群成员增加事件"""
    notice_type: NoticeType = NoticeType.GROUP_INCREASE
    sub_type: GroupIncreaseType # 子类型
    group_id: int  # 群号
    operator_id: int    # 操作者QQ号
    user_id: int  # 加入者QQ号

    @override
    @classmethod
    def _is_suitable(cls, data: dict):
        return super()._is_suitable(data) and data['notice_type'] == cls.notice_type.value
    
    @override
    @classmethod
    def _from_dict(cls, data: dict) -> GroupIncrease:
        return cls(
            raw_data=data,
            self_id=data['self_id'],
            time=data['time'],
            notice_type=NoticeType(data['notice_type']),
            sub_type=GroupIncreaseType(data['sub_type']),
            group_id=data['group_id'],
            operator_id=data['operator_id'],
            user_id=data['user_id']
        )
