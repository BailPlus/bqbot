class BqbotException(Exception):
    """机器人框架异常"""

class NotAnymous(BqbotException):
    """非匿名消息"""
