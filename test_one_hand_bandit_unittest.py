# Tests with unittest module can be run from command-line:
#   Run tests without details:
#       python -m unittest
#   Run tests with more details (command-line argument "-v"):
#       python -m unittest -v
#   Run tests with output XML report file in "test-xmlrunner-reports" folder:
#       python -m test_one_hand_bandit_unittest
#       python test_one_hand_bandit_unittest.py
# Command-line argument "-m" - run only test files

# Tests with unittest module also can be run in IDE (with integrated report):
#   Click "Run" button
#   Press "Shift + F10"

# Tests with unittest module (as pytest for beautiful allure report) can be run from command-line:
#   Run tests with output JSON report files in "test-allure-reports" folder:
#       python -m pytest test_one_hand_bandit_unittest.py --alluredir test-allure-reports -s
#   Show beautiful allure report:
#       allure serve test-allure-reports
# Command-line argument "--alluredir" - folder for JSON report files
# Command-line argument "-s" - disable all output capturing from the command-line (otherwise there will be an OSError)

import unittest
import allure

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


@allure.story('One Hand Bandit game tests')
@allure.feature('All step by step tests')
@allure.testcase('Open and check all pages of the game')
class TestCaseAllStepByStepTests(unittest.TestCase):
    driver = None

    @classmethod
    @allure.step('Set Up Test Case method (Before tests)')
    def setUpClass(cls):
        """Docstring: Set Up Test Case method (Before tests)"""
        # We have to choose browser (webdriver) in cmd-line
        print('Enter browser for testing (F[firefox]/C[chrome]/E[edge]): ', end='')
        driver_name = input()
        print(f'Run for {"Firefox" if driver_name == "F" else ("Chrome" if driver_name == "C" else "Edge")} browser')
        match driver_name:
            case 'F':
                cls.driver = webdriver.Firefox()
            case 'C':
                cls.driver = webdriver.Chrome()
            case 'E':
                cls.driver = webdriver.Edge()
            case _:
                cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        # We have to get URL to webdriver
        cls.driver.get('https://one-hand-bandit.vercel.app/')
        cls.play = cls.driver.find_element(By.ID, 'btn')

    @classmethod
    @allure.step('Tear Down Test Case method (After tests)')
    def tearDownClass(cls):
        """Docstring: Tear Down Test Case method (After tests)"""
        # We have to close webdriver
        cls.driver.close()

    @allure.step('Test 01. Testing opening home page')
    def test_01_open_home_page(self) -> None:
        """Docstring: Testing opening home page"""
        # We have to find unique for this page text
        result = self.driver.find_element(By.ID, 'wish').text
        self.assertEqual('Good Luck, My Friend!', result)

    @allure.step('Test 02. Testing playing game to first win')
    def test_02_play_1_game(self) -> None:
        """Docstring: Testing playing game to first win"""
        # We have to click 'PLAY' button to start game
        self.play.click()
        # We have to click until we win
        while True:
            try:
                # We have to find unique text for this page or will catch exception
                self.driver.find_element(By.XPATH, '//*[contains(text(), "You WON!")]')
            except NoSuchElementException:
                # If we caught exception, we have to click 'NEXT MOVE' button
                self.play.click()
            else:
                # If we didn't catch exception, test passed
                self.assertTrue(True)
                break

    @allure.step('Test 03. Testing finding results of first game')
    def test_03_results_1_game(self) -> None:
        """Docstring: Testing finding results of first game"""
        # We have to check victory in the first game
        # We have to find unique text for this case
        self.assertTrue(self.driver.find_element(By.XPATH, '//*[contains(text(), "1st game")]'))

    @allure.step('Test 04. Testing playing game to second win')
    def test_04_play_2_game(self) -> None:
        """Docstring: Testing playing game to second win"""
        # We have to click 'PLAY AGAIN' button to start second game
        self.play.click()
        # We have to click until we win
        while True:
            try:
                # We have to find unique text for this page or will catch exception
                self.driver.find_element(By.XPATH, '//*[contains(text(), "You WON!")]')
            except NoSuchElementException:
                # If we caught exception, we have to click 'NEXT MOVE' button
                self.play.click()
            else:
                # If we didn't catch exception, test passed
                self.assertTrue(True)
                break

    @allure.step('Test 05. Testing finding results of second game')
    def test_05_results_2_game(self) -> None:
        """Docstring: Testing finding results of second game"""
        # We have to check victory in the second game
        # We have to find unique text for this case
        self.assertTrue(self.driver.find_element(By.XPATH, '//*[contains(text(), "2nd game")]'))

    @allure.step('Test 06. Testing playing game to third win')
    def test_06_play_3_game(self) -> None:
        """Docstring: Testing playing game to third win"""
        # We have to click 'PLAY AGAIN' button to start third game
        self.play.click()
        # We have to click until we win
        while True:
            try:
                # We have to find unique text for this page or will catch exception
                self.driver.find_element(By.XPATH, '//*[contains(text(), "You WON!")]')
            except NoSuchElementException:
                # If we caught exception, we have to click 'NEXT MOVE' button
                self.play.click()
            else:
                # If we didn't catch exception, test passed
                self.assertTrue(True)
                break

    @allure.step('Test 07. Testing finding results of third game')
    def test_07_results_3_game(self) -> None:
        """Docstring: Testing finding results of third game"""
        # We have to check victory in the third game
        # We have to find unique text for this case
        self.assertTrue(self.driver.find_element(By.XPATH, '//*[contains(text(), "3rd game")]'))

    @allure.step('Test 08. Testing deleting results')
    def test_08_delete_results(self) -> None:
        """Docstring: Testing deleting results"""
        # We have to find 'DELETE RESULTS' button and have to click it
        self.driver.find_element(By.ID, 'reload').click()
        # We need exception for passing test
        try:
            # We haven't to find 'DELETE RESULTS' button (will be exception)
            self.driver.find_element(By.ID, 'reload')
        except NoSuchElementException:
            # if we caught exception, 'DELETE RESULTS' button wasn't find
            # Test passed
            self.assertTrue(True)
        else:
            # If we didn't catch exception, test failed
            # We raise exception
            raise AssertionError

    @allure.step('Test 09. Testing opening RULES page')
    def test_09_open_rules_page(self) -> None:
        """Docstring: Testing opening RULES page"""
        # We have to open 'RULES' page
        self.driver.find_element(By.XPATH, '//*[contains(text(), "RULES")]').click()
        # We have to find unique text for this case
        self.assertEqual(self.driver.find_element(By.TAG_NAME, 'h1').text[:9], 'The rules')

    @allure.step('Test 10. Testing button "START GAME"')
    def test_10_check_btn_start_game(self) -> None:
        """Docstring: Testing button 'START GAME'"""
        # We have to open main page to click 'START GAME' button
        self.driver.find_element(By.XPATH, '//*[contains(@value, "START GAME")]').click()
        # We have to find unique for this page text
        result = self.driver.find_element(By.ID, 'wish').text
        self.assertEqual('Good Luck, My Friend!', result)

    @allure.step('Test 11. Testing opening ABOUT page')
    def test_11_open_page_about(self) -> None:
        """Docstring: Testing opening ABOUT page"""
        # We have to open 'ABOUT' page
        self.driver.find_element(By.XPATH, '//*[contains(text(), "ABOUT")]').click()
        # We have to find unique for this page text
        self.assertTrue(self.driver.find_element(By.XPATH, '//*[contains(text(), "Alexey Bobrikov")]'))

    @allure.step('Test 12. Testing returning to the home page')
    def test_12_return_home_page(self) -> None:
        """Docstring: Testing returning to the home page"""
        # We have to open main page to click 'GAME' in menu bar
        self.driver.find_element(By.XPATH, '//*[contains(text(), "GAME")]').click()
        # We have to find unique for this page text
        result = self.driver.find_element(By.ID, 'wish').text
        self.assertEqual('Good Luck, My Friend!', result)


if __name__ == '__main__':
    import xmlrunner

    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-xmlrunner-reports'),
        failfast=False,
        buffer=False,
        catchbreak=False)
