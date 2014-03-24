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
f = open('2014se.txt', 'r')
seasons = []
seas = dict() #team, score
for line in f:
  gam = line.split('\t')
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
j = seas
pr = PageRank()
m = pr.rank(j)
for team in j.keys():
  print names[team] + '\t' + str(m[team]*169.6 + j[team].getScores()[0]*0.0701)
