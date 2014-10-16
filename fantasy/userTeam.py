import operator
class UserTeam:
  def __init__(self, name):
    self.name = name
    self.players = []
    self.scores = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

  def addPlayer(self, name, scores):
    self.players.append(name)
    for i in range(0,9):
      self.scores[i] += scores[i]

  def printScores(self):
    goalScores = [15.837, 14.064, 17.998, 17.37, 13.207, -7.423, 5.507, 6.588, 13.611]
    print self.name
    print str(self.scores[0] / goalScores[0]) + '\t' + str(self.scores[1] / goalScores[1]) + '\t' + str(self.scores[2] / goalScores[2]) + '\t' + str(self.scores[3] / goalScores[3]) + '\t' + str(self.scores[4] / goalScores[4]) + '\t' + str(self.scores[5] / goalScores[5]) + '\t' + str(self.scores[6] / goalScores[6]) + '\t' + str(self.scores[7] / goalScores[7]) + '\t' + str(self.scores[8] / goalScores[8])

  def getDesirabilities(self, players):
    dr = DraftRanks()
    desirabilities = {}
    for player in players:
      desirabilities[player.name] = dr.getDesirability(self.scores, player.getScores())
    return sorted(desirabilities.items(), key=operator.itemgetter(1), reverse=True)
