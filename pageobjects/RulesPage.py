from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class RulesPage:
    """Docstring: Class pageobjects.RulesPage"""
    def __init__(self, driver) -> None:
        """Docstring: Constructor for class pageobjects.RulesPage"""
        self.__driver = driver
        # Webelements and variables:
        self.__rp_start_game_button = self.__driver.find_element(By.XPATH, '//*[contains(@value, "START GAME")]')
        self.__rp_game_menu_item = self.__driver.find_element(By.XPATH, '//*[contains(text(), "GAME")]')
        self.__rp_about_menu_item = self.__driver.find_element(By.XPATH, '//*[contains(text(), "ABOUT")]')
        self.__rp_real_text = 'The rules'
        self.__rp_find_text = self.__driver.find_element(By.TAG_NAME, 'h1').text[:9]

    # Getters:
    def get_rp_real_text(self) -> str:
        """Docstring: Getter for rp_real_text variable"""
        return self.__rp_real_text

    def get_rp_find_text(self) -> WebElement:
        """Docstring: Getter for rp_find_text webElement"""
        return self.__rp_find_text

    # Methods:
    def rp_click_start_game_button(self) -> None:
        """Docstring: Method to click START GAME button on the RULES page"""
        return self.__rp_start_game_button.click()

    def rp_click_game_menu_item(self) -> None:
        """Docstring: Method to click GAME menu item on the RULES page"""
        return self.__rp_game_menu_item.click()

    def rp_click_about_menu_item(self) -> None:
        """Docstring: Method to click ABOUT menu item on the RULES page"""
        return self.__rp_about_menu_item.click()
