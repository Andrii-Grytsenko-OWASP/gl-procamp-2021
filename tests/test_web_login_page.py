from pytest import mark

from src.apps.ui.clients.web.cid_endpoints import CidEndpoints
from src.config.config import CFG
from src.helpers.utils import get_url
from src.page_objects.login_page import LoginPage


class TestWebLoginPage:

    @mark.order(1)
    def test_login(self, web_driver, logger, dp_login_page):
        logger.info(f'Test case for email {dp_login_page["email"]}')
        login_url = get_url(CFG.BASE_URL, CidEndpoints.login)
        web_driver.get(login_url)
        login_page = LoginPage(web_driver)
        login_page.login(dp_login_page["email"], dp_login_page["password"])
        current_url = web_driver.current_url
        assert ((current_url != login_url) == dp_login_page["expected_result"])
        logger.info("Test PASSED")
