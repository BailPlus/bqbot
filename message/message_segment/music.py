#bqbot:message_sengment.music 音乐分享

from __future__ import annotations
from dataclasses import dataclass
from typing import override, Optional, overload, Literal
from enum import Enum
from . import MessageSegment, MessageSegmentType


class MusicType(Enum):
    """联系人分享类型"""
    QQ = "qq"
    NETEASE = "163"
    XM = "xm"
    CUSTOM = "custom"
    OTHERS = None

    @override
    @classmethod
    def _missing_(cls, value) -> MusicType:
        return MusicType.OTHERS


@dataclass(init=False)
class Music(MessageSegment):
    """音乐分享"""
    type: MessageSegmentType = MessageSegmentType.MUSIC
    music_type: MusicType
    id: Optional[str]   # 音乐id
    url: Optional[str]  # 点击卡片后跳转的url
    audio: Optional[str]    # 音乐url
    title: Optional[str]     # 标题
    content: Optional[str]   # 内容描述
    image: Optional[str]     # 图片url

    @overload
    def __init__(self,
                 music_type: Literal[MusicType.QQ, MusicType.NETEASE, MusicType.XM], /,
                 id: str,
                 raw_data: Optional[dict]):
        """从qq/网易/虾米音乐创建"""
    @overload
    def __init__(self,
                 music_type: Literal[MusicType.CUSTOM], /,
                 url: str,
                 audio: str,
                 title: str,
                 content: Optional[str] = None,
                 image: Optional[str] = None,
                 raw_data: Optional[dict] = None):
        """从自定义音乐创建"""
    @overload
    def __init__(self,
                 music_type: Literal[MusicType.OTHERS], /,
                 raw_data: Optional[dict] = None):
        """未识别，不填写参数"""
    def __init__(self,
                 music_type: MusicType|str, /,
                 *args, **kw):
        def _parse_args(arg: str, position: int):
            """解析参数
arg(str): 参数名
position(int): 参数位置
type(type): 参数类型"""
            if arg in kw:
                return kw.pop(arg)
            elif len(args) <= position:
                return None
            elif isinstance(args[position], self.__class__.__annotations__.get(arg, object)):
                return args[position]
            else:
                return None

        raw_data = _parse_args("raw_data", -1)
        super().__init__(raw_data)

        self.music_type = MusicType(music_type)
        match self.music_type:
            case MusicType.QQ | MusicType.NETEASE | MusicType.XM:
                self.id = _parse_args("id", 0)
            case MusicType.CUSTOM:
                self.url = _parse_args("url", 0)
                self.audio = _parse_args("audio", 1)
                self.title = _parse_args("title", 2)
                self.content = _parse_args("content", 3)
                self.image = _parse_args("image", 4)
                if self.url is None or self.audio is None or self.title is None:
                    raise ValueError("Custom music requires url, audio, title")
            case _:
                pass

    @override
    def to_dict(self) -> dict:
        return self.raw_data or {
            "type": self.type.value,
            "data": {
                "contact_type": self.music_type.value,
                "id": self.id,
                "url": self.url,
                "audio": self.audio,
                "title": self.title,
                "content": self.content,
                "image": self.image
            }
        }

    @override
    @classmethod
    def _from_dict(cls, data: dict) -> Music:
        music_type = MusicType(data['data']['type'])
        match music_type:
            case MusicType.QQ | MusicType.NETEASE | MusicType.XM:
                return cls(
                    music_type=music_type,
                    id=data['data']['id'],
                    raw_data=data
                ) # type: ignore
            case MusicType.CUSTOM:
                return cls(
                    music_type=music_type,
                    url=data['data']['url'],
                    audio=data['data'].get('audio'),
                    title=data['data'].get('title'),
                    content=data['data'].get('content'),
                    image=data['data'].get('image'),
                    raw_data=data
                ) # type: ignore
            case _:
                return cls(
                    music_type=music_type,
                    raw_data=data
                ) # type: ignore
