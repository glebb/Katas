Feature: Winning and losing a game
    Scenario: Winning straight
        Given "player one" has the score of "40"
        And "player two" has the score of "15"
        When I mark 1 points to "player one"
        Then scoreboard displays "wins-loses"
        
    Scenario: Winning after advantage
        Given "player one" has the score of "40"
        And "player two" has the score of "adv"
        When I mark 1 points to "player two"
        Then scoreboard displays "loses-wins"