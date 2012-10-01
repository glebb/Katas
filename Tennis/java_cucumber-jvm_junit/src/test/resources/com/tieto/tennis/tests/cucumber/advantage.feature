Feature: Score Advantage
    Scenario: Gaining advantage
        Given "player one" has the score of "40"
        And "player two" has the score of "40"
        When I mark 1 points to "player one"
        Then scoreboard displays "adv-40"

    Scenario: Losing advantage
        Given "player two" has the score of "40"
        And "player one" has the score of "adv"      
        When I mark 1 points to "player two"
        Then scoreboard displays "40-40"        
    