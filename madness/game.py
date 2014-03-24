import os
import sys
import math
class Game:
  def __init__(self, opponent, myscore, theirscore):
    self.opponent = opponent
    self.myscore = myscore
    self.theirscore = theirscore

  def didwin(self):
    return self.myscore > self.theirscore

  def getopponent(self):
    return self.opponent
