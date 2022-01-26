from alchemize import JsonTransmuter
from pytest import mark

from src.models.api.user import User


class TestWebApi:

    @mark.order(1)
    def test_api_dashboard(self, cid_api, logger, dp_api):
        logger.info(f'Test case for email {dp_api["email"]}')
        login = cid_api.login(User(dp_api["email"], dp_api["password"]))
        assert (login.type == dp_api["expected_result"])
        dashboard = cid_api.dashboard()
        assert (dashboard.type == dp_api["expected_result"])
        assert (JsonTransmuter.transmute_to(dashboard.data) != "")
        logger.info("Test PASSED")
