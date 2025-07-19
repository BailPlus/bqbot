#bqbot:event 事件模块

from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import override
from ..common import FactoryInterface


class EventType(Enum):
    """事件类型"""
    MESSAGE = "message" # 消息
    NOTICE = "notice"   # 通知
    REQUEST = "request" # 请求
    META_EVENT = "meta_event"   # 元事件
    OTHERS = "others"   # 其他


class EventInterface(FactoryInterface):
    """事件接口"""


@dataclass(frozen=True, kw_only=True)
class Event(EventInterface):
    """事件基类"""
    raw_data: dict  # 原始数据
    post_type: EventType    # 事件类型
    self_id: int    # 机器人QQ号
    time: int   # 事件发生的时间

    @override
    @classmethod
    def _from_dict(cls, data: dict):
        """从字典创建事件。每个子类都需要重写"""
        return cls(
            raw_data=data,
            post_type=EventType(data['post_type']),
            self_id=data['self_id'],
            time=data['time']
        )

    @override
    @classmethod
    def _is_suitable(cls, data: dict) -> bool:
        """判断data所示的是否可被当前类绑定"""
        return True
