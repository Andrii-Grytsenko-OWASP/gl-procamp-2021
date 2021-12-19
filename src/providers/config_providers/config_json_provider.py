from json import load

from src.providers.config_providers.base_config_provider import BaseDictConfigProvider


class ConfigFromJsonProvider(BaseDictConfigProvider):
    def __init__(self, json_config_file):
        super(ConfigFromJsonProvider, self).__init__()
        self.config_dict = {}
        try:
            with open(json_config_file) as jcf:
                self.config_dict = load(jcf)
        except:
            raise IOError(f"Error reading config file [{json_config_file}]")
