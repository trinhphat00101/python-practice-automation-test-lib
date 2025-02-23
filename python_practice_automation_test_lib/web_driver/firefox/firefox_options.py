from selenium import webdriver


class FirefoxOptions:
    def __init__(self, dict_options):
        self.dict_options = dict_options
        self.options = webdriver.FirefoxOptions()
        self.set_width()
        self.set_height()

    def set_width(self):
        if "width" in self.dict_options:
            self.options.add_argument(f"--width={self.dict_options['width']}")

    def set_height(self):
        if "height" in self.dict_options:
            self.options.add_argument(f"--height={self.dict_options['height']}")
