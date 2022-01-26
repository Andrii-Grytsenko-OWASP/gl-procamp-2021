import selenium
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, webdriver: selenium.webdriver):
        self.wd = webdriver

    def click(self, element):
        self.wd.find_element(*element).click()

    def send_keys(self, element, keys):
        self.wd.find_element(*element).send_keys(keys)

    def exists(self, element):
        timeout = 10000
        try:
            element_present = EC.presence_of_element_located(element)
            WebDriverWait(self.wd, timeout).until(element_present)
        except TimeoutException:
            return False
        return True
