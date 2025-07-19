#bqbot:message_sengments 消息段

from __future__ import annotations
from dataclasses import dataclass
from abc import abstractmethod
from typing import Optional, override, TypeVar
from enum import Enum
from ...common import FactoryInterface

T = TypeVar("T", bound='MessageSegment')


class MessageSegmentType(Enum):
    """消息段类型"""
    TEXT = "text"   # 文本
    FACE = "face"   # 表情
    IMAGE = "image" # 图片
    RECORD = "record"   # 语音
    VIDEO = "video" # 视频
    AT = "at"   # 艾特某人
    RPS = "rps" # 猜拳
    DICE = "dice"   # 骰子
    SHAKE = "shake" # 抖窗
    POKE = "poke"   # 戳一戳
    ANONYMOUS = "anonymous" # 匿名消息
    SHARE = "share" # 链接分享
    CONTACT = "contact" # 推荐好友或群
    LOCATION = "location"   # 位置
    MUSIC = "music" # 音乐分享
    REPLY = "reply" # 回复
    FORWARD = "forward" # 合并转发
    NODE = "node"   # 合并转发节点
    XML = "xml" # XML
    JSON = "json"   # JSON
    OTHERS = None   # 其他

    @override
    @classmethod
    def _missing_(cls, value) -> MessageSegmentType:
        return cls.OTHERS


@dataclass(init=False)
class MessageSegment(FactoryInterface):
    """消息段"""
    type: MessageSegmentType
    raw_data: Optional[dict] = None

    def __init__(self,raw_data: Optional[dict] = None):
        if not hasattr(self, "type"):
            self.type = MessageSegmentType.OTHERS
        self.raw_data = raw_data

    def to_dict(self) -> dict:
        if self.__class__ is not MessageSegment:
            raise NotImplementedError
        return self.raw_data or {
            "type": self.type.value,
            "data": {}
        }

    def to_cqcode(self) -> str:
        """转为CQ码"""
        raise NotImplementedError

    @classmethod
    def from_cqcode(cls, cqcode: str) -> MessageSegment:
        """从CQ码创建消息段"""
        raise NotImplementedError

    @override
    @classmethod
    def _is_suitable(cls, data: dict) -> bool:
        if cls is MessageSegment:
            return True
        return data.get("type") == cls.type.value

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> MessageSegment:
        if cls is not MessageSegment:
            raise NotImplementedError
        return cls(raw_data=data)
