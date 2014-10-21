#do this
import operator
from draftPlayer import DraftPlayer
from draftRanks import DraftRanks
from season import Season
from otherDraft import OtherDraft
from userTeam import UserTeam
def printStats():
  elynn.printScores()
  print
  michael.printScores()
  print
  paolo.printScores()

def printDesired(players):
  print 'Desired players'
  numPlayersLeft = 14 - len(paolo.players)
  #Use arrays!
  goalScores = [15.837, 14.064, 17.998, 17.37, 13.207, -7.423, 5.507, 6.588, 13.611]
  avgScores = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
  avgScores[0] = goalScores[0] - ((numPlayersLeft * ptsAvg) + paolo.scores[0])
  avgScores[1] = goalScores[1] - ((numPlayersLeft * astAvg) + paolo.scores[1])
  avgScores[2] = goalScores[2] - ((numPlayersLeft * rebAvg) + paolo.scores[2])
  avgScores[3] = goalScores[3] - ((numPlayersLeft * stlAvg) + paolo.scores[3])
  avgScores[4] = goalScores[4] - ((numPlayersLeft * blkAvg) + paolo.scores[4])
  avgScores[5] = goalScores[5] - ((numPlayersLeft * tosAvg) + paolo.scores[5])
  avgScores[6] = goalScores[6] - ((numPlayersLeft * fgpAvg) + paolo.scores[6])
  avgScores[7] = goalScores[7] - ((numPlayersLeft * ftpAvg) + paolo.scores[7])
  avgScores[8] = goalScores[8] - ((numPlayersLeft * tpmAvg) + paolo.scores[8])
  print 'Average Scores left: ' + str(avgScores)
  mods = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
  for i in range(0,9):
    if avgScores[i] / goalScores[i] > 0.2:
      mods[i] = 2.0
    elif avgScores[i] / goalScores[i] > 0.1:
      mods[i] = 1.5
  des = paolo.getDesirabilities(players, mods)
  for i in range(0,20):
    print des[i][0] + '- ' + str(des[i][1])

dr = DraftRanks()
year = 2013
se = Season()
sortedPlayers = se.calcSeason('season/thisStats2.txt', year, 3, 1, 2, 28, 23, 22, 24, 25, 26, 10, 19, 11, 7)
players = {}
#Set up the stats for calculating when a stat is low
#turn these into arrays
pts = {}
ast = {}
reb = {}
stl = {}
blk = {}
tos = {}
fgp = {}
ftp = {}
tpm = {}
ptsAvg = 0.0
astAvg = 0.0
rebAvg = 0.0
stlAvg = 0.0
blkAvg = 0.0
tosAvg = 0.0
fgpAvg = 0.0
ftpAvg = 0.0
tpmAvg = 0.0
ptsNum = 0.0
astNum = 0.0
rebNum = 0.0
stlNum = 0.0
blkNum = 0.0
tosNum = 0.0
fgpNum = 0.0
ftpNum = 0.0
tpmNum = 0.0
for pla in sortedPlayers:
  pl = pla.getSeason(year)
  players[pl.name] = DraftPlayer(pla.name, pl.scores[0], pl.scores[1], pl.scores[2], pl.scores[3], pl.scores[4], pl.scores[5], pl.scores[6], pl.scores[7], pl.scores[8])
  pts[pl.name] = pl.scores[0]
  ast[pl.name] = pl.scores[1]
  reb[pl.name] = pl.scores[2]
  stl[pl.name] = pl.scores[3]
  blk[pl.name] = pl.scores[4]
  tos[pl.name] = pl.scores[5]
  fgp[pl.name] = pl.scores[6]
  ftp[pl.name] = pl.scores[7]
  tpm[pl.name] = pl.scores[8]

pts = sorted(pts.items(), key=operator.itemgetter(1), reverse=True)
ast = sorted(ast.items(), key=operator.itemgetter(1), reverse=True)
reb = sorted(reb.items(), key=operator.itemgetter(1), reverse=True)
stl = sorted(stl.items(), key=operator.itemgetter(1), reverse=True)
blk = sorted(blk.items(), key=operator.itemgetter(1), reverse=True)
tos = sorted(tos.items(), key=operator.itemgetter(1), reverse=True)
fgp = sorted(fgp.items(), key=operator.itemgetter(1), reverse=True)
ftp = sorted(ftp.items(), key=operator.itemgetter(1), reverse=True)
tpm = sorted(tpm.items(), key=operator.itemgetter(1), reverse=True)

pts = dict(pts[:50])
ast = dict(ast[:50])
reb = dict(reb[:50])
stl = dict(stl[:50])
blk = dict(blk[:50])
tos = dict(tos[:50])
fgp = dict(fgp[:50])
ftp = dict(ftp[:50])
tpm = dict(tpm[:50])

for i in range(0, 50):
  if i < len(pts):
    ptsNum += 1
    ptsAvg += pts.items()[i][1]
  if i < len(ast):
    astNum += 1
    astAvg += ast.items()[i][1]
  if i < len(reb):
    rebNum += 1
    rebAvg += reb.items()[i][1]
  if i < len(stl):
    stlNum += 1
    stlAvg += stl.items()[i][1]
  if i < len(blk):
    blkNum += 1
    blkAvg += blk.items()[i][1]
  if i < len(tos):
    tosNum += 1
    tosAvg += tos.items()[i][1]
  if i < len(fgp):
    fgpNum += 1
    fgpAvg += fgp.items()[i][1]
  if i < len(ftp):
    ftpNum += 1
    ftpAvg += ftp.items()[i][1]
  if i < len(tpm):
    tpmNum += 1
    tpmAvg += tpm.items()[i][1]
ptsAvg = ptsAvg / ptsNum
astAvg = astAvg / astNum
rebAvg = rebAvg / rebNum
stlAvg = stlAvg / stlNum
blkAvg = blkAvg / blkNum
tosAvg = tosAvg / tosNum
fgpAvg = fgpAvg / fgpNum
ftpAvg = ftpAvg / ftpNum
tpmAvg = tpmAvg / tpmNum

elynn = OtherDraft('elynn')
michael = OtherDraft('michael')
paolo = UserTeam('paolo')

printDesired(players)

while (True):
  inp = raw_input()
  if 'ADD' in inp:
    line = inp.split('\t')
    if line[1] not in players:
      print 'Bad input'
      continue
    if 'elynn' in inp:
      elynn.addPlayer(line[1], players[line[1]].scores)
    if 'michael' in inp:
      michael.addPlayer(line[1], players[line[1]].scores)
    if 'paolo' in inp:
      paolo.addPlayer(line[1], players[line[1]].scores)
    printStats()
    del players[line[1]]
    if line[1] in pts:
      ptsAvg = ptsAvg * ptsNum
      ptsAvg = ptsAvg - pts[line[1]]
      ptsNum = ptsNum - 1
      ptsAvg = ptsAvg / ptsNum
      del pts[line[1]]
    if line[1] in ast:
      astAvg = astAvg * astNum
      astAvg = astAvg - ast[line[1]]
      astNum = astNum - 1
      astAvg = astAvg / astNum
      del ast[line[1]]
    if line[1] in reb:
      rebAvg = rebAvg * rebNum
      rebAvg = rebAvg - reb[line[1]]
      rebNum = rebNum - 1
      rebAvg = rebAvg / rebNum
      del reb[line[1]]
    if line[1] in stl:
      stlAvg = stlAvg * stlNum
      stlAvg = stlAvg - stl[line[1]]
      stlNum = stlNum - 1
      stlAvg = stlAvg / stlNum
      del stl[line[1]]
    if line[1] in blk:
      blkAvg = blkAvg * blkNum
      blkAvg = blkAvg - blk[line[1]]
      blkNum = blkNum - 1
      blkAvg = blkAvg / blkNum
      del blk[line[1]]
    if line[1] in tos:
      tosAvg = tosAvg * tosNum
      tosAvg = tosAvg - tos[line[1]]
      tosNum = tosNum - 1
      tosAvg = tosAvg / tosNum
      del tos[line[1]]
    if line[1] in fgp:
      fgpAvg = fgpAvg * fgpNum
      fgpAvg = fgpAvg - fgp[line[1]]
      fgpNum = fgpNum - 1
      fgpAvg = fgpAvg / fgpNum
      del fgp[line[1]]
    if line[1] in ftp:
      ftpAvg = ftpAvg * ftpNum
      ftpAvg = ftpAvg - ftp[line[1]]
      ftpNum = ftpNum - 1
      ftpAvg = ftpAvg / ftpNum
      del ftp[line[1]]
    if line[1] in tpm:
      tpmAvg = tpmAvg * tpmNum
      tpmAvg = tpmAvg - tpm[line[1]]
      tpmNum = tpmNum - 1
      tpmAvg = tpmAvg / tpmNum
      del tpm[line[1]]
    printDesired(players)
  elif 'PICK' in inp:
    line = inp.split('\t')
    if line[1] not in players:
      print 'Bad input'
      continue
    player = players[line[1]]
    mods = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    des = paolo.getDesirabilities(players, mods)
    print 'Desirability: ' + str(dr.calcDesirability(paolo.scores, player.getScores(), mods))
    print 'Index: ' + str([x[0] for x in des].index(player.name) + 1)
  else:
    print 'I couldn\'t understand you, try again'

