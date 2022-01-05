from os import environ
from src.providers.config_providers.base_config_provider import BaseConfigProvider


class ConfigFromEnvironmentProvider(BaseConfigProvider):
    def __init__(self):
        super(ConfigFromEnvironmentProvider, self).__init__()

    def get(self, env_variable: str, default_value=None):
        return environ.get(env_variable, default_value)
