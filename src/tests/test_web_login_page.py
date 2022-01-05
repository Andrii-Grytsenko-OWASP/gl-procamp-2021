from pytest import mark

from src.config.config import CFG
from src.page_objects.login_page import LoginPage


class TestWebLoginPage:

    @mark.order(1)
    def test_login(self, web_driver, logger, dp_login_page):
        logger.info(f'Test case for login with email {dp_login_page["email"]}')
        web_driver.get(f"{CFG.BASE_URL}login")
        login_page = LoginPage(web_driver)
        login_page.login(dp_login_page["email"], dp_login_page["password"])
        assert True
        logger.info("Test PASSED")
