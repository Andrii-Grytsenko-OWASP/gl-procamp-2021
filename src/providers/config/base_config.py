from abc import ABC, abstractmethod


class BaseConfigProvider(ABC):
    @abstractmethod
    def get(self, key: str, value: str = None) -> str:
        pass


class BaseDictConfigProvider(BaseConfigProvider):
    def __init__(self):
        self.config_source = {}

    def get(self, key: str, value: str = None) -> str:
        return self.config_source.get(key, value)
