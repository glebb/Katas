package com.tennis.tieto.tests.unit;

import static org.junit.Assert.assertEquals;

import org.junit.Before;
import org.junit.Test;

import com.tieto.tennis.TennisGame;

public class TennisGameTest {

	private TennisGame game;
	
	private void setScores(int p1, int p2) {
		for (int i=0; i < p1; i++) {
			game.playerOneScores();
		}
		for (int i=0; i < p2; i++) {
			game.playerTwoScores();
		}
	}
	
	@Before
	public void setUp() {
		game = new TennisGame();
	}
	
	@Test
	public void gameBeginsFrom0_0() {
		assertEquals("0-0", game.getScore());
	}
	
	@Test
	public void playerOneScoresOnce() {
		game.playerOneScores();
		assertEquals("15-0", game.getScore());		
	}

	@Test
	public void playerOneScoresTwice() {
		setScores(2,0);
		assertEquals("30-0", game.getScore());		
	}

	@Test
	public void playerTwoScoresOnce() {
		game.playerTwoScores();
		assertEquals("0-15", game.getScore());		
	}

	@Test
	public void playerTwoScoresThrice() {
		setScores(0,3);
		assertEquals("0-40", game.getScore());		
	}
	
	@Test
	public void bothPlayersScores3Times() {
		setScores(3,3);
		assertEquals("40-40", game.getScore());
	}
	
	@Test
	public void playerOneGainsAdvantage() {
		setScores(3,3);
		game.playerOneScores();
		assertEquals("adv-40", game.getScore());
	}
	
	@Test
	public void palyerOneLosesAdvantage() {
		setScores(3,3);
		game.playerOneScores();
		game.playerTwoScores();		
		assertEquals("40-40", game.getScore());
	}

	@Test
	public void playerTwoGainsAdvantage() {
		setScores(3,3);
		game.playerTwoScores();
		assertEquals("40-adv", game.getScore());
	}
	
	@Test
	public void palyerTwoLosesAdvantage() {
		setScores(3,3);
		game.playerTwoScores();
		game.playerOneScores();		
		assertEquals("40-40", game.getScore());
	}
	
	@Test
	public void playerOneWins() {
		setScores(3,0);
		game.playerOneScores();		
		assertEquals("wins-loses", game.getScore());
	}
	
	@Test
	public void playerTwoWins() {
		setScores(1,3);
		game.playerTwoScores();		
		assertEquals("loses-wins", game.getScore());
	}

	@Test
	public void playerOneWinsAfterAdvantage() {
		setScores(3,3);
		game.playerOneScores();
		game.playerOneScores();
		assertEquals("wins-loses", game.getScore());
	}
	
	@Test
	public void playerTwoWinsAfterAdvantage() {
		setScores(3,3);
		game.playerTwoScores();
		game.playerTwoScores();
		assertEquals("loses-wins", game.getScore());
	}
	
	
}
