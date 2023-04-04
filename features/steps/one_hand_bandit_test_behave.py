# behave -i .feature
from behave import *
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import waiters


@given('website "{url}" with "{brows}" browser')
def step(context: webdriver, url: str, brows: str) -> None:
    if brows == 'edge':
        context.browser = webdriver.Edge()
    elif brows == 'chrome':
        context.browser = webdriver.Chrome()
    elif brows == 'firefox':
        context.browser = webdriver.Firefox()
    context.browser.maximize_window()
    context.browser.get(url)


@then('index page include text "{text}"')
def step(context: webdriver, text: str) -> None:
    waiters.wait_until_page_loaded(context, '//*[contains(text(), "%s")]', text)
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "%s")]' % text)


@then('the game can be played')
def step(context: webdriver) -> None:
    context.browser.find_element(By.ID, 'btn').click()
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "Moves:")]')


@then('the game can be won')
def step(context: webdriver) -> None:
    while True:
        try:
            context.browser.find_element(By.XPATH, '//*[contains(text(), "You WON")]')
        except NoSuchElementException:
            context.browser.find_element(By.ID, 'btn').click()
        else:
            break


@then('you can see your results')
def step(context: webdriver) -> None:
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "1st game")]')


@then('you can play again')
def step(context: webdriver) -> None:
    play = context.browser.find_element(By.ID, 'btn')
    play.click()
    while True:
        try:
            context.browser.find_element(By.XPATH, '//*[contains(text(), "You WON")]')
        except NoSuchElementException:
            play.click()
        else:
            break


@then('you can see your next results')
def step(context: webdriver) -> None:
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "2nd game")]')


@then('you can delete your results')
def step(context: webdriver) -> None:
    context.browser.find_element(By.ID, 'reload').click()
    try:
        context.browser.find_element(By.ID, 'reload')
    except NoSuchElementException:
        pass
    else:
        raise AssertionError


@then('you can read the rules of the game')
def step(context: webdriver) -> None:
    context.browser.find_element(By.XPATH, '//*[contains(text(), "RULES")]').click()
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "That\'s all. Good Luck!")]')


@then('you can click to "START GAME" button')
def step(context: webdriver) -> None:
    context.browser.find_element(By.XPATH, '//*[contains(@value, "START")]').click()
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "Good Luck, My Friend!")]')


@then('you can read "ABOUT" page')
def step(context: webdriver) -> None:
    context.browser.find_element(By.XPATH, '//*[contains(text(), "ABOUT")]').click()
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "Alexey Bobrikov")]')


@then('you can return to the home page')
def step(context: webdriver) -> None:
    context.browser.find_element(By.XPATH, '//*[contains(text(), "GAME")]').click()
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "Good Luck, My Friend!")]')
    context.browser.quit()
