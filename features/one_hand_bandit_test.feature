Feature: Open "One Hand Bandit" game's index page
  Scenario: Open and check index page in firefox browser
    Given website "https://one-hand-bandit.vercel.app/"
    Then index page include text "Good Luck, My Friend!"
    Then the game can be played
    Then the game can be won
    Then you can see your results
    Then you can delete your results