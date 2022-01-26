from enum import Enum


class WebDrivers(Enum):
    WD_CHROME = "Chrome"
    WD_FIREFOX = "Firefox"


class Environments(Enum):
    DEVEL = "dev"
    TEST = "test"
    PROD = "prod"


class ApiResponseType(Enum):
    ok = "OK"
    warning = "Warning"
    info = "Info"
    error = "Error"


class ErrorMessages:
    NOT_IMPLEMENTED_YET = "Not implemented yet"
