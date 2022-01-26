from pytest import mark

from src.apps.ui.clients.web.cid_endpoints import CidEndpoints
from src.config.config import CFG
from src.helpers.utils import get_url
from src.page_objects.sign_up_page import SignUpPage


class TestWebRegisterPage:

    @mark.order(1)
    def test_register(self, web_driver, logger, dp_register_page):
        logger.info(f'Test case for register with email {dp_register_page["email"]}')
        login_url = get_url(CFG.BASE_URL, CidEndpoints.login)
        register_url = get_url(CFG.BASE_URL, CidEndpoints.register)
        web_driver.get(register_url)
        signup_page = SignUpPage(web_driver)
        signup_page.sign_up(dp_register_page["name"], dp_register_page["job_title"],
                           dp_register_page["organization"],
                           dp_register_page["email"], dp_register_page["password"])
        current_url = web_driver.current_url
        logger.info(login_url)
        logger.info(current_url)
        assert ((current_url != login_url) == dp_register_page["expected_result"])
        logger.info("Test PASSED")
