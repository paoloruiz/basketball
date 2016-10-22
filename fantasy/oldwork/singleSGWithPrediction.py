import os
import sys
from season import Season
from nbaplayer import NbaPlayer
from score import Score
year = 2013
se = Season()
sortedPlayers = se.calcSeason('season/nextSeason.txt', year, 0, 0, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1)
scores = []
for p in sortedPlayers:
  se = p.getSeason(year)
  if ("SG" in p.position):
    scores.append(Score(p.name, se.zScore(1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 1.0), se.zScore()))
scores = sorted(scores)
for j in scores:
  print(j.name + "\t" + str(j.score) + "\t" + str(j.extra))
