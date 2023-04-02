from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_until_page_loaded(context: webdriver, xpath: str, text: str) -> None:
    WebDriverWait(context.browser, 120).until(
            EC.presence_of_element_located((By.XPATH, xpath % text))
    )
