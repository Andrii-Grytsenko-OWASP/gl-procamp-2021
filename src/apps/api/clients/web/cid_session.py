import requests

from src.config.config import CFG
from src.helpers.enums import ErrorMessages
from src.helpers.utils import get_url
from src.models.api.response.cid_login_response import LoginResponse
from src.models.api.user import User


class CidSession:
    HEADER_X_TOKEN = "X-Token"

    def __init__(self, user: User, login_data: LoginResponse):
        self.session = requests.Session()
        self.user = user
        self.login_data = login_data
        self.session.headers.update({CidSession.HEADER_X_TOKEN: self.login_data.token})

    def get(self, endpoint: str, *args, **kwargs):
        return self.session.get(url=get_url(CFG.BASE_URL, endpoint),
                                *args, **kwargs)

    def post(self):
        raise NotImplemented(ErrorMessages.NOT_IMPLEMENTED_YET)

    def put(self):
        raise NotImplemented(ErrorMessages.NOT_IMPLEMENTED_YET)

    def patch(self):
        raise NotImplemented(ErrorMessages.NOT_IMPLEMENTED_YET)

    def delete(self):
        raise NotImplemented(ErrorMessages.NOT_IMPLEMENTED_YET)

    def options(self):
        raise NotImplemented(ErrorMessages.NOT_IMPLEMENTED_YET)

    def head(self):
        raise NotImplemented(ErrorMessages.NOT_IMPLEMENTED_YET)

    def trace(self):
        raise NotImplemented(ErrorMessages.NOT_IMPLEMENTED_YET)

    def connect(self):
        raise NotImplemented(ErrorMessages.NOT_IMPLEMENTED_YET)
