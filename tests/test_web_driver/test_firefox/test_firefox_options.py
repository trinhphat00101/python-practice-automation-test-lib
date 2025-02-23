import unittest

from python_practice_automation_test_lib.web_driver.firefox.firefox_options import FirefoxOptions


class TestFirefoxOptions(unittest.TestCase):
    def setUp(self) -> None:
        self.dict_options = {
            "width": 2560,
            "height": 1440
        }
        self.firefox = FirefoxOptions(dict_options=self.dict_options).options

    def test_set_width(self):
        expected_value = f"--width={self.dict_options['width']}"
        assert expected_value in self.firefox.arguments, "Width argument not set up correctly"

    def test_set_height(self):
        expected_value = f"--height={self.dict_options['height']}"
        assert expected_value in self.firefox.arguments, "height argument not set up correctly"
