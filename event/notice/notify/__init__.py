#bqbot:event.notice.notify 其它通知事件

from __future__ import annotations
from dataclasses import dataclass
from typing import override
from enum import Enum
from .. import Notice, NoticeType


class NotifyType(Enum):
    """通知类型"""
    POKE = "poke"   # 群戳一戳
    LUCKY_KING = "lucky_king"   # 群红包运气王
    HONOR = "honor" # 群成员荣誉变更
    INPUT_STATUS = "input_status"   # 输入状态


@dataclass(frozen=True, kw_only=True)
class BaseNotify(Notice):
    """群其它通知基事件"""
    notice_type: NoticeType = NoticeType.NOTIFY
    sub_type: NotifyType    # 通知类型
    group_id: int  # 群号
    user_id: int  # 被撤回的QQ号

    @override
    @classmethod
    def _is_suitable(cls, data: dict):
        return super()._is_suitable(data) and data['notice_type'] == cls.notice_type.value

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> BaseNotify:
        return cls(
            raw_data=data,
            self_id=data['self_id'],
            time=data['time'],
            notice_type=NoticeType(data['notice_type']),
            sub_type=NotifyType(data['sub_type']),
            group_id=data['group_id'],
            user_id=data['user_id']
        )
