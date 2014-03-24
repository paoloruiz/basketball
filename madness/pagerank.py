import os
import sys
import math
import copy

class PageRank:
  def __init__(self):
    return

  def rank(self, season):
    orig_ranks = dict()
    new_ranks = dict()
    init_value = 1.0/len(season)
    damp = 0.999
    for team in season:
      orig_ranks[team] = init_value
      new_ranks[team] = (1.0-damp)/len(season)
    for i in range(1, 90):
      for team in range(0, len(season.keys())-1):
        games = season[season.keys()[team]].getGames()
        for game in games:
          if not game.didwin():
            new_ranks[game.getopponent()] += damp * orig_ranks[season.keys()[team]] / (float(season[season.keys()[team]].losses) + 0.0001)
      orig_ranks = copy.deepcopy(new_ranks)
      new_ranks.clear()
      for team in season:
        new_ranks[team] = (1.0-damp)/len(season)

    return orig_ranks
