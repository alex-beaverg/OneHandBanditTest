from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class HomePage:
    """Docstring: Class pageobjects.HomePage"""

    def __init__(self, driver) -> None:
        """Docstring: Constructor for class pageobjects.HomePage"""
        self.__driver = driver
        # Webelements and variables:
        self.__hp_play_button = self.__driver.find_element(By.ID, 'btn')
        self.__hp_rules_menu_item = self.__driver.find_element(By.XPATH, '//*[contains(text(), "RULES")]')
        self.__hp_about_menu_item = self.__driver.find_element(By.XPATH, '//*[contains(text(), "ABOUT")]')
        self.__hp_real_text = 'Good Luck, My Friend!'
        self.__hp_find_text = self.__driver.find_element(By.ID, 'wish').text
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

    def hp_click_rules_menu_item(self) -> None:
        """Docstring: Method to click RULES menu item on the HOME page"""
        return self.__hp_rules_menu_item.click()

    def hp_click_about_menu_item(self) -> None:
        """Docstring: Method to click ABOUT menu item on the HOME page"""
        return self.__hp_about_menu_item.click()

    def hp_play_game(self, find_text: str) -> None:
        """Docstring: Method to play game until you win on the HOME page"""
        self.__hp_click_play_button()
        while True:
            # You have to find unique field 'win' for this case
            text_after_click = self.__driver.find_element(By.ID, 'win').text
            if 'You WON!' in text_after_click:
                # If text 'You WON!' was find, you won
                self.__hp_find_any_game_result = self.__driver \
                    .find_element(By.XPATH, f'//*[contains(text(), "{find_text}")]')
                return
            else:
                # If text 'You Won!' wasn't find, you have to click 'NEXT MOVE' button
                self.__hp_click_play_button()

    def hp_delete_result(self) -> None:
        """Docstring: Method to click DELETE RESULTS button on the HOME page"""
        # You have to find element with ID='reload'
        self.__hp_delete_result_button = self.__driver.find_element(By.ID, 'reload')
        # You have to click DELETE RESULTS button
        self.__hp_delete_result_button.click()
        # Default src in cells
        self.__hp_find_src_in_cells = [
            self.__driver.find_element(By.ID, f'cell-{i}').get_attribute('src')
            for i in range(1, 6)
        ]
