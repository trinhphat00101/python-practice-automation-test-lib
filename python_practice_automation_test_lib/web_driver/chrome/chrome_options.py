from selenium import webdriver


class ChromeOptions:
    def __init__(self, dict_options):
        self.options = webdriver.ChromeOptions()
        self.dict_options = dict_options
        self.dict_timeouts = {}
        self.set_page_load()
        self.set_implicit_wait()
        self.set_max_windows()
        self.options.timeouts = self.dict_timeouts

    def set_page_load(self):
        if "pageLoad" in self.dict_options:
            self.dict_timeouts["pageLoad"] = self.dict_options["pageLoad"]

    def set_implicit_wait(self):
        if "implicit" in self.dict_options:
            self.dict_timeouts["implicit"] = self.dict_options["implicit"]

    def set_max_windows(self):
        if "start-maximized" in self.dict_options:
            self.options.add_argument("start-maximized")
