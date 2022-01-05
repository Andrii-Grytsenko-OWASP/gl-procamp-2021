import os.path
from abc import ABC
from os import environ

from src.enums import Environments
from src.helpers import utils
from src.providers.config_providers.base_config_provider import BaseConfigProvider
from src.providers.config_providers.config_dict_provider import ConfigFromDictionaryProvider
from src.providers.config_providers.config_env_provider import ConfigFromEnvironmentProvider
from src.providers.config_providers.config_json_provider import ConfigFromJsonProvider


class BaseConfig(ABC):
    DEFAULT_ENVIRONMENT = Environments.TEST

    def __init__(self, environment=DEFAULT_ENVIRONMENT):
        super().__init__()
        self.config_variables = {"TARGET_ENVIRONMENT": environ.get("TARGET_ENVIRONMENT", environment.value)}
        self.config_providers = []

    def __getattr__(self, item):
        return self.config_variables.get(item, None)

    def register_variable(self, item):
        for provider in self.config_providers:
            value = provider.get(item, None)
            if value is not None:
                self.config_variables[item] = value
                return self
        return self

    def get_variable(self, item):
        return self.__getattr__(item)


class BaseMultiSourcedConfig(BaseConfig):
    def __init__(self, environment=BaseConfig.DEFAULT_ENVIRONMENT, dictionary_config={}):
        super().__init__(environment)
        self.add_provider(ConfigFromEnvironmentProvider())
        json_file = f"{utils.get_root_path()}{os.path.sep}src{os.path.sep}config{os.path.sep}presets{os.path.sep}{self.TARGET_ENVIRONMENT}.config.json"
        if os.path.exists(json_file):
            self.add_provider(ConfigFromJsonProvider(json_file))
        self.add_provider(ConfigFromDictionaryProvider(dictionary_config))

    def add_provider(self, provider: BaseConfigProvider):
        if provider is not None:
            self.config_providers.append(provider)
        return self
