import java.util.*;

class Player {
    public int score = 0;
    public boolean advantage = false;    
}

public class TennisGame {
    
    private Player p1 = new Player();
    private Player p2 = new Player();
    private List<String> scores_defs;

    public TennisGame() {
        scores_defs = Arrays.asList("0","15","30","40");
    }

    public String scores() {
        if (p1.score == 3 && p2.score == 3 
            && (!p1.advantage && !p2.advantage))
            return "deuce";

        if (p1.score == 4)
            return "wins-loses";
        
        if (p2.score == 4)
            return "loses-wins";

        if (p1.advantage) {
            return "adv-40";    
        }
        if (p2.advantage) {
            return "40-adv";    
        }

        return scores_defs.get(p1.score) + "-" + 
               scores_defs.get(p2.score);
    }

    public void playerOneScores() {
        if (p2.advantage) p2.advantage = false;
        else if (p1.score == 3 && p2.score == 3) {
            if (p1.advantage) p1.score += 1;
            p1.advantage = true;
        }        
        else {
            p1.score += 1;
        }
    }

    public void playerTwoScores() {
        if (p1.advantage) p1.advantage = false;    
        else if (p2.score == 3 && p1.score == 3) {
            if (p2.advantage) p2.score += 1;
            p2.advantage = true;
        }
        else {
            p2.score += 1;
        }
        
    }
}