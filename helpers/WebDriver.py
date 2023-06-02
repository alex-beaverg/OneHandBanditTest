from selenium import webdriver


class WebDriver(webdriver.Chrome):
    """Docstring: Class singleton WebDriver"""

    def __new__(cls):
        """Docstring: Special constructor for singleton class WebDriver"""
        if not hasattr(cls, 'instance'):
            cls.instance = super(WebDriver, cls).__new__(cls)
        return cls.instance
