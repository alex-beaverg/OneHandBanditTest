from helpers.Locators import BasePageLocators


class BasePage:
    """Docstring: Parent class BasePage"""

    def __init__(self, driver) -> None:
        """Docstring: Constructor for class BasePage"""
        self._driver = driver
        self.__game_menu_item = driver.find_element(*BasePageLocators.GAME_MENU_ITEM)
        self.__rules_menu_item = driver.find_element(*BasePageLocators.RULES_MENU_ITEM)
        self.__about_menu_item = driver.find_element(*BasePageLocators.ABOUT_MENU_ITEM)

    def click_game_menu_item(self) -> None:
        """Docstring: Method to click GAME menu item"""
        return self.__game_menu_item.click()

    def click_rules_menu_item(self) -> None:
        """Docstring: Method to click RULES menu item"""
        return self.__rules_menu_item.click()

    def click_about_menu_item(self) -> None:
        """Docstring: Method to click ABOUT menu item on the HOME page"""
        return self.__about_menu_item.click()
