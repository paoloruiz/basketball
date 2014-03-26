import math
import sys
from copy import deepcopy
from numpy import array
from scipy.cluster.vq import kmeans, whiten
 
arr = []
arrs = []
names = []
for year in range(2009, 2013):
  f = open(str(year) + 'perGameStats.txt', 'r')
  for line in f:
    split = line.split('\t')
    #points
    arr.append(float(split[28][:len(split[28])-1]))
    #rebounds
    #arr.append(float(split[22]))
    #oreb
    arr.append(float(split[20]))
    #dreb
    arr.append(float(split[21]))
    #assists
    arr.append(float(split[23]))
    #steals
    arr.append(float(split[24]))
    #blocks
    arr.append(float(split[25]))
    #fgp
    #arr.append(float(split[12]))
    #ftp
    #arr.append(float(split[19]))
    #turnovers
    arr.append(float(split[26]))
    #pfs
    arr.append(float(split[27]))
    #fgm
    arr.append(float(split[10]))
    #fga
    arr.append(float(split[11]))
    #ftm
    arr.append(float(split[17]))
    #fta
    arr.append(float(split[18]))
    #3pm
    arr.append(float(split[13]))
    #3pa
    arr.append(float(split[14]))
    arrs.append(deepcopy(arr))
    arr = []
    names.append(split[1][:len(split[1])-1] + str(year))# + '-' + split[3])
  f.close()
whitened = whiten(array(arrs))
cores,_ = kmeans(whitened, 10, 50)
playerGroups = dict()
for i in range(len(whitened)):
  player = whitened[i]
  minVal = float('inf')
  minGroup = 0
  for j in range(len(cores)):
    overall = 0.0
    for k in range(len(whitened[i])):
      overall += (whitened[i][k] - cores[j][k])*(whitened[i][k] - cores[j][k])
    v = math.sqrt(overall)
    if minVal > v:
      minVal = v
      minGroup = j+1
  print names[i] + '  ' + str(minGroup)
  playerGroups[names[i]] = minGroup
f.close()
lineup = []
lineupAvg = dict()
lineupCount = dict()
for year in range(2009, 2013):
  g = open(str(year) + 'parsedlineups.txt', 'r')
  for line in g:
    st = line.split('\t')
    players = st[0].split(',')
    for playa in players:
      lineup.append(playerGroups[playa + str(year)])
    lineup.sort()
    if str(lineup) not in lineupCount:
      lineupCount[str(lineup)] = 1
      lineupAvg[str(lineup)] = float(st[1])
    else:
      newAvg = lineupAvg[str(lineup)] * lineupCount[str(lineup)]
      lineupCount[str(lineup)] = lineupCount[str(lineup)] + 1
      lineupAvg[str(lineup)] = (newAvg + float(st[1]))/lineupCount[str(lineup)]
    lineup = []
  g.close()
for work in lineupCount:
  print work + ': ' + str(lineupCount[work]) + '\t' + str(lineupAvg[work])
