import SeasonsIndex
import os
from PredictionStats import PredictionStats
players = SeasonsIndex.parseSeasons()
#Need to figure out a way to make this work with multiple different dimensions at once

statsToLoop = PredictionStats.statsToLoop.value
statsData = {}
for stat in statsToLoop:
  if not os.path.exists(stat):
    os.makedirs(stat)
  statsData[stat] = {}
  for statToGet in statsToLoop:
    statsData[stat][statToGet] = open(stat + '/' + statToGet + 'Data.txt', 'w')
for player in players:
  startYear = player.getFirstYear()
  nextYear = startYear + 1
  while player.hasSeason(nextYear):
    for i in range(0, len(statsToLoop)):
      for j in range(0, len(statsToLoop)):
        statsData[statsToLoop[i]][statsToLoop[j]].write(str(player.getSeason(startYear).getStatsByRateByInputNumber(i)) + ' ' + str(player.getSeason(nextYear).getStatsByRateByInputNumber(j)) + '\n')
    startYear += 1
    nextYear += 1

for key, files in statsData.items():
  for secondKey, fileToClose in files.items():
    fileToClose.close()
