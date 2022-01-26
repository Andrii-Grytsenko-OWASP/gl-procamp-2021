import selenium
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, webdriver: selenium.webdriver):
        self.wd = webdriver

    def click(self, element):
        self.wd.find_element(*element).click()

    def send_keys(self, element, keys):
        self.wd.find_element(*element).send_keys(keys)
