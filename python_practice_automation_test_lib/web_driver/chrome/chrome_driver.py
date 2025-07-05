from python_practice_automation_test_lib.web_driver.chrome.chrome_options import ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class ChromeDriver:
    def __init__(self, dict_options):
        self.dict_options = dict_options
        self.options = ChromeOptions(self.dict_options).options
        self.driver = self.init_chrome_driver()

    def init_chrome_driver(self):
        return webdriver.Chrome(options=self.options, service=ChromeService(ChromeDriverManager().install()))

    def get_url(self):
        return self.driver.current_url
