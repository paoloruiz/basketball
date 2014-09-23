import os
import sys
from season import Season
from nbaplayer import NbaPlayer
from score import Score
year = 2014
season = Season()
sortedPlayers = season.calcSeason('season/nextSeason.txt', year, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1)
scores = []
for p in sortedPlayers:
  se = p.getSeason(year)
  r = se.zScore()
  scores.append(Score(p.name, r))
scores = sorted(scores)
for j in scores:
  print(str(j.name) + "\t" + str(j.score))
