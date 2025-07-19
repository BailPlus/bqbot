#bqbot:event.notice.friend_add 好友添加事件

from __future__ import annotations
from dataclasses import dataclass
from typing import override
from . import Notice, NoticeType


@dataclass(frozen=True, kw_only=True)
class FriendAdd(Notice):
    """好友添加事件"""
    notice_type: NoticeType = NoticeType.FRIEND_ADD
    user_id: int  # 添加者QQ号

    @override
    @classmethod
    def _is_suitable(cls, data: dict):
        return super()._is_suitable(data) and data['notice_type'] == cls.notice_type.value

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> FriendAdd:
        return cls(
            raw_data=data,
            self_id=data['self_id'],
            time=data['time'],
            notice_type=NoticeType(data['notice_type']),
            user_id=data['user_id'],
        )
