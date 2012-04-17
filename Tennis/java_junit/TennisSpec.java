import org.junit.*;
import static org.junit.Assert.*;

public class TennisSpec {
    
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
    public void it_should_be_0_0_at_start() {
        assertEquals("0-0", game.scores());
    }

    @Test
    public void playerOneScoresOnce() {
        setScores(1,0);
        assertEquals("15-0", game.scores());
    }

    @Test
    public void playerTwoScoresOnce() {
        setScores(0,1);
        assertEquals("0-15", game.scores());
    }

    @Test
    public void playerTwoScoresTwice() {
        setScores(0,2);
        assertEquals("0-30", game.scores());
    }

    @Test
    public void playerTwoScoresThrice() {
        setScores(0,3);
        assertEquals("0-40", game.scores());
    }

    @Test
    public void playerOneScoresTwiceAndP2ScoresThrice() {
        setScores(2,3);
        assertEquals("30-40", game.scores());
    }

    @Test
    public void deuce() {
        setScores(3,3); // 40-40
        assertEquals("deuce", game.scores());
    }

    @Test
    public void playerTwoGainsAdvantage() {
        setScores(3,3); // 40-40
        setScores(0,1);
        assertEquals("40-adv", game.scores());
    }

    @Test
    public void playerTwoLosesAdvantage() {
        setScores(3,3); // 40-40
        setScores(0,1);
        setScores(1,0);
        assertEquals("deuce", game.scores());
    }

    @Test
    public void playerOneLosesAdvantage() {
        setScores(3,3); // 40-40
        setScores(1,0);
        setScores(0,1);
        assertEquals("deuce", game.scores());
    }

    
    @Test
    public void playerOneWinsStraight() {
        setScores(4,0);
        assertEquals("wins-loses", game.scores());
    }


    @Test
    public void playerTwoWinsStraight() {
        setScores(0,4);
        assertEquals("loses-wins", game.scores());
    }

    @Test
    public void playerTwoWinsAfterAdv() {
        setScores(3,3);
        setScores(0,2);
        assertEquals("loses-wins", game.scores());
    }

    @Test
    public void playerOneWinsAfterAdv() {
        setScores(3,3);
        setScores(2,0);
        assertEquals("wins-loses", game.scores());
    }


}