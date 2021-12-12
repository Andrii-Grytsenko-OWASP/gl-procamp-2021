from pytest import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src import config as cfg
from src.enums import *


@fixture(scope="class")
def web_driver():
    if cfg.WEB_DRIVER == WebDrivers.WD_CHROME:
        options = Options()
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu')
        wd = webdriver.Chrome(executable_path='..\\..\\bin\\chromedriver.exe', options=options)
    else:
        wd = webdriver.Firefox()
    yield wd
    wd.close()
    del wd
