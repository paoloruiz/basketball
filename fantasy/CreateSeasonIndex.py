import os
import sys
import time
from AdvancedReferenceColumns import AdvancedReferenceColumns
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
    player_name = advanced_stats[AdvancedReferenceColumns.name.value]
    fake_player = NbaPlayer(player_name, 'PG', 1990, {})
    player_index = players.index(fake_player)
    player_season = players[player_index].getSeason(year)
    player_season.setPer(float(advanced_stats[AdvancedReferenceColumns.per.value]))
    player_season.setBpm(float(advanced_stats[AdvancedReferenceColumns.bpm.value]))
    player_season.setVorp(float(advanced_stats[AdvancedReferenceColumns.vorp.value]))
    player = players[player_index]
    player.addSeason(year, player_season)
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
    per = this_season.per
    bpm = this_season.bpm
    vorp = this_season.vorp
    mp = next_season.mp
    pers.append((per, mp))
    bpms.append((bpm, mp))
    vorps.append((vorp, mp))
    if per < per_min:
      per_min = per
    if per > per_max:
      per_max = per
    if bpm < bpm_min:
      bpm_min = bpm
    if bpm > bpm_max:
      bpm_max = bpm
    if vorp < vorp_min:
      vorp_min = vorp
    if vorp > vorp_max:
      vorp_max = vorp
    year = year + 1

print 'per_min: ' + str(per_min)
print 'per_max: ' + str(per_max)
print 'bpm_min: ' + str(bpm_min)
print 'bpm_max: ' + str(bpm_max)
print 'vorp_min: ' + str(vorp_min)
print 'vorp_max: ' + str(vorp_max)

per_file = open('per.txt', 'w')
for pair in pers:
  per_file.write(str(pair) + '\n')
per_file.close()

bpm_file = open('bpm.txt', 'w')
for pair in bpms:
  bpm_file.write(str(pair) + '\n')
bpm_file.close()

vorp_file = open('vorp.txt', 'w')
for pair in vorps:
  vorp_file.write(str(pair) + '\n')
vorp_file.close()

end = time.clock()

print 'time: ' + str(end-start)
