import math
import sys
from copy import deepcopy
from numpy import array, ones
from scipy.cluster.vq import kmeans, whiten
from scipy import stats

rapm = dict()
for year in range(2001, 2014):
  f = open('rapm/' + str(year) + 'rapm.txt', 'r')
  for line in f:
    m = line.split('\t')
    rapm[m[0].strip() + str(year)] = float(m[3])
  f.close()
 
arr = []
arrs = []
names = []
for year in range(2001, 2014):
  f = open('statline/' + str(year) + 'perGameStats.txt', 'r')
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

yearTransitions = dict()

whitened = whiten(array(arrs))
cores,_ = kmeans(whitened, 13, 100)
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
  if names[i][len(names[i])-4:] in yearTransitions:
    year = yearTransitions[names[i][len(names[i])-4:]]
    player = minGroup
    year[names[i][:len(names[i])-4]] = player
    yearTransitions[names[i][len(names[i])-4:]] = deepcopy(year)
  else:
    year = dict()
    player = minGroup
    year[names[i][:len(names[i])-4]] = player
    yearTransitions[names[i][len(names[i])-4:]] = deepcopy(year)
trans = [[], [], [], [], [], [], [], [], [], [], [], [], [], []]
for year in range(2001, 2013):
  origGroup = yearTransitions[str(year)]
  nextGroup = yearTransitions[str(year+1)]
  for player in origGroup:
    if player in nextGroup:
      gro = trans[origGroup[player]]
      gro.append(nextGroup[player])
      trans[origGroup[player]] = deepcopy(gro)
for transition in range(len(trans)):
  statTrans = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  for cat in trans[transition]:
    statTrans[cat] += 1
  print 'Transitions for group ' + str(transition)
  for sta in range(len(statTrans)):
    if float(statTrans[sta]) != 0:
      print str(transition) + ' -> ' + str(sta) + ':\t' + str((100.0*float(statTrans[sta]))/sum(statTrans))
  print

f.close()
lineup = []
lineupAvg = dict()
lineupCount = dict()
lineupRapm = dict()
lineupRapmCount = dict()
for year in range(2001, 2014):
  g = open('lineup/' + str(year) + 'lineups.txt', 'r')
  for line in g:
    st = line.split('\t')
    if float(st[5]) < 200.0:
      continue
    players = st[1].split('|')
    rap = 0.0
    for playa in players:
      playa = playa.strip()
      rap += rapm[playa + str(year)]
      lineup.append(playerGroups[playa + str(year)])
    lineup.sort()
    if str(lineup) not in lineupRapm:
      lineupRapm[str(lineup)] = rap
      lineupRapmCount[str(lineup)] = 1
    else:
      lineupRapm[str(lineup)] += rap
      lineupRapmCount[str(lineup)] += 1
    if str(lineup) not in lineupCount:
      lineupCount[str(lineup)] = 1
      lineupAvg[str(lineup)] = float(st[19])
    else:
      newAvg = lineupAvg[str(lineup)] * lineupCount[str(lineup)]
      lineupCount[str(lineup)] = lineupCount[str(lineup)] + 1
      lineupAvg[str(lineup)] = (newAvg + float(st[19]))/lineupCount[str(lineup)]
    lineup = []
  g.close()
rapArr = []
avgArr = []
for work in lineupAvg:
  avgArr.append(lineupAvg[work])
  rapArr.append(lineupRapm[work]/lineupRapmCount[work])
  #if lineupCount[work] > 4:
  #  print work + ': ' + str(lineupCount[work]) + '\t' + str(lineupAvg[work]) + '\t' + str(lineupRapm[work]/lineupCount[work])

slope, intercept, r_value, p_value, std_err = stats.linregress(rapArr, avgArr)

print 'Our formula is ' + str(slope) + ' * x + ' + str(intercept)
print 'Rapm r squared is ' + str(r_value*r_value)
print 'R is ' + str(r_value)
print 'Std err: ' + str(std_err)
print

minCount = 0
if len(sys.argv) > 1:
  minCount = int(sys.argv[1])

maxCount = 100
if len(sys.argv) > 2:
  maxCount = int(sys.argv[2])

parsedLineups = dict()
for work in lineupCount:
  if lineupCount[work] > minCount and lineupCount[work] < maxCount:
    parsedLineups[work] = lineupAvg[work] - (slope*lineupRapm[work]/lineupCount[work] + intercept)

#for work in parsedLineups:
#  print work + '\t' + str(parsedLineups[work])
#print len(lineupCount)

adjLine = []
plusMinus = []
for year in range(2001, 2014):
  g = open('lineup/' + str(year) + 'lineups.txt', 'r')
  for line in g:
    lineup = []
    st = line.split('\t')
    if float(st[5]) < 200.0:
      continue
    players = st[1].split('|')
    rap = 0.0
    for playa in players:
      playa = playa.strip()
      rap += rapm[playa + str(year)]
      lineup.append(playerGroups[playa + str(year)])
    lineup.sort()
    if lineupCount[str(lineup)] <= minCount or lineupCount[str(lineup)] >= maxCount:
      continue
    if str(lineup) in parsedLineups:
      adjLine.append((slope*rap + intercept) + parsedLineups[str(lineup)])
      plusMinus.append(float(st[19].replace('\n', '')))
    else:
      adjLine.append(slope*rap + intercept)
      plusMinus.append(float(st[19].replace('\n', '')))
    lineup = []
  g.close()

slope, intercept, r_value, p_value, std_err = stats.linregress(adjLine, plusMinus)

print 'Our formula is ' + str(slope) + ' * x + ' + str(intercept)
print 'Adjusted r squared is ' + str(r_value*r_value)
print 'R is ' + str(r_value)
print 'Std err: ' + str(std_err)
