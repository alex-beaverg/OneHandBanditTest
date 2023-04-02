import unittest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class TestOneHandBandit(unittest.TestCase):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get('https://one-hand-bandit.vercel.app/')
    play = driver.find_element(By.ID, 'btn')

    def test_1_open_home_page(self) -> None:
        """Testing of opening home page"""
        result = self.driver.find_element(By.ID, 'wish').text
        self.assertEqual('Good Luck, My Friend!', result)

    def test_2_play_1_game(self) -> None:
        """Testing of playing game to first win"""
        self.play.click()
        while True:
            try:
                self.driver.find_element(By.XPATH, '//*[contains(text(), "You WON")]')
            except NoSuchElementException:
                self.play.click()
            else:
                break
        result = self.driver.find_element(By.XPATH, '//*[contains(text(), "You WON")]').text[:8]
        self.assertEqual('You WON!', result)

    def test_3_results_1_game(self) -> None:
        """Testing results of first game"""
        result = self.driver.find_element(By.XPATH, '//*[contains(text(), "1st game")]').text[:8]
        self.assertEqual('1st game', result)

    def test_4_play_2_game(self) -> None:
        """Testing of playing game to second win"""
        self.play.click()
        while True:
            try:
                self.driver.find_element(By.XPATH, '//*[contains(text(), "You WON")]')
            except NoSuchElementException:
                self.play.click()
            else:
                break
        result = self.driver.find_element(By.XPATH, '//*[contains(text(), "You WON")]').text[:8]
        self.assertEqual('You WON!', result)

    def test_5_results_2_game(self) -> None:
        """Testing results of second game"""
        result = self.driver.find_element(By.XPATH, '//*[contains(text(), "2nd game")]').text[:8]
        self.assertEqual('2nd game', result)

    def test_6_play_3_game(self) -> None:
        """Testing of playing game to third win"""
        self.play.click()
        while True:
            try:
                self.driver.find_element(By.XPATH, '//*[contains(text(), "You WON")]')
            except NoSuchElementException:
                self.play.click()
            else:
                break
        result = self.driver.find_element(By.XPATH, '//*[contains(text(), "You WON")]').text[:8]
        self.assertEqual('You WON!', result)

    def test_7_results_3_game(self) -> None:
        """Testing results of third game"""
        result = self.driver.find_element(By.XPATH, '//*[contains(text(), "3rd game")]').text[:8]
        self.assertEqual('3rd game', result)

        self.driver.close()
