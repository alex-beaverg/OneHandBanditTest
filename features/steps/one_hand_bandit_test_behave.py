# Tests with behave module can be run from command-line:
#   Run with all feature files:
#       behave -i .feature
#   Run only with chrome.feature file:
#       behave -i chrome.feature
#   Run only with edge.feature file:
#       behave -i edge.feature
#   Run only with firefox.feature file:
#       behave -i firefox.feature
# Command-line argument "-i" - only run feature files matching regular expression pattern

# Tests with behave module with beautiful allure report can be run from command-line:
#   Run tests with output JSON report files in "test-allure-behave-reports" folder:
#       With all feature files:
#           behave -f allure_behave.formatter:AllureFormatter -o test-allure-behave-reports -i .feature
#       With chrome.feature file:
#           behave -f allure_behave.formatter:AllureFormatter -o test-allure-behave-reports -i chrome.feature
#       With edge.feature file:
#           behave -f allure_behave.formatter:AllureFormatter -o test-allure-behave-reports -i edge.feature
#       With firefox.feature file:
#           behave -f allure_behave.formatter:AllureFormatter -o test-allure-behave-reports -i firefox.feature
#   Show beautiful allure report:
#       allure serve test-allure-behave-reports
# Command-line argument "-f" - formatter
# Command-line argument "-o" - the directory to generate Allure report into
# Command-line argument "-i" - only run feature files matching regular expression pattern

from behave import *
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import waiters


@given('website "{url}" with "{brows}" browser')
def step(context: webdriver, url: str, brows: str) -> None:
    f"""Docstring: Given website {url} with "{brows}" browser"""
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


@when('you open the game page with text "{text}"')
def step(context: webdriver, text: str) -> None:
    f"""Docstring: When you open the game page with text '{text}'"""
    # Synchronisation utilit
    waiters.wait_until_page_loaded(context, '//*[contains(text(), "%s")]', text)


@then('you see the page including text "{text}"')
def step(context: webdriver, text: str) -> None:
    f"""Docstring: Then you see the page including text '{text}'"""
    # We have to find unique for this page text
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "%s")]' % text)


@when('you click "PLAY" button')
def step(context: webdriver) -> None:
    """Docstring: When you click "PLAY" button"""
    # We have to click 'PLAY' button to start game
    context.browser.find_element(By.ID, 'btn').click()


@then('the game can be played')
def step(context: webdriver) -> None:
    """Docstring: Then the game can be played"""
    # We have to find unique for this page text
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "Moves:")]')


@when('the game is won')
def step(context: webdriver) -> None:
    """Docstring: When the game is won"""
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
    """Docstring: Then you can see your results"""
    # We have to find unique for this page text
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "1st game")]')


@when('you click "PLAY AGAIN" button')
def step(context: webdriver) -> None:
    """Docstring: When you click "PLAY AGAIN" button"""
    # We have to click 'PLAY AGAIN' button to start next game
    play = context.browser.find_element(By.ID, 'btn')
    play.click()


@then('you can play again')
def step(context: webdriver) -> None:
    """Docstring: Then you can play again"""
    # We have to click until we win
    play = context.browser.find_element(By.ID, 'btn')
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
    """Docstring: And you can see your next results"""
    # We have to check victory in the second game
    # We have to find unique text for this case
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "2nd game")]')


@when('you click "DELETE RESULT" button')
def step(context: webdriver) -> None:
    """Docstring: When you click "DELETE RESULT" button"""
    # We have to find 'DELETE RESULTS' button and have to click it
    context.browser.find_element(By.ID, 'reload').click()


@then('you can\'t see results')
def step(context: webdriver) -> None:
    """Docstring: Then you can't see results"""
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


@when('you click "RULES" button')
def step(context: webdriver) -> None:
    """Docstring: When you click "RULES" button"""
    # We have to open 'RULES' page
    context.browser.find_element(By.XPATH, '//*[contains(text(), "RULES")]').click()


@then('you can read the rules of the game')
def step(context: webdriver) -> None:
    """Docstring: Then you can read the rules of the game"""
    # We have to find unique text for this case
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "That\'s all. Good Luck!")]')


@when('you click "START GAME" button')
def step(context: webdriver) -> None:
    """Docstring: When you click "START GAME" button"""
    # We have to open main page to click 'START GAME' button
    context.browser.find_element(By.XPATH, '//*[contains(@value, "START")]').click()


@then('you can see game page')
def step(context: webdriver) -> None:
    """Docstring: Then you can see game page"""
    # We have to find unique for this page text
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "Good Luck, My Friend!")]')


@when('you click "ABOUT" button')
def step(context: webdriver) -> None:
    """Docstring: When you click "ABOUT" button"""
    # We have to open 'ABOUT' page
    context.browser.find_element(By.XPATH, '//*[contains(text(), "ABOUT")]').click()


@then('you can read "ABOUT" page')
def step(context: webdriver) -> None:
    """Docstring: Then you can read "ABOUT" page"""
    # We have to find unique for this page text
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "Alexey Bobrikov")]')


@when('you click "GAME" button')
def step(context: webdriver) -> None:
    """Docstring: When you click "GAME" button"""
    # We have to open main page to click 'GAME' in menu bar
    context.browser.find_element(By.XPATH, '//*[contains(text(), "GAME")]').click()


@then('you can return to the home page')
def step(context: webdriver) -> None:
    """Docstring: Then you can return to the home page"""
    # We have to find unique for this page text
    assert context.browser.find_element(By.XPATH, '//*[contains(text(), "Good Luck, My Friend!")]')
    # We have to close webdriver
    context.browser.quit()
