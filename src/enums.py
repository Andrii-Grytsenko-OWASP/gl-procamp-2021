from enum import Enum


class WebDrivers(Enum):
    WD_CHROME = "Chrome"
    WD_FIREFOX = "Firefox"


class Environments(Enum):
    DEVEL = "dev"
    TEST = "test"
    PROD = "prod"

