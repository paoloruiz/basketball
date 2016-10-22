import os
import sys
from season import Season
from nbaplayer import NbaPlayer
from score import Score
firstYear = 1990
lastYear = 2013
lastSeason = []
players = []
all_seasons_by_age = dict()
for year in range(firstYear, lastYear+1):
  se = Season()
  sortedPlayers = se.calcSeason('season/' + str(year) + 'Stats.txt', year
  for pa in sortedPlayers:
    ses = pa.getSeason(year)
    hold = dict()
    if int(ses.age) in all_seasons_by_age:
      hold = all_seasons_by_age[int(ses.age)]
    hold[ses] = pa
    all_seasons_by_age[int(ses.age)] = hold
    if pa in players:
      pl_sea = players[players.index(pa)]
      pl_sea.addPSeason(year, pa)
      players[players.index(pa)] = pl_sea
    else:
      players.append(pa)

lastSeason = se.calcSeason('season/lastStats.txt', year)

n = open('season/nextSeason.txt', 'w')
for pa in lastSeason:
  #skip if they played less than 10 minutes per game last season
  if pa.getSeason(lastYear).mp < 10.0:
    print "Skipping " + pa.getSeason(lastYear).name
    continue

  similar_seasons_se = dict()
  similar_seasons_pa = dict()
  se = pa.getSeason(lastYear)
  testSeason = se.to_array()
  closeAgeYoung = dict()
  if int(se.age)-1 in all_seasons_by_age:
    closeAgeYoung = all_seasons_by_age[int(se.age)-1]
  closeAge = dict()
  if int(se.age) in all_seasons_by_age:
    closeAge = all_seasons_by_age[int(se.age)]
  closeAgeOld = dict()
  if int(se.age)+1 in all_seasons_by_age:
    closeAgeOld = all_seasons_by_age[int(se.age)+1]
  temp = dict(closeAgeYoung , **closeAge)
  testSeasons = dict(temp, **closeAgeOld)
  keys = testSeasons.keys()
  for k in keys:
    y = k.year
    p = testSeasons[k]
    if not p.hasSeason(y+1):
      continue
    p_season = k.to_array()
    sco = k.rev_similarity(testSeason, p_season)
    similar_seasons_se[sco] = k
    similar_seasons_pa[sco] = p
  scores = similar_seasons_se.keys()
  sorted(scores)
  mult = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
  le = 10
  if len(scores) < 10:
    le = len(scores)
  b = le
  for i in range(b):
    nexSeason = similar_seasons_pa[scores[i]].getSeason(similar_seasons_se[scores[i]].year+1)
    if similar_seasons_se[scores[i]].points == 0.0:
      le += -1
      continue
    if similar_seasons_se[scores[i]].assists == 0.0:
      le += -1
      continue
    if similar_seasons_se[scores[i]].rebounds == 0.0:
      le += -1
      continue
    if similar_seasons_se[scores[i]].steals == 0.0:
      le += -1
      continue
    if similar_seasons_se[scores[i]].blocks == 0.0:
      le += -1
      continue
    if similar_seasons_se[scores[i]].turnovers == 0.0:
      le += -1
      continue
    if similar_seasons_se[scores[i]].fgp == 0.0:
      le += -1
      continue
    if similar_seasons_se[scores[i]].ftp == 0.0:
      le += -1
      continue
    if similar_seasons_se[scores[i]].tpm == 0.0:
      le += -1
      continue
    mult[0] += (nexSeason.points)-(similar_seasons_se[scores[i]].points)
    mult[1] += (nexSeason.assists)-(similar_seasons_se[scores[i]].assists)
    mult[2] += (nexSeason.rebounds)-(similar_seasons_se[scores[i]].rebounds)
    mult[3] += (nexSeason.steals)-(similar_seasons_se[scores[i]].steals)
    mult[4] += (nexSeason.blocks)-(similar_seasons_se[scores[i]].blocks)
    mult[5] += (nexSeason.turnovers)-(similar_seasons_se[scores[i]].turnovers)
    mult[6] += (nexSeason.fgp)-(similar_seasons_se[scores[i]].fgp)
    mult[7] += (nexSeason.ftp)-(similar_seasons_se[scores[i]].ftp)
    mult[8] += (nexSeason.tpm)-(similar_seasons_se[scores[i]].tpm)
  if le == 0:
    print(se.name + " skipped due to no scores???")
    continue
  mult[0] = mult[0]/le
  mult[1] = mult[1]/le
  mult[2] = mult[2]/le
  mult[3] = mult[3]/le
  mult[4] = mult[4]/le
  mult[5] = mult[5]/le
  mult[6] = mult[6]/le
  mult[7] = mult[7]/le
  mult[8] = mult[8]/le
  n.write(se.name + "\t" + str(se.points+mult[0]) + "\t" + str(se.assists+mult[1]) + "\t" + str(se.rebounds+mult[2]) + "\t" + str(se.steals+mult[3]) + "\t" + str(se.blocks+mult[4]) + "\t" + str(se.turnovers+mult[5]) + "\t" + str(se.fgp+mult[6]) + "\t" + str(se.ftp+mult[7]) + "\t" + str(se.tpm+mult[8]) + "\t" + str(pa.position) + "\n")
n.close()
