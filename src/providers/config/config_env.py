from os import environ
from src.providers.config.base_config import BaseConfigProvider


class ConfigFromEnvironmentProvider(BaseConfigProvider):
    def __init__(self):
        super(ConfigFromEnvironmentProvider, self).__init__()

    def get(self, env_variable: str, default_value=None) -> str:
        return environ.get(env_variable, default_value)
