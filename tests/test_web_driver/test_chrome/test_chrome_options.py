import unittest

from python_practice_automation_test_lib.web_driver.chrome.chrome_options import ChromeOptions


class TestChromeOptions(unittest.TestCase):
    def setUp(self) -> None:
        self.dict_options = {
            "start-maximized": True,
            "pageLoad": 2560,
            "implicit": 1440,
        }
        self.options = ChromeOptions(dict_options=self.dict_options).options

    def test_set_page_load(self):
        assert self.options.timeouts['pageLoad'] == 2560, "Payload time not correct"

    def test_set_implicit_wait(self):
        assert self.options.timeouts['implicit'] == 1440, "Implicit time not correct"

    def test_set_max_windows(self):
        assert "start-maximized" in self.options.arguments, "Start maximize not added to argument"
