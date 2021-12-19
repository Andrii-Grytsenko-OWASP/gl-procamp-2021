import json
from src.providers.config_providers.base_config_provider import BaseDictConfigProvider
from src.error_handling import NoConfigDictionaryError


class ConfigFromDictionaryProvider(BaseDictConfigProvider):
    def __init__(self, config_dict):
        super(ConfigFromDictionaryProvider, self).__init__()
        if config_dict is None:
            raise NoConfigDictionaryError()
        self.config_dict = json.loads(json.dumps(config_dict))
