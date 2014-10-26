import os
import sys
import math
from season import Season
from nbaplayer import NbaPlayer
from score import Score
year = 2013
se = Season()
sortedPlayers = se.calcSeason('season/thisStats.txt', year, 3, 1, 2, 28, 23, 22, 24, 25, 26, 10, 19, 11, 7)
scores = []
ovpoints = 0.0
ovassists = 0.0
ovrebounds = 0.0
ovsteals = 0.0
ovblocks = 0.0
ovturnovers = 0.0
ovfgp = 0.0
ovftp = 0.0
ovtpm = 0.0
f = open('input/' + sys.argv[1] + '.txt', 'r')
ou = open('output/' + sys.argv[1] + 'Stats.txt', 'w')
for line in f:
  p = NbaPlayer(line.split('\t')[0], "ATH", year, None)
  print line
  playerIndex = sortedPlayers.index(p)
  s = sortedPlayers[playerIndex].getSeason(year)
  ou.write(p.name + '\t' + str(math.ceil(s.scores[0]*1000)/1000.0) + '\t' + str(math.ceil(s.scores[1]*1000)/1000.0) + '\t' + str(math.ceil(s.scores[2]*1000)/1000.0) + '\t' + str(math.ceil(s.scores[3]*1000)/1000.0) + '\t' + str(math.ceil(s.scores[4]*1000)/1000.0) + '\t' + str(math.ceil(s.scores[5]*1000)/1000.0) + '\t' + str(math.ceil(s.scores[6]*1000)/1000.0) + '\t' + str(math.ceil(s.scores[7]*1000)/1000.0) + '\t' + str(math.ceil(s.scores[8]*1000)/1000.0) + '\n')
  ovpoints += math.ceil(s.scores[0]*1000)/1000.0
  ovassists += math.ceil(s.scores[1]*1000)/1000.0
  ovrebounds += math.ceil(s.scores[2]*1000)/1000.0
  ovsteals += math.ceil(s.scores[3]*1000)/1000.0
  ovblocks += math.ceil(s.scores[4]*1000)/1000.0
  ovturnovers += math.ceil(s.scores[5]*1000)/1000.0
  ovfgp += math.ceil(s.scores[6]*1000)/1000.0
  ovftp += math.ceil(s.scores[7]*1000)/1000.0
  ovtpm += math.ceil(s.scores[8]*1000)/1000.0
ou.write(str(ovpoints) + '\t' + str(ovassists) + '\t' + str(ovrebounds) + '\t' + str(ovsteals) + '\t' + str(ovblocks) + '\t' + str(ovturnovers) + '\t' + str(ovfgp) + '\t' + str(ovftp) + '\t' + str(ovtpm))
