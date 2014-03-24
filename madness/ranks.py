#!usr/bin/python
import sys
from team import Team
from game import Game
from pagerank import PageRank
from numpy import array, ones, linalg
from copy import deepcopy

names = dict()
e = open('teamname.txt', 'r')
for name in e:
  sp = name.split('\t')
  names[sp[0]] = sp[1][0:len(sp[1])-1]
f = open('bballregseason.txt', 'r')
seasons = []
curseason = 'A'
seas = dict() #team, score
for line in f:
  gam = line.split('\t')
  if curseason is not gam[0]:
    if len(seas.keys()) > 0:
      seasons.append(deepcopy(seas))
    seas.clear()
    curseason = gam[0]
  if gam[2] in seas:
    team1 = seas[gam[2]]
  else:
    team1 = Team(names[gam[2]])
  if gam[4] in seas:
    team2 = seas[gam[4]]
  else:
    team2 = Team(names[gam[4]])
  team1.addGame(Game(gam[4], gam[3], gam[5]))
  team2.addGame(Game(gam[2], gam[5], gam[3]))
  seas[gam[2]] = deepcopy(team1)
  seas[gam[4]] = deepcopy(team2)
seasons.append(deepcopy(seas))
#seas.clear()

for i in range(2, len(seasons)):
  seaso = seasons[i]
  q = open(str(1996 + i) + 'se.txt', 'r')
  teamStats = dict()
  for lines in q:
    stat = lines.split('\t')
    teamStats[stat[1]] = lines
  for team in seaso.keys():
    if team not in teamStats:
      continue
    sta = teamStats[team].split('\t')
    teamNode = seaso[team]
    teamNode.blocks = float(sta[30])/float(sta[2])
    teamNode.rebounds = float(sta[27])/float(sta[2])
    teamNode.turnovers = float(sta[31])/float(sta[2])
    teamNode.assists = float(sta[28])/float(sta[2])
    teamNode.steals = float(sta[29])/float(sta[2])
    seasons[i][team] = deepcopy(teamNode)


seedsF = open('pastseeds.txt', 'r')
seCur = 'd'
indCur = -1
seSeed = seasons[0]
for line in seedsF:
  gal = line.split('\t')
  if seCur not in gal[0]:
    if indCur != -1:
      seasons[indCur] = deepcopy(seSeed)
    seCur = gal[0]
    indCur += 1
    seSeed = deepcopy(seasons[indCur])
  te = gal[2][0:3]
  seSeed[te].seed = float(gal[1][1:3])
seasons[indCur] = deepcopy(seSeed)
#j = seasons[0]
pr = PageRank()
#m = pr.rank(j)
#new_dict = dict(zip(m.values(), m.keys()))
#sorted_arr = sorted(new_dict.keys())

#for n in reversed(sorted_arr):
#  print names[new_dict[n]] + " " + str(n)
mad = open('madresults.txt', 'r')
curseason = '0'
curInd = -1
correct = 0
wrong = 0
correctAvg = 0.0
overCorrect = 0
wrongAvg = 0.0
lowestWrong = 0.0
curSe = seasons[0]
s = pr.rank(curSe)
winsPredict = dict()
countPredict = dict()
count = 0
rest = 0
restWins = 0
for res in mad:
  gam = res.split('\t')
  if curseason is not gam[0]:
    curseason = gam[0]
    curInd += 1
    curSe = seasons[curInd]
    s = pr.rank(curSe)
    overCorrect += correct
    #if curInd is not 0:
      #print 'The average for wins in season ' + str(curInd + 1995) + ' is ' + str(correctAvg/correct) + ' with ' + str(correct) + ' correct. Wrong is ' + str(wrongAvg/wrong) + ' with ' + str(wrong) + ' wrong and a low of ' + str(lowestWrong) + '. correct percentage is ' + str(float(correct)/(correct + wrong))
    correct = 0
    wrong = 0
    correctAvg = 0.0
    wrongAvg = 0.0
    lowestWrong = 0.0
  firstTeam = gam[2]
  favSco = curSe[firstTeam].getScores()
  firstScore = int(gam[3])
  secondTeam = gam[4]
  savSco = curSe[secondTeam].getScores()
  secondScore = int(gam[5])
  firstSeed = curSe[firstTeam].seed
  secondSeed = curSe[secondTeam].seed
  fSuperScore = s[firstTeam]*(169.6) + favSco[0]*0.0701 - firstSeed*0.0011 + curSe[firstTeam].assists*0.123 + curSe[firstTeam].blocks*0.5
  sSuperScore = s[secondTeam]*(169.6) + savSco[0]*0.0701 - secondSeed*0.0011 + curSe[secondTeam].assists*0.123 + curSe[secondTeam].blocks*0.5
  if firstScore > secondScore:
    if fSuperScore > sSuperScore:
      if firstSeed != secondSeed and firstSeed + secondSeed != 17.0:
        restWins += 1
        rest += 1
      if firstSeed > secondSeed:
        keS = str(firstSeed) + '-' + str(secondSeed)
        if keS in winsPredict:
          winsPredict[keS] += 1
        else:
          winsPredict[keS] = 1
      else:
        keS = str(secondSeed) + '-' + str(firstSeed)
        if keS in winsPredict:
          winsPredict[keS] += 1
        else:
          winsPredict[keS] = 1
      if keS in countPredict:
        countPredict[keS] += 1
      else:
        countPredict[keS] = 1
      correct += 1
      correctAvg += fSuperScore - sSuperScore
    else:
      if firstSeed != secondSeed and firstSeed + secondSeed != 17.0:
        rest += 1
      if firstSeed == 11.0 and secondSeed == 6.0:
        count += 1
      if firstSeed > secondSeed:
        keS = str(firstSeed) + '-' + str(secondSeed)
      else:
        keS = str(secondSeed) + '-' + str(firstSeed)
      if keS in countPredict:
        countPredict[keS] += 1
      else:
        countPredict[keS] = 1
      wrong += 1
      wrongAvg += sSuperScore - fSuperScore
      if sSuperScore - fSuperScore > lowestWrong:
        lowestWrong = sSuperScore - fSuperScore
overCorrect += correct
#print 'The average for wins in season ' + str(curInd + 1996) + ' is ' + str(correctAvg/correct) + ' with ' + str(correct) + ' correct. Wrong is ' + str(wrongAvg/wrong) + ' with ' + str(wrong) + ' wrong and a low of ' + str(lowestWrong) + '. correct percentage is ' + str(float(correct)/(correct + wrong))
#print 'Overal Correctness: ' + str(overCorrect)
for matchup in countPredict:
  if float(matchup[0:matchup.index('-')]) + float(matchup[matchup.index('-')+1:]) != 17.0:
    continue
  if matchup in winsPredict:
    print matchup + ' matchup has ' + str(winsPredict[matchup]) + '/' + str(countPredict[matchup]) + ' = ' + str(float(winsPredict[matchup])/countPredict[matchup])
  else:
    print matchup + ' matchup has 0/' + str(countPredict[matchup]) + ' = 0'
print float(restWins)/rest
