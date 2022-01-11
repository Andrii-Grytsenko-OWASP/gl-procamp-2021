from alchemize import JsonTransmuter

from src.apps.api.clients.web.cid_endpoints import CidEndpoints
from src.helpers.enums import ApiResponseType
from src.helpers.error_handling import ApiSessionError
from src.models.api.response.api_response import ApiResponse
from src.models.api.response.cid_dashboard_response import DashboardResponse
from src.models.api.user import User


class CidWebApiClient:
    def __init__(self, config, auth_provider):
        self._config = config
        self._auth_provider = auth_provider(config)
        self._session = None

    def login(self, user: User) -> ApiResponse:
        try:
            self._session = self._auth_provider.login(CidEndpoints.login, user)
            return ApiResponse(200, ApiResponseType.ok, self)
        except:
            self._session = None
            return ApiResponse(401, ApiResponseType.error, self)

    def dashboard(self) -> ApiResponse:
        if self._session is None:
            raise ApiSessionError()
        response = self._session.get(CidEndpoints.dashboard)
        return ApiResponse(
            response.status_code,
            ApiResponseType.ok if response.ok else ApiResponseType.error,
            JsonTransmuter.transmute_from(response.json(), DashboardResponse)
            if response.ok else response.text
        )
