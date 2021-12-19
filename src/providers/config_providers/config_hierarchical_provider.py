from src.error_handling import NoConfigHierarchyError
from src.providers.config_providers.base_config_provider import BaseConfigProvider


class HierarchicalConfigProvider(BaseConfigProvider):
    def __init__(self, config_providers=None):
        super(HierarchicalConfigProvider, self).__init__()
        if config_providers is None:
            raise NoConfigHierarchyError()
        self.config_providers = config_providers

    def get(self, key: str):
        for provider in self.config_providers:
            value = provider.get(key)
            if value is not None:
                return value
        return None
