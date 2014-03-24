import os
import sys
from season import Season
from nbaplayer import NbaPlayer
from namescore import NameScore
o = open('thisseason.txt', 'r')
players = []
overdist = 0.0
avgdist = 0.0
plNum = 0
for line in o:
  m = line.split('\t')
  sco = NameScore(m[0], m[1])
  players.append(sco)
o.close()
d = open('predict.txt', 'r')
for line in d:
  m = line.split('\t')
  sco = NameScore(m[0], m[1])
  if sco in players:
    plNum += 1
    other = players[players.index(sco)]
    s = float(sco.score) - float(other.score)
    print(sco.name + '\t' + str(s))
    overdist += s
    if s < 0:
      s = -s
    avgdist += s
print("Number of players in both: " + str(plNum) + ", average distance: " + str(avgdist/plNum) + ", and overall distance: " + str(overdist/plNum))
