from src.config.base_config import *
from src.providers.config.config_dotenv import ConfigFromDotEnvProvider


class Config(BaseMultiSourcedConfig):
    def __init__(self):
        super().__init__()
        dotenv_file = f"{utils.get_root_path()}{os.path.sep}.env"
        self.add_provider(ConfigFromDotEnvProvider(dotenv_file, self.TARGET_ENVIRONMENT))
        self.register_variable("BASE_URL")
        self.register_variable("WEB_DRIVER")
        self.register_variable("USER_EMAIL")
        self.register_variable("USER_PASSWORD")


CFG = Config()
