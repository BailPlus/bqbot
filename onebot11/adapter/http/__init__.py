#bqbot:connection.http http连接模块

from typing import override
from .receiver import HttpReceiver
from .sender import HttpSender
from .. import OneBot11Connection

class HttpConnection(OneBot11Connection):
    receiver: HttpReceiver
    sender: HttpSender

    def __init__(self, receiver: HttpReceiver, sender: HttpSender):
        self.receiver = receiver
        self.sender = sender

    @override
    def recv(self) -> dict:
        return self.receiver.recv()
    
    @override
    def send(self, action: str, data: dict) -> dict:
        self.sender.send(action, data)
        return self.receiver.recv()
