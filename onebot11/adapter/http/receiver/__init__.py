#bqbot:connection.http.receiver http接收模块

from typing import override
from ... import OneBot11Connection


class HttpReceiver(OneBot11Connection):
    """http接收接口"""
    @override
    def send(self, action: str, data: dict):
        raise NotImplementedError('http接收接口不支持发送消息')
