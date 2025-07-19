#bqbot:connection.http.httpx_sender httpx发送模块

from typing import override
from httpx import Client
from . import HttpSender


class HttpxSender(HttpSender):
    client: Client  # httpx客户端

    def __init__(self, client: Client|None = None):
        self.client = client or Client()
    
    @override
    def send(self, action: str, data: dict) -> dict:
        return self.client.post('/'+action, json=data).json()
