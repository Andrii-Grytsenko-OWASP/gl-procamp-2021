from selenium.webdriver.common.by import By


class SignUpPage:
    text_name = (By.ID("name"))
    text_job_title = (By.ID("jobTitle"))
    text_organization = (By.ID("organization"))
    text_email = (By.ID("email"))
    text_password = (By.ID("password"))
    text_confirm_password = (By.ID("confirm_password"))
    checkbox_terms = (By.ID("termsCheckbox"))
    button_sign_up = (By.ID("signUpButton"))

    def __init__(self, webdriver):
        self.wd = webdriver

    def sign_up(self, name: str, job_title: str, organization: str, email: str, password: str):
        self.wd.find_element_by_id(SignUpPage.text_name).send_keys(name)
        self.wd.find_element_by_id(SignUpPage.text_job_title).send_keys(job_title)
        self.wd.find_element_by_id(SignUpPage.text_organization).send_keys(organization)
        self.wd.find_element_by_id(SignUpPage.text_email).send_keys(email)
        self.wd.find_element_by_id(SignUpPage.text_password).send_keys(password)
        self.wd.find_element_by_id(SignUpPage.text_confirm_password).send_keys(password)
        self.wd.find_element_by_id(SignUpPage.checkbox_terms).click()
        self.wd.find_element_by_id(SignUpPage.button_sign_up).click()
        return self
