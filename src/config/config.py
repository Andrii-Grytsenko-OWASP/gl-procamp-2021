from src.config.base_config import *


class Config(BaseMultiSourcedConfig):
    def __init__(self):
        super().__init__()
        self.register_variable("BASE_URL")
        self.register_variable("WEB_DRIVER")


CFG = Config()
