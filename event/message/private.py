#bqbot:event.message.private 私聊消息

from __future__ import annotations
from dataclasses import dataclass
from typing import override
from . import MessageEvent, MessageType, BaseMessageSubType, BaseSender, SenderSex
from ...message import Message
from ...message.message_segment import MessageSegment


class PrivateMessageSubType(BaseMessageSubType):
    """私聊消息子类型"""
    FRIEND = "friend"   # 好友消息
    GROUP = "group" # 群临时会话消息
    OTHERS = "other" # 其他消息


@dataclass(frozen=True, kw_only=True)
class PrivateSender(BaseSender):
    """私聊消息发送者"""
    pass


@dataclass(frozen=True, kw_only=True)
class PrivateMessage(MessageEvent):
    """私聊消息"""
    message_type: MessageType = MessageType.PRIVATE
    sub_type: PrivateMessageSubType
    sender: PrivateSender

    @override
    @classmethod
    def _is_suitable(cls, data: dict) -> bool:
        return super()._is_suitable(data) and data.get("message_type") == MessageType.PRIVATE.value

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> PrivateMessage:
        # 解析消息
        messages = Message()
        for i in data['message']:
            assert (m := MessageSegment.factory(i))
            messages.append(m)

        # 返回对象
        return cls(
            raw_data=data,
            self_id=data['self_id'],
            time=data['time'],
            message_type=MessageType(
                data.get("message_type")
            ),
            sub_type=PrivateMessageSubType(
                data.get("sub_type")
            ),
            message_id=data['message_id'],
            user_id=data['user_id'],
            message=messages,
            raw_message=data['raw_message'],
            font=data['font'],
            sender=PrivateSender(
                user_id=data['sender']['user_id'],
                nickname=data['sender']['nickname'],
                sex=SenderSex(
                    data['sender'].get('sex','unknown')
                ),
                age=data['sender'].get('age')
            )
        )
