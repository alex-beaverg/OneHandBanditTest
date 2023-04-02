# behave -i firefox.feature
Feature: The game "One Hand Bandit"

  Scenario: Open and check all pages of the game
    Given website "https://one-hand-bandit.vercel.app/" with "firefox" browser
    Then index page include text "Good Luck, My Friend!"
    Then the game can be played
    Then the game can be won
    Then you can see your results
    Then you can play again
    Then you can see your next results
    Then you can delete your results
    Then you can read the rules of the game
    Then you can click to "START GAME" button
    Then you can read "ABOUT" page
    Then you can return to the home page
