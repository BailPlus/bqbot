#bqbot:event.notice.notify.honor 群成员荣誉事件

from __future__ import annotations
from dataclasses import dataclass
from typing import override
from enum import Enum
from . import BaseNotify, NotifyType
from .. import NoticeType


class HonorType(Enum):
    """群成员荣誉事件类型"""
    TALKATIVE = "talkative" # 龙王
    PERFORMER = "performer" # 群聊之火
    EMOTION = "emotion" # 快乐源泉


@dataclass(frozen=True, kw_only=True)
class Honor(BaseNotify):
    """群成员荣誉事件"""
    sub_type: NotifyType = NotifyType.LUCKY_KING
    honor_type: HonorType   #　荣誉类型

    @override
    @classmethod
    def _is_suitable(cls, data: dict):
        return super()._is_suitable(data) and data['sub_type'] == cls.sub_type.value

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> Honor:
        return cls(
            raw_data=data,
            self_id=data['self_id'],
            time=data['time'],
            notice_type=NoticeType(data['notice_type']),
            sub_type=NotifyType(data['sub_type']),
            group_id=data['group_id'],
            user_id=data['user_id'],
            honor_type=HonorType(data['honor_type'])
        )
