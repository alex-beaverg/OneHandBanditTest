# behave -i .feature
# behave -i chrome.feature
# behave -i edge.feature
# behave -i firefox.feature
from behave import *
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import waiters


@given('website "{url}" with "{brows}" browser')
def step(context: webdriver, url: str, brows: str) -> None:
    # We have to choose browser (webdriver) in cmd-line
    if brows == 'edge':
        context.browser = webdriver.Edge()
    elif brows == 'chrome':
        context.browser = webdriver.Chrome()
    elif brows == 'firefox':
        context.browser = webdriver.Firefox()
    context.browser.maximize_window()
    # We have to get URL to webdriver
    context.browser.get(url)


@then('index page include text "{text}"')
def step(context: webdriver, text: str) -> None:
    # Synchronisation utilit
    waiters.wait_until_page_loaded(context, '//*[contains(text(), "%s")]', text)
    # We have to find unique for this page text
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "%s")]' % text)


@then('the game can be played')
def step(context: webdriver) -> None:
    # We have to click 'PLAY' button to start game
    context.browser.find_element(By.ID, 'btn').click()
    # We have to find unique for this page text
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "Moves:")]')


@then('the game can be won')
def step(context: webdriver) -> None:
    # We have to click until we win
    while True:
        try:
            # We have to find unique text for this page or will catch exception
            context.browser.find_element(By.XPATH, '//*[contains(text(), "You WON")]')
        except NoSuchElementException:
            # If we caught exception, we have to click 'NEXT MOVE' button
            context.browser.find_element(By.ID, 'btn').click()
        else:
            # If we didn't catch exception, test passed
            break


@then('you can see your results')
def step(context: webdriver) -> None:
    # We have to find unique for this page text
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "1st game")]')


@then('you can play again')
def step(context: webdriver) -> None:
    # We have to click 'PLAY AGAIN' button to start next game
    play = context.browser.find_element(By.ID, 'btn')
    play.click()
    # We have to click until we win
    while True:
        try:
            # We have to find unique text for this page or will catch exception
            context.browser.find_element(By.XPATH, '//*[contains(text(), "You WON")]')
        except NoSuchElementException:
            # If we caught exception, we have to click 'NEXT MOVE' button
            play.click()
        else:
            # If we didn't catch exception, test passed
            break


@then('you can see your next results')
def step(context: webdriver) -> None:
    # We have to check victory in the second game
    # We have to find unique text for this case
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "2nd game")]')


@then('you can delete your results')
def step(context: webdriver) -> None:
    # We have to find 'DELETE RESULTS' button and have to click it
    context.browser.find_element(By.ID, 'reload').click()
    # We need exception for passing test
    try:
        # We haven't to find 'DELETE RESULTS' button (will be exception)
        context.browser.find_element(By.ID, 'reload')
    except NoSuchElementException:
        # if we caught exception, 'DELETE RESULTS' button wasn't find
        # Test passed
        pass
    else:
        # If we didn't catch exception, test failed
        # We raise exception
        raise AssertionError


@then('you can read the rules of the game')
def step(context: webdriver) -> None:
    # We have to open 'RULES' page
    context.browser.find_element(By.XPATH, '//*[contains(text(), "RULES")]').click()
    # We have to find unique text for this case
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "That\'s all. Good Luck!")]')


@then('you can click to "START GAME" button')
def step(context: webdriver) -> None:
    # We have to open main page to click 'START GAME' button
    context.browser.find_element(By.XPATH, '//*[contains(@value, "START")]').click()
    # We have to find unique for this page text
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "Good Luck, My Friend!")]')


@then('you can read "ABOUT" page')
def step(context: webdriver) -> None:
    # We have to open 'ABOUT' page
    context.browser.find_element(By.XPATH, '//*[contains(text(), "ABOUT")]').click()
    # We have to find unique for this page text
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "Alexey Bobrikov")]')


@then('you can return to the home page')
def step(context: webdriver) -> None:
    # We have to open main page to click 'GAME' in menu bar
    context.browser.find_element(By.XPATH, '//*[contains(text(), "GAME")]').click()
    # We have to find unique for this page text
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "Good Luck, My Friend!")]')
    # We have to close webdriver
    context.browser.quit()
