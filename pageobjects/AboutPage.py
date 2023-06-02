from selenium.webdriver.remote.webelement import WebElement

from helpers.Locators import AboutPageLocators
from pageobjects.BasePage import BasePage


class AboutPage(BasePage):
    """Docstring: Class AboutPage extends class BasePage"""

    def __init__(self, driver) -> None:
        """Docstring: Constructor for class AboutPage"""
        super().__init__(driver)
        self.__ap_real_text = 'Information'
        self.__ap_find_text = driver.find_element(*AboutPageLocators.FIND_TEXT).text[:11]

    # Getters:
    def get_ap_real_text(self) -> str:
        """Docstring: Getter for ap_real_text variable"""
        return self.__ap_real_text

    def get_ap_find_text(self) -> WebElement:
        """Docstring: Getter for ap_find_text webElement"""
        return self.__ap_find_text
