import unittest

class _Player(object):
    def __init__(self, name):
        self.score = 0
        self.hasAdvantage = False
        self.wins = False
        self.name = name

class TennisGame(object):

    def __init__(self, p1, p2, *args, **kwargs):
        object.__init__(self, *args, **kwargs)
        self.p1 = _Player(p1)
        self.p2 = _Player(p2)
        self.scoreLiterals = ("0", "15", "30", "40")
        
    def score(self):
        status = self._advOrWins()
        if status:
            return status
        else:
            return self.scoreLiterals[self.p1.score] + "-" + self.scoreLiterals[self.p2.score]

    
    def playerOneScores(self):
        if self.p2.hasAdvantage:
            self.p2.hasAdvantage = False
        elif self.p1.hasAdvantage:
            self.p1.wins = True
            self.p1.hasAdvantage = False
        elif self.p1.score == 3 and self.p2.score == 3:
            self.p1.hasAdvantage = True
        elif self.p1.score == 3:
            self.p1.wins = True
        else:
            self.p1.score += 1

    
    def playerTwoScores(self):
        if self.p1.hasAdvantage:
            self.p1.hasAdvantage = False
        elif self.p2.hasAdvantage:
            self.p2.wins = True
            self.p2.hasAdvantage = False
        elif self.p1.score == 3 and self.p2.score == 3:
            self.p2.hasAdvantage = True
        elif self.p2.score == 3:
            self.p2.wins = True
        else:
            self.p2.score += 1

    def _advOrWins(self):
        if self.p1.hasAdvantage:
            return self.p1.name + " advantage"
        if self.p2.hasAdvantage:
            return self.p2.name + " advantage"
        if self.p1.wins:
            return self.p1.name + " wins"
        if self.p2.wins:
            return self.p2.name + " wins"  
        if self.p1.score == 3 and self.p2.score == 3:
            return "deuce"
        return None

class TennisSpec(unittest.TestCase):

    def setScores(self, p1, p2):
        [self.game.playerOneScores() for i in range(p1)]
        [self.game.playerTwoScores() for i in range(p2)]
  
    def setUp(self):
        self.game = TennisGame("player 1", "player 2")

    def testGameBegins0_0(self):
        self.assertEqual("0-0", self.game.score())
        
    def testPlayerOneScores(self):
        self.setScores(1, 0)
        self.assertEqual("15-0", self.game.score())
        
    def testPlayerTwoScores(self):
        self.game.playerTwoScores()
        self.assertEqual("0-15", self.game.score())
        
    def testPlayerTwoScoresTwice(self):
        self.setScores(0, 2)
        self.assertEqual("0-30", self.game.score())

    def testPlayerTwoScoresThrice(self):
        self.setScores(0,3)
        self.assertEqual("0-40", self.game.score())

    def testPlayerOneWinsDirectly(self):
        self.setScores(4,0)
        self.assertEqual("player 1 wins", self.game.score())

    def testDeuce(self):
        self.setScores(3,3)
        self.assertEqual("deuce", self.game.score())
        
    def testPlayerOneGainsAdvatange(self):
        self.setScores(3,3)
        self.game.playerOneScores()
        self.assertEqual("player 1 advantage", self.game.score())
        
    def testPlayerTwoGainsAdvatange(self):
        self.setScores(3,3)
        self.game.playerTwoScores()
        self.assertEqual("player 2 advantage", self.game.score())

    def testPlayerOneLosesAdvantage(self):
        self.setScores(3,3)
        self.setScores(1,1)
        self.assertEqual("deuce", self.game.score())

    def testPlayerTwoLosesAdvantage(self):
        self.setScores(3,3)
        self.game.playerTwoScores()
        self.game.playerOneScores()
        self.assertEqual("deuce", self.game.score())


    def testPlayerOneWinsAfterAdvantage(self):
        self.setScores(3,3)
        self.setScores(2,0)
        self.assertEqual("player 1 wins", self.game.score())

    def testPlayerTwoWinsAfterAdvantage(self):
        self.setScores(3,3)
        self.setScores(0,2)
        self.assertEqual("player 2 wins", self.game.score())

        
if __name__ == "__main__":
    unittest.main()