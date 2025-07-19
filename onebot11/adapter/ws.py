#bqbot:connection.ws websocket连接模块

from __future__ import annotations
from typing import override
from websocket import WebSocket
from . import Connection
import json


class WsConnection(Connection):
    ws: WebSocket   # websocket对象

    def __init__(self, ws: WebSocket):
        self.ws = ws

    @classmethod
    def connect(cls, url: str) -> WsConnection:
        ws = WebSocket()
        ws.connect(url)
        return cls(ws)

    @override
    def recv(self) -> dict:
        return json.loads(
            self.ws.recv()
        )

    @override
    def send(self, action: str, data: dict):
        self.ws.send(
            json.dumps({
                'action': action,
                'params': data
            })
        )
        return self.recv()
