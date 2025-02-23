import unittest

from python_practice_automation_test_lib.web_driver.edge.edge_driver import EdgeDriver


class TestEdgeDriver(unittest.TestCase):
    def setUp(self) -> None:
        self.dict_options = {
            "start-maximized": True,
            "pageLoad": 2560,
            "implicit": 1440,
        }
        self.edge = EdgeDriver(dict_options=self.dict_options)

    def test_init_edge_driver(self):
        """Test init_chrome_driver"""
        assert self.edge.driver.caps['browserName'] == "MicrosoftEdge"
