#bqbot:message 消息

from __future__ import annotations
from .message_segment import MessageSegment


class Message(list[MessageSegment]):
    """消息
由多个消息段组成"""
    @classmethod
    def from_json(cls, json: list[dict]) -> Message:
        """从JSON转为消息"""
        obj = cls()
        for seg_json in json:
            assert (seg := MessageSegment.factory(seg_json))
            obj.append(seg)
        return obj

    @classmethod
    def from_cqcode(cls, cqcode: str) -> Message:
        """从CQ码转为消息"""
        raise NotImplementedError

    def to_json(self) -> list:
        """转为JSON"""
        return [seg.to_dict() for seg in self]

    def to_cqcode(self) -> str:
        """转为CQ码"""
        return "".join(seg.to_cqcode() for seg in self)
