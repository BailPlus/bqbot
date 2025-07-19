#bqbot:connect bot端连接相关库

from abc import ABC, abstractmethod

class Connection(ABC):
    """连接接口"""
    @abstractmethod
    def recv(self) -> dict:
        """接收数据"""
    
    @abstractmethod
    def send(self, action: str, data: dict) -> dict:
        """发送数据
action为不含/的api名"""
