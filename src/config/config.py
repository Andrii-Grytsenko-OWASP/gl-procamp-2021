import os.path
from os import environ

from src.config.base_config import BaseConfig
from src.providers.config_providers.config_dict_provider import ConfigFromDictionaryProvider
from src.providers.config_providers.config_env_provider import ConfigFromEnvironmentProvider
from src.providers.config_providers.config_hierarchical_provider import HierarchicalConfigProvider
from src.providers.config_providers.config_json_provider import ConfigFromJsonProvider


class Config(BaseConfig):
    def __init__(self):
        super(Config, self).__init__()

        json_config_file = f"../config/presets/{environ.get('TARGET_ENVIRONMENT', Config.DEFAULT_ENVIRONMENT.value)}.config.json"
        config_env = ConfigFromEnvironmentProvider()
        config_json = ConfigFromJsonProvider(json_config_file)
        config_dict = ConfigFromDictionaryProvider(
            {
                "BASE_URL": "https://app.cosmosid.com/",
                "WEB_DRIVER": "Chrome"
            }
        )
        self.config_provider_hierarchy = HierarchicalConfigProvider([config_env, config_json, config_dict])

        self._register_key("BASE_URL")
        self._register_key("WEB_DRIVER")


CFG = Config()
