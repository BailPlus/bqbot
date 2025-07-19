#bqbot:bot 机器人模块

from .adapter import Connection
from .event import Event
from .event.message import MessageEvent
from .event.message.private import PrivateMessage
from .event.message.group import GroupMessage
from .message import Message
import atexit


class Bot:
    connection: Connection  # 连接

    def __init__(self, connection: Connection):
        self.connection = connection

    def on_event(self, event: Event):
        """处理事件"""

    def on_message(self, message: MessageEvent):
        """处理消息"""
    
    def on_private_message(self, message: PrivateMessage):
        """处理私聊消息"""

    def on_group_message(self, message: GroupMessage):
        """处理群消息"""

    def on_exit(self):
        """退出时调用"""

    def run(self):
        """运行机器人"""
        atexit.register(self.on_exit)
        while True:
            event = Event.factory(self.connection.recv())
            assert event
            self.on_event(event)
            if isinstance(event, MessageEvent):
                self.on_message(event)
                if isinstance(event, PrivateMessage):
                    self.on_private_message(event)
                if isinstance(event, GroupMessage):
                    self.on_group_message(event)
