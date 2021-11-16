from selenium.webdriver.common.by import By
from pages.base.base_element import BaseElement


class SePage(BaseElement):
    BTN_GO = (By.XPATH, "//input[@id='submit']")

    def __init__(self, driver):
        BaseElement.__init__(self, driver)

    def search(self, value):
        self.type((By.XPATH, "//input[@id='q']"), value)

    def click_go(self):
        self.click(self.BTN_GO)
