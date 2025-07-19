#bqbot:connection.http.receiver http接收模块

from typing import override
from ... import OneBot11Connection


class HttpSender(OneBot11Connection):
    """http发送接口"""
    @override
    def recv(self):
        raise NotImplementedError('http发送接口不支持接收消息')
