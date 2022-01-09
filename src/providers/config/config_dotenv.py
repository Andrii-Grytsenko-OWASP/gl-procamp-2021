import dotenv

from src.providers.config.base_config import BaseConfigProvider


class ConfigFromDotEnvProvider(BaseConfigProvider):
    def __init__(self, dotenv_file: str, target_environment: str):
        super(ConfigFromDotEnvProvider, self).__init__()
        self.dotenv_file = dotenv_file
        self.target_environment = target_environment

    def get(self, env_variable: str, default_value=None) -> str:
        return dotenv.get_key(self.dotenv_file, f"{env_variable}_{self.target_environment}")
