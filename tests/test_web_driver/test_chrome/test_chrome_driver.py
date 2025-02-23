import unittest

from python_practice_automation_test_lib.web_driver.chrome.chrome_driver import ChromeDriver


class TestChromeDriver(unittest.TestCase):

    def setUp(self) -> None:
        self.dict_options = {
            "start-maximized": True,
            "pageLoad": 2560,
            "implicit": 1440,
        }
        self.chrome = ChromeDriver(dict_options=self.dict_options)

    def test_init_chrome_driver(self):
        """Test init_chrome_driver"""
        assert self.chrome.driver.caps['browserName'] == "chrome"
