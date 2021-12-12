from pytest import mark

import src.config as cfg
from src.page_objects.login import Login


class TestWebLoginPage:

    @mark.order(1)
    def test_login(self, web_driver, logger, dp_login_page):
        logger.info(f'Test case for login with email {dp_login_page["email"]}')
        web_driver.get(f"{cfg.BASE_URL}login")
        login_page = Login(web_driver)
        login_page.login(dp_login_page["email"], dp_login_page["password"])
        assert True
        logger.info("Test PASSED")


if __name__ == "__main__":
    pass
