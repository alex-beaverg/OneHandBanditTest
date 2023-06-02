from selenium.webdriver.common.by import By


class BasePageLocators:
    """Docstring: Class BasePageLocators"""
    GAME_MENU_ITEM = (By.XPATH, "//*[contains(text(), 'GAME')]")
    RULES_MENU_ITEM = (By.XPATH, "//*[contains(text(), 'RULES')]")
    ABOUT_MENU_ITEM = (By.XPATH, "//*[contains(text(), 'ABOUT')]")


class HomePageLocators:
    """Docstring: Class HomePageLocators"""
    PLAY_BUTTON = (By.ID, "btn")
    FIND_TEXT = (By.ID, "wish")
    DELETE_RESULT_BUTTON = (By.ID, "reload")
    TEXT_AFTER_CLICK = (By.ID, "win")
    FIND_GAME_RESULT = (By.XPATH, "//*[contains(text(), '{x}')]")
    FIND_SRC_IN_CELLS = (By.ID, "cell-{x}")


class RulesPageLocators:
    """Docstring: Class RulesPageLocators"""
    START_GAME_BUTTON = (By.XPATH, "//*[contains(@value, 'START GAME')]")
    FIND_TEXT = (By.TAG_NAME, "h1")


class AboutPageLocators:
    """Docstring: Class AboutPageLocators"""
    FIND_TEXT = (By.TAG_NAME, "h1")
