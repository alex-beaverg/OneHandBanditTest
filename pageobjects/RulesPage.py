from selenium.webdriver.common.by import By


class RulesPage:
    """Docstring: Class pageobjects.RulesPage"""
    def __init__(self, driver) -> None:
        """Docstring: Constructor for class pageobjects.RulesPage"""
        self.driver = driver
        # Webelements and variables:
        self.rp_start_game_button = self.driver.find_element(By.XPATH, '//*[contains(@value, "START GAME")]')
        self.rp_game_menu_item = self.driver.find_element(By.XPATH, '//*[contains(text(), "GAME")]')
        self.rp_about_menu_item = self.driver.find_element(By.XPATH, '//*[contains(text(), "ABOUT")]')
        self.rp_real_text = 'The rules'
        self.rp_find_text = self.driver.find_element(By.TAG_NAME, 'h1').text[:9]

    def rp_click_start_game_button(self) -> None:
        """Docstring: Method to click START GAME button on the RULES page"""
        return self.rp_start_game_button.click()

    def rp_click_game_menu_item(self) -> None:
        """Docstring: Method to click GAME menu item on the RULES page"""
        return self.rp_game_menu_item.click()

    def rp_click_about_menu_item(self) -> None:
        """Docstring: Method to click ABOUT menu item on the RULES page"""
        return self.rp_about_menu_item.click()
