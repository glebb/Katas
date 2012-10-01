package com.tieto.tennis;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class TennisGame {

	
	private List<ScoreBoard> scoreboards = new ArrayList<ScoreBoard>();
	
	private class Player {
		public int tracker = 0;
	}

	private Player playerOne;
	private Player playerTwo;
	
	private static final List<String> scoresDefs = Arrays.asList
			("0", "15", "30", "40", "adv", "wins", "loses");
	
	public String getScore() {
		return scoresDefs.get(playerOne.tracker) + "-" + scoresDefs.get(playerTwo.tracker);
	}
	
	public TennisGame() {
		playerOne = new Player();
		playerTwo = new Player();
	}
	
	public void attach(ScoreBoard sb) {
		scoreboards.add(sb);
		sb.updateScore(getScore());		
	}	

	public void playerOneScores() {
		if (hasAdvantage(playerTwo)) {
			playerTwo.tracker--;
		}
		else if (checkForNormalWin(playerOne, playerTwo)) {
			setFinalScore(playerOne, playerTwo);
		}
		else if (playerOne.tracker == scoresDefs.indexOf("adv")) {
			setFinalScore(playerOne, playerTwo);		}
		else this.playerOne.tracker++;
		updateScores();
	}

	public void playerTwoScores() {
		if (hasAdvantage(playerOne)) {
			playerOne.tracker--;
		}
		else if (checkForNormalWin(playerTwo, playerOne)) {
			setFinalScore(playerTwo, playerOne);
		}
		else if (playerTwo.tracker == scoresDefs.indexOf("adv")) {
			setFinalScore(playerTwo, playerOne);		}
		else this.playerTwo.tracker++;
		updateScores();
	}	
	
	private boolean hasAdvantage(Player player) {
		return player.tracker == scoresDefs.indexOf("adv");		
	}
	
	private void updateScores() {
		for (ScoreBoard sb : scoreboards) {
			sb.updateScore(getScore());
		}
		
	}

	private void setFinalScore(Player winner, Player loser) {
		winner.tracker = scoresDefs.indexOf("wins");
		loser.tracker = scoresDefs.indexOf("loses");
	}
	
	private boolean checkForNormalWin(Player candidate, Player other) {
		return candidate.tracker == scoresDefs.indexOf("40") 
				&& other.tracker < scoresDefs.indexOf("40");		
	}
}
