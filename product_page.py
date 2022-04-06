
from pages.base_page import BasePage
from pages.locators import MainPageLocators
from selenium.webdriver.common.by import By

class PageObject(BasePage):
    def add_backet(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        login_link.click()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(By.CSS_SELECTOR, "div#messages:nth-child(2) strong"), \
            "Success message is presented, but should not be"
