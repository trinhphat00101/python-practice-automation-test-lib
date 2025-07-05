from python_practice_automation_test_lib.web_driver.chrome.chrome_driver import ChromeDriver
from python_practice_automation_test_lib.web_driver.edge.edge_driver import EdgeDriver
from python_practice_automation_test_lib.web_driver.firefox.firefox_driver import FirefoxDriver


class WebDriver:
    def __init__(self, name_browser: str, dict_options={}):
        self.name_browser = name_browser
        self.dict_options = dict_options
        self.driver = self.init_web_driver()

    def init_web_driver(self):
        if self.name_browser == "chrome":
            driver = ChromeDriver(dict_options=self.dict_options)
        elif self.name_browser == "edge":
            driver = EdgeDriver(dict_options=self.dict_options)
        elif self.name_browser == "firefox":
            driver = FirefoxDriver(dict_options=self.dict_options)
        return driver.driver
