#bqbot:i18n 国际化模块

from abc import ABC
from typing import override


class Strings(ABC):
    """国际化接口"""
    http_sender_does_not_support_receiving_data = "HttpSender does not support receiving data"


def set_i18n(i18n: Strings):
    """设置国际化模块"""
    global strings
    strings = i18n
