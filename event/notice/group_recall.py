#bqbot:event.notice.group_recall 群消息撤回事件

from __future__ import annotations
from dataclasses import dataclass
from typing import override
from . import Notice, NoticeType


@dataclass(frozen=True, kw_only=True)
class GroupRecall(Notice):
    """群消息撤回事件"""
    notice_type: NoticeType = NoticeType.GROUP_RECALL
    group_id: int  # 群号
    user_id: int  # 被撤回的QQ号
    operator_id: int    # 操作者QQ号
    message_id: int # 被撤回的消息ID

    @override
    @classmethod
    def _is_suitable(cls, data: dict):
        return super()._is_suitable(data) and data['notice_type'] == cls.notice_type.value

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> GroupRecall:
        return cls(
            raw_data=data,
            self_id=data['self_id'],
            time=data['time'],
            notice_type=NoticeType(data['notice_type']),
            group_id=data['group_id'],
            user_id=data['user_id'],
            operator_id=data['operator_id'],
            message_id=data['message_id']
        )
