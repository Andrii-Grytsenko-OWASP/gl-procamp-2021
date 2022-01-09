import requests
from alchemize import JsonTransmuter
from requests.auth import HTTPBasicAuth

from src.apps.api.clients.web.cid_session import CidSession
from src.config.config import Config
from src.models.api.response.cid_login_response import LoginResponse
from src.models.api.user import User
from src.providers.service.auth.base_auth_provider import BaseAuthProvider


class AuthBasicProvider(BaseAuthProvider):
    def __init__(self, config: Config):
        super().__init__(config)

    def login(self, endpoint: str, user: User) -> CidSession:
        response = requests.get(url=f"{self._config.BASE_URL}{endpoint}",
                                auth=HTTPBasicAuth(user.email, user.password))
        response.raise_for_status()
        session = CidSession(user, JsonTransmuter.transmute_from(response.json(), LoginResponse))
        return session
