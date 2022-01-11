import os

from pytest import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.config.config import CFG
from src.helpers import utils
from src.helpers.enums import WebDrivers
from src.apps.api.clients.web.cid_api import CidWebApiClient
from src.providers.service.auth.auth_basic_provider import AuthBasicProvider


@fixture(scope="class")
def web_driver():
    if WebDrivers(CFG.WEB_DRIVER) == WebDrivers.WD_CHROME:
        options = Options()
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu')
        wd = webdriver.Chrome(executable_path=os.path.join(utils.get_root_path(), 'bin', 'chromedriver.exe'),
                              options=options)
    else:
        wd = webdriver.Firefox()
    yield wd
    wd.close()
    del wd


@fixture(scope="class")
def cid_api():
    api = CidWebApiClient(CFG, AuthBasicProvider)
    yield api
    del api
