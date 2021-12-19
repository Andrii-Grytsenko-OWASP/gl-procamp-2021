from abc import ABC, abstractmethod


class BaseConfigProvider(ABC):
    @abstractmethod
    def get(self, key: str, value: str = None):
        pass


class BaseDictConfigProvider(BaseConfigProvider, ABC):
    def __init__(self):
        self.config_dict = None

    def get(self, key: str):
        return self.config_dict.get(key, None)
