from abc import ABC, abstractmethod

from src.config.config import Config


class BaseAuthProvider(ABC):
    def __init__(self, config: Config):
        super().__init__()
        self._config = config

    @abstractmethod
    def login(self, *args, **kwargs):
        pass
