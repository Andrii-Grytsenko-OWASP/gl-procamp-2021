from alchemize import JsonTransmuter
from pytest import mark

from src.models.api.user import User


class TestWebApi:

    @mark.order(1)
    def test_api_dashboard(self, cid_api, logger, dp_api):
        logger.info(f'Test case for login with email {dp_api["email"]}')
        try:
            cid_api.login(User(dp_api["email"], dp_api["password"]))
            dashboard = cid_api.dashboard()
            assert (dashboard.type == dp_api["expected_result"])
            assert (JsonTransmuter.transmute_to(dashboard.data) != "")
            logger.info("Test PASSED")
        except:
            assert False
            logger.info("Test FAILED")
