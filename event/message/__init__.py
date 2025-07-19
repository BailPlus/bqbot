#bqbot:event.message 消息事件模块

from __future__ import annotations
from enum import Enum
from dataclasses import dataclass
from typing import override
from abc import ABC
from .. import Event, EventType
from ...message import Message
from ...message.message_segment import MessageSegment


class MessageType(Enum):
    """消息类型"""
    PRIVATE = "private" # 私聊消息
    GROUP   = "group"   # 群消息
    OTHERS  = ""  # 其他消息


class BaseMessageSubType(Enum):
    """消息子类型基类"""


class SenderSex(Enum):
    """发送者性别"""
    MALE = "male"
    FEMALE = "female"
    UNKNOWN = "unknown"


@dataclass(frozen=True, kw_only=True)
class BaseSender(ABC):
    """消息发送者基类"""
    user_id: int  # 发送者QQ号
    nickname: str # 发送者昵称
    sex: SenderSex  # 发送者性别
    age: int    # 发送者年龄


@dataclass(frozen=True, kw_only=True)
class MessageEvent(Event):
    """元事件"""
    post_type: EventType = EventType.MESSAGE
    message_type: MessageType   # 消息类型
    sub_type: BaseMessageSubType    # 消息子类型
    message_id: int # 消息ID
    user_id: int    # 消息发送者QQ号
    message: Message    # 消息内容(消息段)
    raw_message: str    # 原始消息内容(CQ码)
    font: int   # 字号
    sender: BaseSender  # 发送者信息

    @override
    @classmethod
    def _is_suitable(cls, data: dict) -> bool:
        return super()._is_suitable(data) and data.get("post_type") == EventType.MESSAGE.value

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> MessageEvent:
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
            sub_type=BaseMessageSubType(
                data.get("sub_type")
            ),
            message_id=data['message_id'],
            user_id=data['user_id'],
            message=messages,
            raw_message=data['raw_message'],
            font=data['font'],
            sender=BaseSender(
                user_id=data['sender']['user_id'],
                nickname=data['sender']['nickname'],
                sex=SenderSex(
                    data['sender'].get('sex','unknown')
                ),
                age=data['sender'].get('age')
            )
        )

    def reply(self, message: str):
        """回复消息"""
        # TODO
        raise NotImplementedError

    def recall(self):
        """撤回消息"""
        # TODO
        raise NotImplementedError
