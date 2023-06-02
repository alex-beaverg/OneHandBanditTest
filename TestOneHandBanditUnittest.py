# Tests with unittest module can be run from command-line:
#   Run tests without details:
#       python -m unittest
#   Run tests with more details (command-line argument "-v"):
#       python -m unittest -v
#   Run tests with output XML report file in "test-xmlrunner-reports" folder:
#       python -m test_one_hand_bandit_unittest
#       python TestOneHandBanditUnittest.py
# Command-line argument "-m" - run only test files

# Tests with unittest module also can be run in IDE (with integrated report):
#   Click "Run" button
#   Press "Shift + F10"

# Tests with unittest module (as pytest for beautiful allure report) can be run from command-line:
#   Run tests with output JSON report files in "test-allure-reports" folder:
#       python -m pytest TestOneHandBanditUnittest.py --alluredir test-allure-reports -s
#   Show beautiful allure report:
#       allure serve test-allure-reports
# Command-line argument "--alluredir" - folder for JSON report files
# Command-line argument "-s" - disable all output capturing from the command-line (otherwise there will be an OSError)

import unittest
import allure

from pageobjects.HomePage import HomePage
from pageobjects.RulesPage import RulesPage
from pageobjects.AboutPage import AboutPage
from helpers.WebDriver import WebDriver


@allure.story('One Hand Bandit game tests')
@allure.feature('All step by step tests')
@allure.testcase('Open and check all pages of the game')
class TestCaseAllOneHandBanditTests(unittest.TestCase):
    """Docstring: Class TestCaseAllOneHandBanditTests extends unittest.TestCase"""

    @allure.step('Setup Test Case method (Before every test)')
    def setUp(self):
        """Docstring: Setup Test Case method (Before every test)"""
        self.driver = WebDriver()
        self.driver.maximize_window()
        self.home_page_url = 'https://one-hand-bandit.vercel.app/'
        self.rules_page_url = 'https://one-hand-bandit.vercel.app/rules.html'
        self.about_page_url = 'https://one-hand-bandit.vercel.app/about.html'

    @allure.step('Teardown Test Case method (After every test)')
    def tearDown(self) -> None:
        """Docstring: Teardown Test Case method (After every test)"""
        self.driver.quit()

    @allure.step('Test 01. Testing opening HOME page')
    def test_01_open_home_page(self) -> None:
        """Docstring: Testing opening HOME page"""
        self.driver.get(self.home_page_url)
        home_page = HomePage(self.driver)
        self.assertEqual(home_page.get_hp_find_text(), home_page.get_hp_real_text())

    @allure.step('Test 02. Testing playing game to first win')
    def test_02_play_1st_game(self) -> None:
        """Docstring: Testing playing game to first win"""
        self.driver.get(self.home_page_url)
        home_page = HomePage(self.driver)
        home_page.hp_play_game(home_page.get_hp_real_first_game_result())
        self.assertEqual(home_page.get_hp_game_result().text[:8], home_page.get_hp_real_first_game_result())

    @allure.step('Test 03. Testing playing game to second win')
    def test_03_play_2nd_game(self) -> None:
        """Docstring: Testing playing game to second win"""
        self.driver.get(self.home_page_url)
        home_page = HomePage(self.driver)
        home_page.hp_play_game(home_page.get_hp_real_first_game_result())
        home_page.hp_play_game(home_page.get_hp_real_second_game_result())
        self.assertEqual(home_page.get_hp_game_result().text[:8], home_page.get_hp_real_second_game_result())

    @allure.step('Test 04. Testing playing game to third win')
    def test_04_play_3rd_game(self) -> None:
        """Docstring: Testing playing game to third win"""
        self.driver.get(self.home_page_url)
        home_page = HomePage(self.driver)
        home_page.hp_play_game(home_page.get_hp_real_first_game_result())
        home_page.hp_play_game(home_page.get_hp_real_second_game_result())
        home_page.hp_play_game(home_page.get_hp_real_third_game_result())
        self.assertEqual(home_page.get_hp_game_result().text[:8], home_page.get_hp_real_third_game_result())

    @allure.step('Test 05. Testing deleting results')
    def test_05_delete_results(self) -> None:
        """Docstring: Testing deleting results"""
        self.driver.get(self.home_page_url)
        home_page = HomePage(self.driver)
        home_page.hp_play_game(home_page.get_hp_real_first_game_result())
        home_page.hp_delete_result()
        self.assertEqual(home_page.get_hp_find_src_in_cells(), home_page.get_hp_real_src_in_cells())

    @allure.step('Test 06. Testing RULES menu item on the HOME page')
    def test_06_open_rules_page_from_home_page(self) -> None:
        """Docstring: Testing RULES menu item on the HOME page"""
        self.driver.get(self.home_page_url)
        home_page = HomePage(self.driver)
        home_page.click_rules_menu_item()
        rules_page = RulesPage(self.driver)
        self.assertEqual(rules_page.get_rp_find_text(), rules_page.get_rp_real_text())

    @allure.step('Test 07. Testing ABOUT menu item on the HOME page')
    def test_07_open_about_page_from_home_page(self) -> None:
        """Docstring: Testing ABOUT menu item on the HOME page"""
        self.driver.get(self.home_page_url)
        home_page = HomePage(self.driver)
        home_page.click_about_menu_item()
        about_page = AboutPage(self.driver)
        self.assertEqual(about_page.get_ap_find_text(), about_page.get_ap_real_text())

    @allure.step('Test 08. Testing START GAME button on the RULES page')
    def test_08_open_home_page_from_rules_page(self) -> None:
        """Docstring: Testing START GAME button on the RULES page"""
        self.driver.get(self.rules_page_url)
        rules_page = RulesPage(self.driver)
        rules_page.rp_click_start_game_button()
        home_page = HomePage(self.driver)
        self.assertEqual(home_page.get_hp_find_text(), home_page.get_hp_real_text())

    @allure.step('Test 09. Testing GAME menu item on the RULES page')
    def test_09_open_home_page_from_rules_page(self) -> None:
        """Docstring: Testing GAME menu item on the RULES page"""
        self.driver.get(self.rules_page_url)
        rules_page = RulesPage(self.driver)
        rules_page.click_game_menu_item()
        home_page = HomePage(self.driver)
        self.assertEqual(home_page.get_hp_find_text(), home_page.get_hp_real_text())

    @allure.step('Test 10. Testing ABOUT menu item on the RULES page')
    def test_10_open_about_page_from_rules_page(self) -> None:
        """Docstring: Testing ABOUT menu item on the RULES page"""
        self.driver.get(self.rules_page_url)
        rules_page = RulesPage(self.driver)
        rules_page.click_about_menu_item()
        about_page = AboutPage(self.driver)
        self.assertEqual(about_page.get_ap_find_text(), about_page.get_ap_real_text())

    @allure.step('Test 11. Testing GAME menu item on the ABOUT page')
    def test_11_open_home_page_from_about_page(self) -> None:
        """Docstring: Testing GAME menu item on the ABOUT page"""
        self.driver.get(self.about_page_url)
        about_page = AboutPage(self.driver)
        about_page.click_game_menu_item()
        home_page = HomePage(self.driver)
        self.assertEqual(home_page.get_hp_find_text(), home_page.get_hp_real_text())

    @allure.step('Test 12. Testing RULES menu item on the ABOUT page')
    def test_12_open_rules_page_from_about_page(self) -> None:
        """Docstring: Testing RULES menu item on the ABOUT page"""
        self.driver.get(self.about_page_url)
        about_page = AboutPage(self.driver)
        about_page.click_rules_menu_item()
        rules_page = RulesPage(self.driver)
        self.assertEqual(rules_page.get_rp_find_text(), rules_page.get_rp_real_text())


if __name__ == '__main__':
    import xmlrunner

    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-xmlrunner-reports'),
        failfast=False,
        buffer=False,
        catchbreak=False)
