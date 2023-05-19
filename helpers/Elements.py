import configparser

from selenium.webdriver.common.by import By

from helpers.WebDriver import WebDriver


class Elements:
    """Docstring: class Elements"""
    driver = WebDriver()
    config = configparser.RawConfigParser()
    config.read('resources/elements.properties')

    @staticmethod
    def get_element(section: str, name: str):
        """Docstring: Static method to get element"""
        locator = Elements.config.get(section, name)
        result_lst = locator.split('=', 2)
        locator_type = result_lst[0]
        selector = result_lst[1]
        match locator_type:
            case 'id':
                return Elements.driver.find_element(By.ID, selector)
            case 'name':
                return Elements.driver.find_element(By.NAME, selector)
            case 'class_name':
                return Elements.driver.find_element(By.CLASS_NAME, selector)
            case 'tag_name':
                return Elements.driver.find_element(By.TAG_NAME, selector)
            case 'link_text':
                return Elements.driver.find_element(By.LINK_TEXT, selector)
            case 'partial_link_text':
                return Elements.driver.find_element(By.PARTIAL_LINK_TEXT, selector)
            case 'css_selector':
                return Elements.driver.find_element(By.CSS_SELECTOR, selector)
            case 'xpath':
                return Elements.driver.find_element(By.XPATH, selector)
            case _:
                raise RuntimeError("No such locator type")

    @staticmethod
    def get_element_with_text(section: str, name: str, text: str):
        """Docstring: Static method to get element with text"""
        locator = Elements.config.get(section, name)
        result_lst = locator.split('=', 2)
        locator_type = result_lst[0]
        selector = result_lst[1]
        match locator_type:
            case 'id':
                return Elements.driver.find_element(By.ID, selector.replace('{x}', text))
            case 'name':
                return Elements.driver.find_element(By.NAME, selector.replace('{x}', text))
            case 'class_name':
                return Elements.driver.find_element(By.CLASS_NAME, selector.replace('{x}', text))
            case 'tag_name':
                return Elements.driver.find_element(By.TAG_NAME, selector.replace('{x}', text))
            case 'link_text':
                return Elements.driver.find_element(By.LINK_TEXT, selector.replace('{x}', text))
            case 'partial_link_text':
                return Elements.driver.find_element(By.PARTIAL_LINK_TEXT, selector.replace('{x}', text))
            case 'css_selector':
                return Elements.driver.find_element(By.CSS_SELECTOR, selector.replace('{x}', text))
            case 'xpath':
                return Elements.driver.find_element(By.XPATH, selector.replace('{x}', text))
            case _:
                raise RuntimeError("No such locator type")