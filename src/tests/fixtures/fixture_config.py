from pytest import *
from selenium import webdriver

from src import config as cfg
from src.enums import *


@fixture(scope="class")
def webdriver():
    if cfg.WEB_DRIVER.capitalize() == WebDrivers.WD_CHROME:
        wd = webdriver.Chrome
    else:
        wd = webdriver.Firefox
    yield wd
    del wd
