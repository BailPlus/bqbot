#bqbot:event.notice.group_admin 群管理员变动事件

from __future__ import annotations
from dataclasses import dataclass
from typing import override
from enum import Enum
from . import Notice, NoticeType


class GroupAdminType(Enum):
    """群管理员变化类型"""
    SET = "set"
    UNSET = "unset"


@dataclass(frozen=True, kw_only=True)
class GroupAdmin(Notice):
    """群文件上传事件"""
    notice_type: NoticeType = NoticeType.GROUP_ADMIN
    sub_type: GroupAdminType    # 子类型
    group_id: int  # 群号
    user_id: int  # 发送者QQ号

    @override
    @classmethod
    def _is_suitable(cls, data: dict):
        return super()._is_suitable(data) and data['notice_type'] == cls.notice_type.value
    
    @override
    @classmethod
    def _from_dict(cls, data: dict) -> GroupAdmin:
        return cls(
            raw_data=data,
            self_id=data['self_id'],
            time=data['time'],
            notice_type=NoticeType(data['notice_type']),
            sub_type=GroupAdminType(data['sub_type']),
            group_id=data['group_id'],
            user_id=data['user_id']
        )
