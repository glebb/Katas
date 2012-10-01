Feature: Score counting up to 40
	
	Scenario: Love
	   Given no points have been scored
	   Then scoreboard displays "0-0"
				
	Scenario Outline: Basic scores
	   When I mark <p1> points to "player one"
	   And I mark <p2> points to "player two"
	   Then scoreboard displays <score>
	   
	   Examples:
	       | p1 | p2 | score   | 
	       |  1 | 0  | "15-0"  |
           |  2 | 0  | "30-0"  |
           |  0 | 1  | "0-15"  |
           |  2 | 2  | "30-30" |
           |  3 | 1  | "40-15" |
           |  3 | 3  | "40-40" |
 
	       