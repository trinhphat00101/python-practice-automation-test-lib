from python_practice_automation_test_lib.web_driver.edge.edge_options import EdgeOptions
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class EdgeDriver:
    def __init__(self, dict_options):
        self.options = EdgeOptions(dict_options).options
        self.driver = self.init_edge_driver()

    def init_edge_driver(self):
        return webdriver.Edge(options=self.options, service=EdgeService(EdgeChromiumDriverManager().install()))

