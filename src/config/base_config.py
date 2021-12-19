from src.enums import Environments
from src.error_handling import *


class BaseConfig:
    DEFAULT_ENVIRONMENT = Environments.TEST

    def __init__(self):
        self.config_dic = {}
        self.config_provider_hierarchy = None

    def _register_key(self, item):
        if self.config_provider_hierarchy is None:
            raise NoConfigHierarchyError()
        self.config_dic[item] = self.config_provider_hierarchy.get(item)

    def __getattr__(self, item):
        if item not in self.config_dic:
            #raise UnregisteredConfigKeyError(f"Unregistered config key [{item}]")
            return None
        return self.config_dic[item]

    def get(self, item):
        return self.__getattr__(item)
