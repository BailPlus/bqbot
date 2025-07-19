#bqbot:event.notice.notify.lucky_king 群红包运气王事件

from __future__ import annotations
from dataclasses import dataclass
from typing import override
from . import BaseNotify, NotifyType
from .. import NoticeType


@dataclass(frozen=True, kw_only=True)
class LuckyKing(BaseNotify):
    """群红包运气王事件"""
    sub_type: NotifyType = NotifyType.LUCKY_KING
    target_id: int # 被戳的群员QQ

    @property
    def is_self(self) -> bool:
        """判断是否是戳自己"""
        return self.target_id == self.self_id

    @override
    @classmethod
    def _is_suitable(cls, data: dict):
        return super()._is_suitable(data) and data['sub_type'] == cls.sub_type.value

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> LuckyKing:
        return cls(
            raw_data=data,
            self_id=data['self_id'],
            time=data['time'],
            notice_type=NoticeType(data['notice_type']),
            sub_type=NotifyType(data['sub_type']),
            group_id=data['group_id'],
            user_id=data['user_id'],
            target_id=data['target_id'],
        )
