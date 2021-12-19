class BaseError(BaseException):
    def __init__(self, message="Base Error occurred"):
        self.message = message


class NoConfigHierarchyError(BaseError):
    def __init__(self, message=None):
        super(NoConfigHierarchyError, self).__init__((message, "No config providers defined")[message is None])


class NoConfigDictionaryError(BaseError):
    def __init__(self, message=None):
        super(NoConfigDictionaryError, self).__init__((message, "No config dictionary provided")[message is None])


class UnregisteredConfigKeyError(BaseError):
    def __init__(self, message=None):
        super(UnregisteredConfigKeyError, self).__init__((message, "Unregistered config key")[message is None])
