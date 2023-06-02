from selenium.webdriver.common.by import By


class HomePageLocators:
    PLAY_BUTTON = (By.ID, "btn")
    RULES_MENU_ITEM = (By.XPATH, "//*[contains(text(), 'RULES')]")
    ABOUT_MENU_ITEM = (By.XPATH, "//*[contains(text(), 'ABOUT')]")
    FIND_TEXT = (By.ID, "wish")
    DELETE_RESULT_BUTTON = (By.ID, "reload")
    TEXT_AFTER_CLICK = (By.ID, "win")
    FIND_GAME_RESULT = (By.XPATH, "//*[contains(text(), '{x}')]")
    FIND_SRC_IN_CELLS = (By.ID, "cell-{x}")


class RulesPageLocators:
    START_GAME_BUTTON = (By.XPATH, "//*[contains(@value, 'START GAME')]")
    GAME_MENU_ITEM = (By.XPATH, "//*[contains(text(), 'GAME')]")
    ABOUT_MENU_ITEM = (By.XPATH, "//*[contains(text(), 'ABOUT')]")
    FIND_TEXT = (By.TAG_NAME, "h1")


class AboutPageLocators:
    GAME_MENU_ITEM = (By.XPATH, "//*[contains(text(), 'GAME')]")
    RULES_MENU_ITEM = (By.XPATH, "//*[contains(text(), 'RULES')]")
    FIND_TEXT = (By.TAG_NAME, "h1")
