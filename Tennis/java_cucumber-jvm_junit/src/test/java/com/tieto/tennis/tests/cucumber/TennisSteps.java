package com.tieto.tennis.tests.cucumber;

import static org.junit.Assert.assertEquals;

import com.tieto.tennis.ScoreBoard;
import com.tieto.tennis.TennisGame;

import cucumber.annotation.Before;
import cucumber.annotation.en.Given;
import cucumber.annotation.en.Then;
import cucumber.annotation.en.When;

public class TennisSteps {

	private TennisGame game;
	private MockScoreBoard sb;
	
	@Before
	public void setUp() {
		game = new TennisGame();
		sb = new MockScoreBoard();
		game.attach(sb);
	}
	
	@Given("^no points have been scored$")
	public void no_points_have_been_scored() throws Throwable {
	}

	@Then("^scoreboard displays \"([^\"]*)\"$")
	public void scoreboard_displays(String score) throws Throwable {
		assertEquals(score, sb.currentScore);
	}

	@When("^I mark (\\d+) points to \"([^\"]*)\"$")
	public void I_mark_points_to(int points, String player) throws Throwable {
		if (player.equals("player one")) {
			for (int i=0; i < points; i++) {
				game.playerOneScores();
			}
			
		}
		if (player.equals("player two")) {

			for (int i=0; i < points; i++) {
				game.playerTwoScores();
			}
		}
	}
	
	@Given("^\"([^\"]*)\" has the score of \"([^\"]*)\"$")
	public void has_the_score_of(String arg1, String arg2) throws Throwable {
		if (arg1.equals("player one")) {
			while (!sb.currentScore.startsWith(arg2)) {
				game.playerOneScores();
			}
		}
		if (arg1.equals("player two")) {
			while (!sb.currentScore.endsWith(arg2)) {
				game.playerTwoScores();
			}
		}

	}


}

class MockScoreBoard implements ScoreBoard{
	public String currentScore;

	public void updateScore(String score) {
		currentScore = score;
		
	}
}
