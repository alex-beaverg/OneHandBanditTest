from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class HomePage:
    """Docstring: Class pageobjects.HomePage"""
    def __init__(self, driver) -> None:
        """Docstring: Constructor for class pageobjects.HomePage"""
        self.driver = driver
        # Webelements and variables:
        self.hp_play_button = self.driver.find_element(By.ID, 'btn')
        self.hp_rules_menu_item = self.driver.find_element(By.XPATH, '//*[contains(text(), "RULES")]')
        self.hp_about_menu_item = self.driver.find_element(By.XPATH, '//*[contains(text(), "ABOUT")]')
        self.hp_real_text = 'Good Luck, My Friend!'
        self.hp_find_text = self.driver.find_element(By.ID, 'wish').text
        self.hp_game_result = None
        self.hp_delete_result_button = None

    def hp_click_play_button(self) -> None:
        """Docstring: Method to click PLAY button on the HOME page"""
        return self.hp_play_button.click()

    def hp_click_rules_menu_item(self) -> None:
        """Docstring: Method to click RULES menu item on the HOME page"""
        return self.hp_rules_menu_item.click()

    def hp_click_about_menu_item(self) -> None:
        """Docstring: Method to click ABOUT menu item on the HOME page"""
        return self.hp_about_menu_item.click()

    def hp_play_game(self, find_text: str) -> None:
        """Docstring: Method to play game until you win on the HOME page"""
        self.hp_click_play_button()
        while True:
            try:
                # You have to find unique text for this page or will catch exception
                self.driver.find_element(By.XPATH, '//*[contains(text(), "You WON!")]')
            except NoSuchElementException:
                # If you caught exception, you have to click 'NEXT MOVE' button
                self.hp_click_play_button()
            else:
                # If you didn't catch exception, you won
                self.hp_game_result = self.driver.find_element(By.XPATH, f'//*[contains(text(), "{find_text}")]')
                return

    def hp_delete_result(self) -> (Exception, None):
        """Docstring: Method to click DELETE RESULTS button on the HOME page"""
        try:
            # You have to find element with ID='reload' or will catch exception
            self.hp_delete_result_button = self.driver.find_element(By.ID, 'reload')
        except NoSuchElementException:
            # If you caught exception, you have to return exception
            return NoSuchElementException
        else:
            # If you didn't catch exception, you have to click DELETE RESULTS button
            return self.hp_delete_result_button.click()
