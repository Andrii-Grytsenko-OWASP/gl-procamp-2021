import json

from src.providers.config_providers.base_config_provider import BaseDictConfigProvider


class ConfigFromDictionaryProvider(BaseDictConfigProvider):
    def __init__(self, config_dict={}):
        super(ConfigFromDictionaryProvider, self).__init__()
        # Make a local copy of source dictionary
        self.config_source = json.loads(json.dumps(config_dict if config_dict is not None else {}))
