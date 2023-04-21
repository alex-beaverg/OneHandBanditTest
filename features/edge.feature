# Tests with behave module can be run from command-line:
#   Run with all feature files:
#       behave -i .feature
#   Run only with edge.feature file (this file):
#       behave -i edge.feature
# Command-line argument "-i" - only run feature files matching regular expression pattern

# Tests with behave module with beautiful allure report can be run from command-line:
#   Run tests with output JSON report files in "test-allure-behave-reports" folder:
#       With all feature files:
#           behave -f allure_behave.formatter:AllureFormatter -o test-allure-behave-reports -i .feature
#       With edge.feature file:
#           behave -f allure_behave.formatter:AllureFormatter -o test-allure-behave-reports -i edge.feature
#   Show beautiful allure report:
#       allure serve test-allure-behave-reports
# Command-line argument "-f" - formatter
# Command-line argument "-o" - the directory to generate Allure report into
# Command-line argument "-i" - only run feature files matching regular expression pattern

Feature: The game "One Hand Bandit" with "edge" browser

  Scenario: Open and check all pages of the game with "edge" browser
    Given website "https://one-hand-bandit.vercel.app/" with "edge" browser
    When you open the game page with text "Good Luck, My Friend!"
    Then you see the page including text "Good Luck, My Friend!"
    When you click "PLAY" button
    Then the game can be played
    When the game is won
    Then you can see your results
    When you click "PLAY AGAIN" button
    Then you can play again
      And you can see your next results
    When you click "DELETE RESULT" button
    Then you can't see results
    When you click "RULES" button
    Then you can read the rules of the game
    When you click "START GAME" button
    Then you can see game page
    When you click "ABOUT" button
    Then you can read "ABOUT" page
    When you click "GAME" button
    Then you can return to the home page
