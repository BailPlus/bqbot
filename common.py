from abc import ABC, abstractmethod
from typing import TypeVar

T = TypeVar('T', bound='FactoryInterface')


class FactoryInterface(ABC):
    """工厂递归查找子类接口"""
    @classmethod
    def factory(cls: type[T], data: dict) -> T|None:
        """寻找合适的子类并创建实例"""
        for subclass in cls.__subclasses__():
            if obj := subclass.factory(data):
                return obj
        if cls._is_suitable(data):
            return cls._from_dict(data)

    @classmethod
    @abstractmethod
    def _from_dict(cls: type[T], data: dict) -> T:
        """从字典中创建子类"""

    @classmethod
    @abstractmethod
    def _is_suitable(cls: type[T], data: dict) -> bool:
        """判断当前子类是否可适合绑定"""
