#bqbot:event.message.group 群聊消息

from __future__ import annotations
from dataclasses import dataclass
from typing import override, Optional
from enum import Enum
from . import MessageEvent, MessageType, BaseMessageSubType, BaseSender, SenderSex
from ...errors import NotAnymous
from ...message import Message
from ...message.message_segment import MessageSegment


class GroupMessageSubType(BaseMessageSubType):
    """私聊消息子类型"""
    NORMAL = "normal"   # 常规消息
    ANYMOUS = "anonymous"   # 匿名消息
    NOTICE = "notice"   # 通知消息
    OTHERS = None # 其他消息


class GroupMemberRole(Enum):
    OWNER = "owner"
    ADMINISTRATOR = "admin"
    MEMBER = "member"
    OTHERS = None


@dataclass(frozen=True, kw_only=True)
class GroupSender(BaseSender):
    """私聊消息发送者"""
    card: str   # 群昵称
    area: Optional[str]   # 地区
    level: Optional[str]  # 等级
    role: GroupMemberRole   # 群角色
    title: Optional[str]  # 专属头衔


@dataclass(init=False, repr=False)
class Anymous:
    _id: int    # 匿名用户ID(不是QQ号)
    _name: str  # 匿名用户名称
    _flag: str  # 匿名用户标识（用于禁言等操作）
    is_anonymous: bool  # 是否匿名

    def __init__(self, data: dict|None):
        if data is None:
            self.is_anonymous = False
        else:
            self.is_anonymous = True
            self._id = data['id']
            self._name = data['name']
            self._flag = data['flag']

    @property
    def id(self) -> int:
        if not self.is_anonymous:
            raise NotAnymous("This is not an anonymous user")
        return self._id
    
    @property
    def name(self) -> str:
        if not self.is_anonymous:
            raise NotAnymous("This is not an anonymous user")
        return self._name

    @property
    def flag(self) -> str:
        if not self.is_anonymous:
            raise NotAnymous("This is not an anonymous user")
        return self._flag

    def __repr__(self) -> str:
        if self.is_anonymous:
            return f"Anonymous({self.id=}, {self.name=}, {self.flag=})"
        else:
            return 'NotAnymous'

    def __bool__(self) -> bool:
        return self.is_anonymous


@dataclass(frozen=True, kw_only=True)
class GroupMessage(MessageEvent):
    """群聊消息"""
    message_type: MessageType = MessageType.GROUP
    sub_type: GroupMessageSubType
    sender: GroupSender
    group_id: int   # 群号
    anymous: Anymous    # 匿名身份

    @override
    @classmethod
    def _is_suitable(cls, data: dict) -> bool:
        return super()._is_suitable(data) and data.get("message_type") == MessageType.GROUP.value

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> GroupMessage:
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
            sub_type=GroupMessageSubType(
                data.get("sub_type")
            ),
            message_id=data['message_id'],
            group_id=data['group_id'],
            user_id=data['user_id'],
            anymous=Anymous(
                data.get("anonymous")
            ),
            message=messages,
            raw_message=data['raw_message'],
            font=data['font'],
            sender=GroupSender(
                user_id=data['sender']['user_id'],
                nickname=data['sender']['nickname'],
                sex=SenderSex(
                    data['sender'].get('sex','unknown')
                ),
                age=data['sender'].get('age'),
                card=data['sender']['card'],
                area=data['sender'].get('area'),
                level=data['sender'].get('level'),
                role=GroupMemberRole(
                    data['sender'].get('role')
                ),
                title=data['sender'].get('title'),
            )
        )
