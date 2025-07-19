#bqbot:event.notice 通知事件模块

from __future__ import annotations
from enum import Enum
from dataclasses import dataclass
from typing import override
from .. import Event, EventType


class NoticeType(Enum):
    """通知事件类型"""
    GROUP_UPLOAD = "group_upload"   # 群文件上传
    GROUP_ADMIN = "group_admin"     # 群管理员变动
    GROUP_DECREASE = "group_decrease"   # 群成员减少
    GROUP_INCREASE = "group_increase"   # 群成员增加
    GROUP_BAN = "group_ban" # 群禁言
    FRIEND_ADD = "friend_add"   # 好友添加
    GROUP_RECALL = "group_recall"   # 群消息撤回
    FRIEND_RECALL = "friend_recall"   # 好友消息撤回
    GROUP_MSG_EMOJI_LIKE = 'group_msg_emoji_like'   # 群消息表情表态
    NOTIFY = "notify"   # 其他通知
    OTHERS = None

    @override
    @classmethod
    def _missing_(cls, value) -> NoticeType:
        return NoticeType.OTHERS


@dataclass(frozen=True, kw_only=True)
class Notice(Event):
    """通知事件基类"""
    post_type: EventType = EventType.NOTICE
    notice_type: NoticeType

    @override
    @classmethod
    def _is_suitable(cls, data: dict):
        return super()._is_suitable(data) and data['post_type'] == cls.post_type.value
    
    @override
    @classmethod
    def _from_dict(cls, data: dict) -> Notice:
        return cls(
            raw_data=data,
            self_id=data['self_id'],
            time=data['time'],
            notice_type=NoticeType(data['notice_type'])
        )
