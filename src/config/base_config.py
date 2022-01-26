import os.path
from abc import ABC
from os import environ

from src.helpers.enums import Environments
from src.helpers import utils
from src.providers.config.base_config import BaseConfigProvider
from src.providers.config.config_dict import ConfigFromDictionaryProvider
from src.providers.config.config_env import ConfigFromEnvironmentProvider
from src.providers.config.config_json import ConfigFromJsonProvider


class BaseConfig(ABC):
    DEFAULT_ENVIRONMENT = Environments.TEST

    def __init__(self, environment=DEFAULT_ENVIRONMENT):
        super().__init__()
        self.config_variables = {"TARGET_ENVIRONMENT": environ.get("TARGET_ENVIRONMENT", environment.value)}
        self.config_providers = []

    def __getattr__(self, item: str) -> str:
        return self.config_variables.get(item, None)

    def register_variable(self, item: str) -> str:
        for provider in self.config_providers:
            value = provider.get(item, None)
            if value is not None:
                self.config_variables[item] = value
                return self
        return self

    def get_variable(self, item: str) -> str:
        return self.__getattr__(item)


class BaseMultiSourcedConfig(BaseConfig):
    def __init__(self, environment=BaseConfig.DEFAULT_ENVIRONMENT, dictionary_config={}):
        super().__init__(environment)
        self.add_provider(ConfigFromEnvironmentProvider())
        json_file = f"{utils.get_root_path()}{os.path.sep}" \
                    f"src{os.path.sep}" \
                    f"config{os.path.sep}" \
                    f"presets{os.path.sep}" \
                    f"{self.TARGET_ENVIRONMENT}.config.json"
        if os.path.exists(json_file):
            self.add_provider(ConfigFromJsonProvider(json_file))
        self.add_provider(ConfigFromDictionaryProvider(dictionary_config))

    def add_provider(self, provider: BaseConfigProvider):
        if provider is not None:
            self.config_providers.append(provider)
        return self
