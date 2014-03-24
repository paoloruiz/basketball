import os
import sys
import math
class Team:
  def __init__(self, name):
    self.name = name
    self.scores = 1.0
    self.games = []
    self.wins = 0
    self.losses = 0
    self.rebounds = 0.0
    self.blocks = 0.0
    self.steals = 0.0
    self.assists = 0.0
    self.turnovers = 0.0
    self.seed = 0.0

  def addGame(self, game):
    self.games.append(game)
    if game.didwin():
      self.wins += 1
    else:
      self.losses += 1

  def getGames(self):
    return self.games

  def getScores(self):
    mySco = 0.0
    theirSco = 0.0
    for g in self.games:
      mySco += float(g.myscore)
      theirSco += float(g.theirscore)
    return (mySco/len(self.games), theirSco/len(self.games))
