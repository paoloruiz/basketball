import os
import sys
import math
class DraftRanks:
  def __init__(self):
    self.goalScores = [15.837, 14.064, 17.998, 17.37, 13.207, -7.423, 5.507, 6.588, 13.611]
    self.scoreRanks = [1.0, 1.5, 1.5, 2.5, 2.5, 0.0, 1.0, 0.0, 2.0]

  def calcDesirability(self, teamScores, playerScores):
    desirability = 0.0
    for i in range(0,9):
      pctComplete = teamScores[i] / self.goalScores[i]
      if pctComplete < 0.0:
        pctComplete = 0.0
      desirability += playerScores[i] * pctComplete * self.scoreRanks[i]
    return desirability

