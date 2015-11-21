import os
import sys
import time
import AdvancedReferenceColumns
from season import Season
from nbaplayer import NbaPlayer
from score import Score

start = time.clock()

first_year = 1990
last_year = 2014
players = []
all_seasons_by_age = dict()
for year in range(first_year, last_year + 1):
  this_season = Season()
  sorted_players = this_season.calcSeason('season/' + str(year) + 'Stats.txt', year)
  for player in sorted_players:
    seasons = player.getSeason(year)
    hold = dict()
    if int(seasons.age) in all_seasons_by_age:
      hold = all_seasons_by_age[int(seasons.age)]
    hold[seasons] = player
    all_seasons_by_age[int(seasons.age)] = hold
    if player in players:
      player_season = players[players.index(player)]
      player_season.addPSeason(year, player)
      players[players.index(player)] = player_season
    else:
      players.append(player)

for year in range(first_year, last_year + 1):
  advanced_file = open('season/' + str(year) + 'AdvancedStats.txt', 'r')
  for line in advanced_file:
    advanced_stats = line.split('\t')
    player_name = advanced_stats[AdvancedReferenceColumns.name]
    player_index = players.index(player_name)
    player_season = players[player_index].getSeason(year)
    player_season.setPer(advanced_stats[AdvancedReferenceColumns.per.value])
    player_season.setBpm(advanced_stats[AdvancedReferenceColumns.bpm.value])
    player_season.setVorp(advanced_stats[AdvancedReferenceColumns.vorp.value])
    player = players[player_index]
    player.addSeason(player_season)
    players[player_index] = player
  advanced_file.close()

pers = []
per_min = 300.0
per_max = -300.0
bpms = []
bpm_min = 300.0
bpm_max = -300.0
vorps = []
vorp_min = 300.0
vorp_max = -300.0
for player in players:
  year = player.getFirstYear()
  while player.hasSeason(year + 1):
    this_season = player.getSeason(year)
    next_season = player.getSeason(year + 1)
    pers.append((this_season.getPer(), next_season.mp))
    bpms.append((this_season.getBpm(), next_season.mp))
    vorps.append((this_season.getVorp(), next_season.mp))
    per_min = min(per_min, this_season.getPer())
    per_max = max(per_min, this_season.getPer())
    bpm_min = min(per_min, this_season.getBpm())
    bpm_max = max(per_min, this_season.getBpm())
    vorp_min = min(per_min, this_season.getVorp())
    vorp_max = max(per_min, this_season.getVorp())

print 'per_min: ' + str(per_min)
print 'per_max: ' + str(per_max)
print 'bpm_min: ' + str(bpm_min)
print 'bpm_max: ' + str(bpm_max)
print 'vorp_min: ' + str(vorp_min)
print 'vorp_max: ' + str(vorp_max)

end = time.clock()

print 'time: ' + str(end-start)
