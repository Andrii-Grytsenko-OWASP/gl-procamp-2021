from pytest import *
from selenium import webdriver

from src import config as cfg


@fixture(scope="class")
def webdriver():
    if cfg.WEB_DRIVER == "Chrome":
        wd = webdriver.Chrome
    else:
        wd = webdriver.Firefox
    yield wd
    del wd
