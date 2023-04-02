from behave import *
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import waiters


@given('website "{url}" with "{brows}" browser')
def step(context: webdriver, url: str, brows: str) -> None:
    # Run webdriver
    if brows == 'edge':
        context.browser = webdriver.Edge()
    elif brows == 'chrome':
        context.browser = webdriver.Chrome()
    elif brows == 'firefox':
        context.browser = webdriver.Firefox()
    # Maximize window
    context.browser.maximize_window()
    # Open page with getting URL
    context.browser.get(url)


@then('index page include text "{text}"')
def step(context: webdriver, text: str) -> None:
    # Synchronisation
    waiters.wait_until_page_loaded(context, '//*[contains(text(), "%s")]', text)
    # Check if the page was opened
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "%s")]' % text)


@then('the game can be played')
def step(context: webdriver) -> None:
    # Click the button to play the game
    context.browser.find_element(By.XPATH, '//*[@id="btn"]').click()
    # Check if the button was clicked
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "Moves:")]')


@then('the game can be won')
def step(context: webdriver) -> None:
    # Play the game to win
    while True:
        try:
            # Check if the game was won
            context.browser.find_element(By.XPATH, '//*[contains(text(), "You WON")]')
        except NoSuchElementException:
            # Do next move if the game wasn't won
            context.browser.find_element(By.XPATH, '//*[@id="btn"]').click()
        else:
            # Exit when the game was won
            break


@then('you can see your results')
def step(context: webdriver) -> None:
    # Check if result string exists
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "1st game")]')


@then('you can play again')
def step(context: webdriver) -> None:
    # Play the game to win again
    play = context.browser.find_element(By.XPATH, '//*[@id="btn"]')
    play.click()
    while True:
        try:
            # Check if the game was won
            context.browser.find_element(By.XPATH, '//*[contains(text(), "You WON")]')
        except NoSuchElementException:
            # Do next move if the game wasn't won
            play.click()
        else:
            # Exit when the game was won
            break


@then('you can see your next results')
def step(context: webdriver) -> None:
    # Check if result string exists
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "2nd game")]')


@then('you can delete your results')
def step(context: webdriver) -> None:
    # Delete result
    context.browser.find_element(By.XPATH, '//*[@id="reload"]').click()
    try:
        # Check if the button "DELETE" exists
        context.browser.find_element(By.XPATH, '//*[@id="reload"]')
    except NoSuchElementException:
        # Pass if the button "DELETE" wasn't found
        pass
    else:
        # Fail if the button "DELETE" was found
        raise AssertionError


@then('you can read the rules of the game')
def step(context: webdriver) -> None:
    # Click the button "RULES"
    context.browser.find_element(By.XPATH, '//*[contains(text(), "RULES")]').click()
    # Check if the button was clicked
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "That\'s all. Good Luck!")]')


@then('you can click to "START GAME" button')
def step(context: webdriver) -> None:
    # Click the button "START GAME"
    context.browser.find_element(By.XPATH, '//*[contains(@value, "START")]').click()
    # Check if the button was clicked
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "Good Luck, My Friend!")]')


@then('you can read "ABOUT" page')
def step(context: webdriver) -> None:
    # Click the button "ABOUT"
    context.browser.find_element(By.XPATH, '//*[contains(text(), "ABOUT")]').click()
    # Check if the button was clicked
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "Alexey Bobrikov")]')


@then('you can return to the home page')
def step(context: webdriver) -> None:
    # Click the button "GAME"
    context.browser.find_element(By.XPATH, '//*[contains(text(), "GAME")]').click()
    # Check if the button was clicked
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "Good Luck, My Friend!")]')
    # Close webdriver
    context.browser.quit()
