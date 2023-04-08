# RUN WITH CMD:         python -m unittest
# FOR MORE DETAILS:     python -m unittest -v
# FOR XML REPORT:       python -m test_one_hand_bandit_unittest

import unittest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class AllStepByStepTests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        """Set Up Test Case method (Before tests)"""
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
        cls.driver.get('https://one-hand-bandit.vercel.app/')
        cls.play = cls.driver.find_element(By.ID, 'btn')

    @classmethod
    def tearDownClass(cls):
        """Tear Down Test Case method (After tests)"""
        cls.driver.close()

    def test_01_open_home_page(self) -> None:
        """Testing opening home page"""
        # We have to find unique for this page text
        result = self.driver.find_element(By.ID, 'wish').text
        self.assertEqual('Good Luck, My Friend!', result)

    def test_02_play_1_game(self) -> None:
        """Testing playing game to first win"""
        # We have to click 'PLAY' button to start game
        self.play.click()
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

    def test_03_results_1_game(self) -> None:
        """Testing finding results of first game"""
        # We have to check victory in the first game
        # We have to find unique text for this case
        self.assertTrue(self.driver.find_element(By.XPATH, '//*[contains(text(), "1st game")]'))

    def test_04_play_2_game(self) -> None:
        """Testing playing game to second win"""
        # We have to click 'PLAY AGAIN' button to start second game
        self.play.click()
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

    def test_05_results_2_game(self) -> None:
        """Testing finding results of second game"""
        # We have to check victory in the second game
        # We have to find unique text for this case
        self.assertTrue(self.driver.find_element(By.XPATH, '//*[contains(text(), "2nd game")]'))

    def test_06_play_3_game(self) -> None:
        """Testing playing game to third win"""
        # We have to click 'PLAY AGAIN' button to start third game
        self.play.click()
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

    def test_07_results_3_game(self) -> None:
        """Testing finding results of third game"""
        # We have to check victory in the third game
        # We have to find unique text for this case
        self.assertTrue(self.driver.find_element(By.XPATH, '//*[contains(text(), "3rd game")]'))

    def test_08_delete_results(self) -> None:
        """Testing deleting results"""
        # We have to find 'DELETE RESULTS' button and have to click it
        self.driver.find_element(By.ID, 'reload').click()
        try:
            # We haven't to find 'DELETE RESULTS' button (will be exception)
            self.driver.find_element(By.ID, 'reload')
        except NoSuchElementException:
            # if we caught exception, 'DELETE RESULTS' button wasn't find
            # Test passed
            self.assertTrue(True)
        else:
            # If we didn't catch exception, test failed
            raise AssertionError

    def test_09_open_rules_page(self) -> None:
        """Testing opening RULES page"""
        # We have to open 'RULES' page
        self.driver.find_element(By.XPATH, '//*[contains(text(), "RULES")]').click()
        # We have to find unique text for this case
        self.assertEqual(self.driver.find_element(By.TAG_NAME, 'h1').text[:9], 'The rules')

    def test_10_check_btn_start_game(self) -> None:
        """Testing button 'START GAME'"""
        # We have to open main page to click 'START GAME' button
        self.driver.find_element(By.XPATH, '//*[contains(@value, "START GAME")]').click()
        # We have to find unique for this page text
        result = self.driver.find_element(By.ID, 'wish').text
        self.assertEqual('Good Luck, My Friend!', result)

    def test_11_open_page_about(self) -> None:
        """Testing opening ABOUT page"""
        # We have to open 'ABOUT' page
        self.driver.find_element(By.XPATH, '//*[contains(text(), "ABOUT")]').click()
        # We have to find unique for this page text
        self.assertTrue(self.driver.find_element(By.XPATH, '//*[contains(text(), "Alexey Bobrikov")]'))

    def test_12_return_home_page(self) -> None:
        """Testing returning to the home page"""
        # We have to open main page to click 'GAME' in menu bar
        self.driver.find_element(By.XPATH, '//*[contains(text(), "GAME")]').click()
        # We have to find unique for this page text
        result = self.driver.find_element(By.ID, 'wish').text
        self.assertEqual('Good Luck, My Friend!', result)


# ONLY IF RUN: python -m test_one_hand_bandit_unittest
if __name__ == '__main__':
    import xmlrunner

    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-xmlrunner-reports'),
        failfast=False,
        buffer=False,
        catchbreak=False)
