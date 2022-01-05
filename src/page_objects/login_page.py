from selenium.webdriver.common.by import By

class LoginPage:
    # div_dialog = (By.XPATH("//div[@role='dialog']"))
    # button_dialog_ok = (By.XPATH("//div[@role='dialog']/div/button[2]"))
    # text_email = (By.ID("email"))
    # text_password = (By.ID("password"))
    # button_sign_in = (By.ID("signInButton"))
    # link_forgot_password = (By.XPATH("//form/div/a"))
    # link_sign_up = (By.XPATH("//*[@id='mount']/div/div[1]/div/div/a[2]"))
    # button_sign_in_with_google = (By.XPATH("//div[@id='g-signin2']/div"))

    div_dialog = "//div[@role='dialog']"
    button_dialog_ok = "//div[@role='dialog']/div/button[2]"
    text_email = "email"
    text_password = "password"
    button_sign_in = "signInButton"
    link_forgot_password = "//form/div/a"
    link_sign_up = "//*[@id='mount']/div/div[1]/div/div/a[2]"
    button_sign_in_with_google = "//div[@id='g-signin2']/div"

    def __init__(self, webdriver):
        self.wd = webdriver

    def is_dialog_opened(self):
        return self.wd.find_element_by_xpath(LoginPage.div_dialog).is_displayed()

    def close_dialog(self):
        self.wd.find_element_by_xpath(LoginPage.button_dialog_ok).click()
        return self

    def login(self, email: str, password: str):
        if self.is_dialog_opened():
            self.close_dialog()
        self.wd.find_element_by_id(LoginPage.text_email).send_keys(email)
        self.wd.find_element_by_id(LoginPage.text_password).send_keys(password)
        self.wd.find_element_by_id(LoginPage.button_sign_in).click()
        return self