import os
import sys
from season import Season
from nbaplayer import NbaPlayer
from score import Score
year = 2013
se = Season()
sortedPlayers = se.calcSeason('season/thisStats.txt', year, 3, 1, 2, 28, 23, 22, 24, 25, 26, 10, 19, 11, 7)
scores = []
for p in sortedPlayers:
  se = p.getSeason(year)
  if ("PF" in p.position):
    scores.append(Score(p.name, se.zScore(1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0), se.zScore()))
scores = sorted(scores)
for j in scores:
  print(j.name + "\t" + str(j.score) + "\t" + str(j.extra))
