class BaseError(BaseException):
    def __init__(self, message="Base Error occurred"):
        self.message = message
