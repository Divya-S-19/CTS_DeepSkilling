from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class DropdownPage(BasePage):

    DROPDOWN = (By.ID, "select-demo")

    def select_day(self, day_name):
        Select(
            self.driver.find_element(*self.DROPDOWN)
        ).select_by_visible_text(day_name)

    def get_selected_day(self):
        return Select(
            self.driver.find_element(*self.DROPDOWN)
        ).first_selected_option.text