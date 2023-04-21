from selenium.webdriver.common.by import By


class AboutPage:
    """Docstring: Class pageobjects.AboutPage"""
    def __init__(self, driver) -> None:
        """Docstring: Constructor for class pageobjects.AboutPage"""
        self.driver = driver
        # Webelements and variables:
        self.ap_game_menu_item = self.driver.find_element(By.XPATH, '//*[contains(text(), "GAME")]')
        self.ap_rules_menu_item = self.driver.find_element(By.XPATH, '//*[contains(text(), "RULES")]')
        self.ap_real_text = 'Information'
        self.ap_find_text = self.driver.find_element(By.TAG_NAME, 'h1').text[:11]

    def ap_click_game_menu_item(self) -> None:
        """Docstring: Method to click GAME menu item on the ABOUT page"""
        return self.ap_game_menu_item.click()

    def ap_click_rules_menu_item(self) -> None:
        """Docstring: Method to click RULES menu item on the ABOUT page"""
        return self.ap_rules_menu_item.click()
