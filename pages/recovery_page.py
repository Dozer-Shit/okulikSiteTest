from selenium.webdriver.chrome import webdriver

from pages.base_page import BasePage


class RecoveryPage(BasePage):
    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
