import dotenv

from src.providers.config_providers.base_config_provider import BaseConfigProvider


class ConfigFromDotEnvProvider(BaseConfigProvider):
    def __init__(self, dotenv_file, target_environment):
        super(ConfigFromDotEnvProvider, self).__init__()
        self.dotenv_file = dotenv_file
        self.target_environment = target_environment

    def get(self, env_variable: str, default_value=None):
        return dotenv.get_key(self.dotenv_file, f"{env_variable}_{self.target_environment}")
