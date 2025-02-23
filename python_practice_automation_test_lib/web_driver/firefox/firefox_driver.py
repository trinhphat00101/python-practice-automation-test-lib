from python_practice_automation_test_lib.web_driver.firefox.firefox_options import FirefoxOptions
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class FirefoxDriver:
    def __init__(self, dict_options):
        self.dict_options = dict_options
        self.options = FirefoxOptions(self.dict_options).options
        self.driver = self.init_firefox_driver()

    def init_firefox_driver(self):
        return webdriver.Firefox(options=self.options, service=FirefoxService(GeckoDriverManager().install()))

