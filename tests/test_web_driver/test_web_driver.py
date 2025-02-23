import unittest
from python_practice_automation_test_lib.web_driver.web_driver import WebDriver


class TestWebDriver(unittest.TestCase):

    def setUp(self) -> None:
        self.dict_options = {
            "start-maximized": True,
            "pageLoad": 2560,
            "implicit": 1440,
        }
        self.driver = None

    def test_init_web_driver_chrome(self):
        self.driver = WebDriver("chrome", dict_options=self.dict_options).driver
        assert self.driver.capabilities['browserName'] == "chrome"

    def test_init_web_driver_edge(self):
        self.driver = WebDriver("edge", dict_options=self.dict_options).driver
        assert self.driver.capabilities['browserName'] == "edge"

    def test_init_web_driver_firefox(self):
        self.driver = WebDriver("firefox", dict_options=self.dict_options).driver
        assert self.driver.capabilities['browserName'] == "firefox"
        self.driver.quit()
