from json import load

from src.providers.config.base_config import BaseDictConfigProvider


class ConfigFromJsonProvider(BaseDictConfigProvider):
    def __init__(self, json_config_file: str):
        super(ConfigFromJsonProvider, self).__init__()
        self.config_source = {}
        try:
            with open(json_config_file) as jcf:
                self.config_source = load(jcf)
        except:
            raise IOError(f"Error reading config file [{json_config_file}]")
