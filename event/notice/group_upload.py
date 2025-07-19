#bqbot:event.notice.group_upload 群文件上传事件

from __future__ import annotations
from dataclasses import dataclass
from typing import override
from . import Notice, NoticeType


@dataclass(frozen=True, kw_only=True)
class File:
    """文件信息"""
    id: str  # 文件ID
    name: str  # 文件名
    size: int  # 文件大小
    busid: int  # 文件BUSID


@dataclass(frozen=True, kw_only=True)
class GroupUpload(Notice):
    """群文件上传事件"""
    notice_type: NoticeType = NoticeType.GROUP_UPLOAD
    group_id: int  # 群号
    user_id: int  # 发送者QQ号
    file: File  # 文件信息

    @override
    @classmethod
    def _is_suitable(cls, data: dict):
        return super()._is_suitable(data) and data['notice_type'] == cls.notice_type.value
    
    @override
    @classmethod
    def _from_dict(cls, data: dict) -> GroupUpload:
        return cls(
            raw_data=data,
            self_id=data['self_id'],
            time=data['time'],
            notice_type=NoticeType(data['notice_type']),
            group_id=data['group_id'],
            user_id=data['user_id'],
            file=File(**data['file'])
        )
