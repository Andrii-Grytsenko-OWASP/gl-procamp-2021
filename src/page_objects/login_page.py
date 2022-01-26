from selenium.webdriver.common.by import By
from src.page_objects.base_page import BasePage


class LoginPage(BasePage):
    div_dialog = (By.XPATH, "//div[@role='dialog']")
    button_dialog_ok = (By.XPATH, "//div[@role='dialog']/div/button[2]")
    text_email = (By.ID, "email")
    text_password = (By.ID, "password")
    button_sign_in = (By.ID, "signInButton")
    link_forgot_password = (By.XPATH, "//form/div/a")
    link_sign_up = (By.XPATH, "//*[@id='mount']/div/div[1]/div/div/a[2]")
    button_sign_in_with_google = (By.XPATH, "//div[@id='g-signin2']/div")

    def is_dialog_opened(self) -> bool:
        return self.wd.find_element(*LoginPage.div_dialog).is_displayed()

    def close_dialog(self):
        self.click(LoginPage.button_dialog_ok)
        return self

    def login(self, email: str, password: str):
        if self.is_dialog_opened():
            self.close_dialog()
        self.send_keys(LoginPage.text_email, email)
        self.send_keys(LoginPage.text_password, password)
        self.click(LoginPage.button_sign_in)
        return self
