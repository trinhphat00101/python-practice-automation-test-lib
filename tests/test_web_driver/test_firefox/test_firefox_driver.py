import unittest

from python_practice_automation_test_lib.web_driver.firefox.firefox_driver import FirefoxDriver


class TestChromeDriver(unittest.TestCase):

    def setUp(self) -> None:
        self.dict_options = {
            "width": 2560,
            "height": 1440,
            "set_windows_max_size": True
        }
        self.firefox = FirefoxDriver(dict_options=self.dict_options)

    def test_init_firefox_driver(self):
        """Test init_firefox_driver"""
        assert self.firefox.driver.caps['browserName'] == "firefox"

    def tearDown(self) -> None:
        self.firefox.driver.quit()
