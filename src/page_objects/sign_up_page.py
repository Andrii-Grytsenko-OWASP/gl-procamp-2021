from selenium.webdriver.common.by import By
from src.page_objects.base_page import BasePage


class SignUpPage(BasePage):
    text_name = (By.ID, "name")
    text_job_title = (By.ID, "jobTitle")
    text_organization = (By.ID, "organization")
    text_email = (By.ID, "email")
    text_password = (By.ID, "password")
    text_confirm_password = (By.ID, "confirm_password")
    checkbox_terms = (By.ID, "termsCheckbox")
    button_sign_up = (By.ID, "signUpButton")

    def sign_up(self, name: str, job_title: str, organization: str, email: str, password: str):
        self.send_keys(SignUpPage.text_name, name)
        self.send_keys(SignUpPage.text_job_title, job_title)
        self.send_keys(SignUpPage.text_organization, organization)
        self.send_keys(SignUpPage.text_email, email)
        self.send_keys(SignUpPage.text_password, password)
        self.send_keys(SignUpPage.text_confirm_password, password)
        self.click(SignUpPage.checkbox_terms)
        self.click(SignUpPage.button_sign_up)
        return self
