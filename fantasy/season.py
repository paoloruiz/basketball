import os
import sys
import math
from itertools import izip
from nbaplayer import NbaPlayer
class Season:
  def __init__(self, age = None, year = None, name = None, position = None, point = None, assist = None, rebound = None, steal = None, block = None, turnover = None, fg = None, ft = None, tp = None):
    if age is None:
      return
    self.age = age
    self.year = year
    self.name = name
    self.positions = position.split(',')
    self.points = point
    self.assists = assist
    self.rebounds = rebound
    self.steals = steal
    self.blocks = block
    self.turnovers = turnover
    self.fgp = fg
    self.ftp = ft
    self.tpm = tp
    self.scores = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

  def calcZ(self, apoint, stdp, aassist, stda, arebound, stdr, asteal, stds, ablock, stdb, aturnover, stdt, afgp, stdfg, aftp, stdft, atpm, stdtp):
    self.scores[0] = (self.points - apoint)/stdp
    self.scores[1] = (self.assists - aassist)/stda
    self.scores[2] = (self.rebounds - arebound)/stdr
    self.scores[3] = (self.steals - asteal)/stds
    self.scores[4] = (self.blocks - ablock)/stdb
    self.scores[5] = -(self.turnovers - aturnover)/stdt
    self.scores[6] = (self.fgp - afgp)/stdfg
    self.scores[7] = (self.ftp - aftp)/stdft
    self.scores[8] = (self.tpm - atpm)/stdtp

  def zScore(self, a = 1.0, b = 1.0, c = 1.0, d = 1.0, e = 1.0, f = 1.0, g = 1.0, h = 1.0, i = 1.0):
    return self.scores[0]*a + self.scores[1]*b + self.scores[2]*c + self.scores[3]*d + self.scores[4]*e + self.scores[5]*f + self.scores[6]*g + self.scores[7]*h + self.scores[8]*i

  def __gt__(self, nb2):
    return self.zScore(1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0) > nb2.zScore(1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0)

  def __ge__(self, nb2):
    return self.zScore(1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0) >= nb2.zScore(1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0)

  def __lt__(self, nb2):
    return self.zScore(1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0) < nb2.zScore(1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0)

  def __le__(self, nb2):
    return self.zScore(1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0) <= nb2.zScore(1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0)

  def __eq__(self, nb2):
    return self.zScore(1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0) == nb2.zScore(1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0)

  def __ne__(self, nb2):
    return self.zScore(1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0) != nb2.zScore(1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0)

  def __cmp__(self, nb2):
    if self > nb2:
      return 1
    elif self < nb2:
      return -1
    else:
      return 0

  def __str__(self):
    return str(self.age) + str(self.year) + str(self.name) + str(self.positions) + str(self.points) + str(self.assists) + str(self.rebounds) + str(self.steals) + str(self.blocks) + str(self.turnovers) + str(self.fgp) + str(self.ftp) + str(self.tpm)

  def __hash__(self):
    return (hash(str(self)))

  def to_array(self):
    x = []
    x.append(self.points)
    x.append(self.assists)
    x.append(self.rebounds)
    x.append(self.blocks)
    x.append(self.steals)
    x.append(self.tpm)
    x.append(self.fgp)
    x.append(self.ftp)
    x.append(self.turnovers)
    return x

  def dot_product(self, v1, v2):
    return sum(map(lambda x: x[0] * x[1], izip(v1, v2)))

  def rev_similarity(self, v1,v2):
    prod = self.dot_product(v1, v2)
    len1 = math.sqrt(self.dot_product(v1, v1))
    len2 = math.sqrt(self.dot_product(v2, v2))
    if len1*len2 == 0:
      return 1.0
    return prod/(len1*len2)

  def calcSeason(self, filName, year, a, b, c, d, e, f, g, h, i, j, k, l):
    fil = open(filName, 'r')
    players = []
    points = 0.0
    assists = 0.0
    rebounds = 0.0
    steals = 0.0
    blocks = 0.0
    turnovers = 0.0
    fg = 0.0
    ft = 0.0
    tp = 0.0
    plNum = 0
    for line in fil:
      #player - name position year season
      sea = line.split('\t');
      #season - age, year, name, position, point, assist, rebound, steal, block, turnover, fg, ft, tp
      season = Season(sea[a], year, sea[b], str(sea[c]), float(sea[d]), float(sea[e]), float(sea[f]), float(sea[g]), float(sea[h]), float(sea[i]), float(sea[j]), float(sea[k]), float(sea[l]))
      points += float(sea[d])
      assists += float(sea[e])
      rebounds += float(sea[f])
      steals += float(sea[g])
      blocks += float(sea[h])
      turnovers += float(sea[i])
      fg += float(sea[j])
      ft += float(sea[k])
      tp += float(sea[l])
      season.calcZ(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
      player = NbaPlayer(sea[b], sea[c], year, season)
      players.append(player);
      plNum += 1
    retPlayers = []
    stdp = 0.0
    stda = 0.0
    stdr = 0.0
    stds = 0.0
    stdb = 0.0
    stdt = 0.0
    stdfg = 0.0
    stdft = 0.0
    stdtp = 0.0
    points = points/plNum
    assists = assists/plNum
    rebounds = rebounds/plNum
    steals = steals/plNum
    blocks = blocks/plNum
    turnovers = turnovers/plNum
    fg = fg/plNum
    ft = ft/plNum
    tp = tp/plNum
    for pa in players:
      se = pa.getSeason(year)
      stdp += ((se.points - points) * (se.points - points))
      stda += ((se.assists - assists) * (se.assists - assists))
      stdr += ((se.rebounds - rebounds) * (se.rebounds - rebounds))
      stds += ((se.steals - steals) * (se.steals - steals))
      stdb += ((se.blocks - blocks) * (se.blocks - blocks))
      stdt += ((se.turnovers - turnovers) * (se.turnovers - turnovers))
      stdfg += ((se.fgp - fg) * (se.fgp - fg))
      stdft += ((se.ftp - ft) * (se.ftp - ft))
      stdtp += ((se.tpm - tp) * (se.tpm - tp))
    stdp = stdp/plNum
    stda = stda/plNum
    stdr = stdr/plNum
    stds = stds/plNum
    stdb = stdb/plNum
    stdt = stdt/plNum
    stdfg = stdfg/plNum
    stdft = stdft/plNum
    stdtp = stdtp/plNum
    for pa in players:
      se = pa.getSeason(year)
      se.calcZ(points, math.sqrt(stdp), assists, math.sqrt(stda), rebounds, math.sqrt(stdr), steals, math.sqrt(stds), blocks, math.sqrt(stdb), turnovers, math.sqrt(stdt), fg, math.sqrt(stdfg), ft, math.sqrt(stdft), tp, math.sqrt(stdtp))
      pa.addSeason(year, se)
      retPlayers.append(pa)
    fil.close()
    return retPlayers
