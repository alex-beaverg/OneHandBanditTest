from selenium.webdriver.remote.webelement import WebElement

from helpers.Elements import Elements


class AboutPage:
    """Docstring: Class pageobjects.AboutPage"""
    def __init__(self, driver) -> None:
        """Docstring: Constructor for class pageobjects.AboutPage"""
        self.__driver = driver
        # Webelements and variables:
        self.__ap_game_menu_item = Elements.get_element('AboutPage', 'AP.game_menu_item')
        self.__ap_rules_menu_item = Elements.get_element('AboutPage', 'AP.rules_menu_item')
        self.__ap_real_text = 'Information'
        self.__ap_find_text = Elements.get_element('AboutPage', 'AP.find_text').text[:11]

    # Getters:
    def get_ap_real_text(self) -> str:
        """Docstring: Getter for ap_real_text variable"""
        return self.__ap_real_text

    def get_ap_find_text(self) -> WebElement:
        """Docstring: Getter for ap_find_text webElement"""
        return self.__ap_find_text

    # Methods:
    def ap_click_game_menu_item(self) -> None:
        """Docstring: Method to click GAME menu item on the ABOUT page"""
        return self.__ap_game_menu_item.click()

    def ap_click_rules_menu_item(self) -> None:
        """Docstring: Method to click RULES menu item on the ABOUT page"""
        return self.__ap_rules_menu_item.click()
