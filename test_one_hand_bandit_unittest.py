# python -m unittest discover -v .
import unittest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class TestOneHandBanditFirefox(unittest.TestCase):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('https://one-hand-bandit.vercel.app/')
    play = driver.find_element(By.ID, 'btn')

    def test_01_open_home_page(self) -> None:
        """Testing opening home page"""
        result = self.driver.find_element(By.ID, 'wish').text
        self.assertEqual('Good Luck, My Friend!', result)

    def test_02_play_1_game(self) -> None:
        """Testing playing game to first win"""
        self.play.click()
        while True:
            try:
                self.driver.find_element(By.XPATH, '//*[contains(text(), "You WON!")]')
            except NoSuchElementException:
                self.play.click()
            else:
                self.assertTrue(True)
                break

    def test_03_results_1_game(self) -> None:
        """Testing finding results of first game"""
        self.assertTrue(self.driver.find_element(By.XPATH, '//*[contains(text(), "1st game")]'))

    def test_04_play_2_game(self) -> None:
        """Testing playing game to second win"""
        self.play.click()
        while True:
            try:
                self.driver.find_element(By.XPATH, '//*[contains(text(), "You WON!")]')
            except NoSuchElementException:
                self.play.click()
            else:
                self.assertTrue(True)
                break

    def test_05_results_2_game(self) -> None:
        """Testing finding results of second game"""
        self.assertTrue(self.driver.find_element(By.XPATH, '//*[contains(text(), "2nd game")]'))

    def test_06_play_3_game(self) -> None:
        """Testing playing game to third win"""
        self.play.click()
        while True:
            try:
                self.driver.find_element(By.XPATH, '//*[contains(text(), "You WON!")]')
            except NoSuchElementException:
                self.play.click()
            else:
                self.assertTrue(True)
                break

    def test_07_results_3_game(self) -> None:
        """Testing finding results of third game"""
        self.assertTrue(self.driver.find_element(By.XPATH, '//*[contains(text(), "3rd game")]'))

    def test_08_delete_results(self) -> None:
        """Testing deleting results"""
        self.driver.find_element(By.ID, 'reload').click()
        try:
            self.driver.find_element(By.ID, 'reload')
        except NoSuchElementException:
            self.assertTrue(True)
        else:
            raise AssertionError

    def test_09_open_rules_page(self) -> None:
        """Testing opening RULES page"""
        self.driver.find_element(By.XPATH, '//*[contains(text(), "RULES")]').click()
        self.assertEqual(self.driver.find_element(By.TAG_NAME, 'h1').text[:9], 'The rules')

    def test_10_check_btn_start_game(self) -> None:
        """Testing button 'START GAME'"""
        self.driver.find_element(By.XPATH, '//*[contains(@value, "START GAME")]').click()
        result = self.driver.find_element(By.ID, 'wish').text
        self.assertEqual('Good Luck, My Friend!', result)

    def test_11_open_page_about(self) -> None:
        """Testing opening ABOUT page"""
        self.driver.find_element(By.XPATH, '//*[contains(text(), "ABOUT")]').click()
        self.assertTrue(self.driver.find_element(By.XPATH, '//*[contains(text(), "Alexey Bobrikov")]'))

    def test_12_return_home_page(self) -> None:
        """Testing returning to the home page"""
        self.driver.find_element(By.XPATH, '//*[contains(text(), "GAME")]').click()
        result = self.driver.find_element(By.ID, 'wish').text
        self.assertEqual('Good Luck, My Friend!', result)
        self.driver.close()


class TestOneHandBanditChrome(TestOneHandBanditFirefox):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://one-hand-bandit.vercel.app/')
    play = driver.find_element(By.ID, 'btn')


class TestOneHandBanditEdge(TestOneHandBanditFirefox):
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get('https://one-hand-bandit.vercel.app/')
    play = driver.find_element(By.ID, 'btn')
