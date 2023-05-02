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

from pageobjects.HomePage import HomePage
from pageobjects.RulesPage import RulesPage
from pageobjects.AboutPage import AboutPage


@allure.story('One Hand Bandit game tests')
@allure.feature('All step by step tests')
@allure.testcase('Open and check all pages of the game')
class TestCaseAllStepByStepTests(unittest.TestCase):

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
        cls.base_url = 'https://one-hand-bandit.vercel.app/'

    @classmethod
    @allure.step('Tear Down Test Case method (After tests)')
    def tearDownClass(cls) -> None:
        """Docstring: Tear Down Test Case method (After tests)"""
        # We have to quit webdriver
        cls.driver.quit()

    @allure.step('Test 01. Testing opening HOME page')
    def test_01_open_home_page(self) -> None:
        """Docstring: Testing opening HOME page"""
        self.driver.get(self.base_url)
        home_page = HomePage(self.driver)
        self.assertEqual(home_page.get_hp_find_text(), home_page.get_hp_real_text())

    @allure.step('Test 02. Testing playing game to first win')
    def test_02_play_1st_game(self) -> None:
        """Docstring: Testing playing game to first win"""
        home_page = HomePage(self.driver)
        home_page.hp_play_game(home_page.get_hp_real_first_game_result())
        self.assertEqual(home_page.get_hp_game_result().text[:8], home_page.get_hp_real_first_game_result())

    @allure.step('Test 03. Testing playing game to second win')
    def test_03_play_2nd_game(self) -> None:
        """Docstring: Testing playing game to second win"""
        home_page = HomePage(self.driver)
        home_page.hp_play_game(home_page.get_hp_real_second_game_result())
        self.assertEqual(home_page.get_hp_game_result().text[:8], home_page.get_hp_real_second_game_result())

    @allure.step('Test 04. Testing playing game to third win')
    def test_04_play_3rd_game(self) -> None:
        """Docstring: Testing playing game to third win"""
        home_page = HomePage(self.driver)
        home_page.hp_play_game(home_page.get_hp_real_third_game_result())
        self.assertEqual(home_page.get_hp_game_result().text[:8], home_page.get_hp_real_third_game_result())

    @allure.step('Test 05. Testing deleting results')
    def test_05_delete_results(self) -> None:
        """Docstring: Testing deleting results"""
        home_page = HomePage(self.driver)
        home_page.hp_delete_result()
        self.assertEqual(home_page.get_hp_find_src_in_cells(), home_page.get_hp_real_src_in_cells())

    @allure.step('Test 06. Testing RULES menu item on the HOME page')
    def test_06_open_rules_page_from_home_page(self) -> None:
        """Docstring: Testing RULES menu item on the HOME page"""
        home_page = HomePage(self.driver)
        home_page.hp_click_rules_menu_item()
        rules_page = RulesPage(self.driver)
        self.assertEqual(rules_page.get_rp_find_text(), rules_page.get_rp_real_text())

    @allure.step('Test 07. Testing START GAME button on the RULES page')
    def test_07_open_home_page_from_rules_page(self) -> None:
        """Docstring: Testing START GAME button on the RULES page"""
        rules_page = RulesPage(self.driver)
        rules_page.rp_click_start_game_button()
        home_page = HomePage(self.driver)
        self.assertEqual(home_page.get_hp_find_text(), home_page.get_hp_real_text())

    @allure.step('Test 08 (repeat Test 06)')
    def test_08_repeat_test_06(self) -> None:
        """Docstring: Test 08 (repeat Test 06)"""
        home_page = HomePage(self.driver)
        home_page.hp_click_rules_menu_item()
        rules_page = RulesPage(self.driver)
        self.assertEqual(rules_page.get_rp_find_text(), rules_page.get_rp_real_text())

    @allure.step('Test 09. Testing GAME menu item on the RULES page')
    def test_09_open_home_page_from_rules_page(self) -> None:
        """Docstring: Testing GAME menu item on the RULES page"""
        rules_page = RulesPage(self.driver)
        rules_page.rp_click_game_menu_item()
        home_page = HomePage(self.driver)
        self.assertEqual(home_page.get_hp_find_text(), home_page.get_hp_real_text())

    @allure.step('Test 10 (repeat Test 06)')
    def test_10_repeat_test_06(self) -> None:
        """Docstring: Test 10 (repeat Test 06)"""
        home_page = HomePage(self.driver)
        home_page.hp_click_rules_menu_item()
        rules_page = RulesPage(self.driver)
        self.assertEqual(rules_page.get_rp_find_text(), rules_page.get_rp_real_text())

    @allure.step('Test 11. Testing ABOUT menu item on the RULES page')
    def test_11_open_about_page_from_rules_page(self) -> None:
        """Docstring: Testing ABOUT menu item on the RULES page"""
        rules_page = RulesPage(self.driver)
        rules_page.rp_click_about_menu_item()
        about_page = AboutPage(self.driver)
        self.assertEqual(about_page.get_ap_find_text(), about_page.get_ap_real_text())

    @allure.step('Test 12. Testing GAME menu item on the ABOUT page')
    def test_12_open_home_page_from_about_page(self) -> None:
        """Docstring: Testing GAME menu item on the ABOUT page"""
        about_page = AboutPage(self.driver)
        about_page.ap_click_game_menu_item()
        home_page = HomePage(self.driver)
        self.assertEqual(home_page.get_hp_find_text(), home_page.get_hp_real_text())

    @allure.step('Test 13. Testing ABOUT menu item on the HOME page')
    def test_13_open_about_page_from_home_page(self) -> None:
        """Docstring: Testing ABOUT menu item on the HOME page"""
        home_page = HomePage(self.driver)
        home_page.hp_click_about_menu_item()
        about_page = AboutPage(self.driver)
        self.assertEqual(about_page.get_ap_find_text(), about_page.get_ap_real_text())

    @allure.step('Test 14. Testing RULES menu item on the ABOUT page')
    def test_14_open_rules_page_from_about_page(self) -> None:
        """Docstring: Testing RULES menu item on the ABOUT page"""
        about_page = AboutPage(self.driver)
        about_page.ap_click_rules_menu_item()
        rules_page = RulesPage(self.driver)
        self.assertEqual(rules_page.get_rp_find_text(), rules_page.get_rp_real_text())


if __name__ == '__main__':
    import xmlrunner

    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-xmlrunner-reports'),
        failfast=False,
        buffer=False,
        catchbreak=False)
