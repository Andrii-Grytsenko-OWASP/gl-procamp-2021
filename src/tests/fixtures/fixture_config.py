from pytest import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.config.config import CFG
from src.helpers.enums import WebDrivers


@fixture(scope="class")
def web_driver():
    if WebDrivers(CFG.WEB_DRIVER) == WebDrivers.WD_CHROME:
        options = Options()
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu')
        wd = webdriver.Chrome(executable_path='..\\..\\bin\\chromedriver.exe', options=options)
    else:
        wd = webdriver.Firefox()
    yield wd
    wd.close()
    del wd
