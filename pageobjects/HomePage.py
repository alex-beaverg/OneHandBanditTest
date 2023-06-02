from selenium.webdriver.remote.webelement import WebElement

from helpers.Locators import HomePageLocators
from pageobjects.BasePage import BasePage


class HomePage(BasePage):
    """Docstring: Class HomePage extends BasePage"""

    def __init__(self, driver) -> None:
        """Docstring: Constructor for class HomePage"""
        super().__init__(driver)
        self.__hp_play_button = driver.find_element(*HomePageLocators.PLAY_BUTTON)
        self.__hp_real_text = 'Good Luck, My Friend!'
        self.__hp_find_text = driver.find_element(*HomePageLocators.FIND_TEXT).text
        self.__hp_real_first_game_result = '1st game'
        self.__hp_real_second_game_result = '2nd game'
        self.__hp_real_third_game_result = '3rd game'
        self.__hp_find_any_game_result = None
        self.__hp_delete_result_button = None
        self.__hp_real_src_in_cells = 'https://one-hand-bandit.vercel.app/images/item05.png'
        self.__hp_find_src_in_cells = None

    # Getters:
    def get_hp_real_text(self) -> str:
        """Docstring: Getter for hp_real_text variable"""
        return self.__hp_real_text

    def get_hp_find_text(self) -> str:
        """Docstring: Getter for hp_find_text variable"""
        return self.__hp_find_text

    def get_hp_real_first_game_result(self) -> str:
        """Docstring: Getter for hp_real_first_game_result variable"""
        return self.__hp_real_first_game_result

    def get_hp_real_second_game_result(self) -> str:
        """Docstring: Getter for hp_real_second_game_result variable"""
        return self.__hp_real_second_game_result

    def get_hp_real_third_game_result(self) -> str:
        """Docstring: Getter for hp_real_third_game_result variable"""
        return self.__hp_real_third_game_result

    def get_hp_game_result(self) -> WebElement:
        """Docstring: Getter for hp_game_result webElement"""
        return self.__hp_find_any_game_result

    def get_hp_find_src_in_cells(self) -> list:
        """Docstring: Getter for hp_find_src_in_cells list"""
        return self.__hp_find_src_in_cells

    def get_hp_real_src_in_cells(self) -> list:
        """Docstring: Getter for hp_real_src_in_cells list"""
        return [self.__hp_real_src_in_cells] * 5

    # Methods:
    def __hp_click_play_button(self) -> None:
        """Docstring: Private method to click PLAY button on the HOME page"""
        return self.__hp_play_button.click()

    def hp_play_game(self, find_text: str) -> None:
        """Docstring: Method to play game until you win on the HOME page"""
        self.__hp_click_play_button()
        while True:
            text_after_click = self.__driver.find_element(*HomePageLocators.TEXT_AFTER_CLICK).text
            if 'You WON!' in text_after_click:
                self.__hp_find_any_game_result = self.__driver\
                    .find_element(HomePageLocators.FIND_GAME_RESULT[0],
                                  HomePageLocators.FIND_GAME_RESULT[1].replace('{x}', find_text))
                return
            else:
                self.__hp_click_play_button()

    def hp_delete_result(self) -> None:
        """Docstring: Method to click DELETE RESULTS button on the HOME page"""
        self.__hp_delete_result_button = self.__driver.find_element(*HomePageLocators.DELETE_RESULT_BUTTON)
        self.__hp_delete_result_button.click()
        self.__hp_find_src_in_cells = [
            self.__driver
            .find_element(HomePageLocators.FIND_SRC_IN_CELLS[0],
                          HomePageLocators.FIND_SRC_IN_CELLS[1].replace('{x}', str(i))).get_attribute('src')
            for i in range(1, 6)
        ]
