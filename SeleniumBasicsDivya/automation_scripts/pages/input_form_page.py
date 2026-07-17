from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InputFormPage(BasePage):

    NAME = (By.NAME, "name")
    EMAIL = (By.NAME, "email")
    PHONE = (By.NAME, "phone")
    ADDRESS = (By.NAME, "address")
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")

    def fill_form(self, name, email, phone, address):

        self.driver.find_element(*self.NAME).send_keys(name)
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.PHONE).send_keys(phone)
        self.driver.find_element(*self.ADDRESS).send_keys(address)

    def submit_form(self):
        self.driver.find_element(*self.SUBMIT).click()

    def get_success_message(self):
        return self.driver.page_source
    