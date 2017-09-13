import os
import sys
import time
from AdvancedReferenceColumns import AdvancedReferenceColumns
from season import Season
from nbaplayer import NbaPlayer
from score import Score

def parseSeasons():
  start = time.clock()

  first_year = 2000
  last_year = 2017
  min_minutes_played = 10.0
  min_games = 20
  players = []
  all_seasons_by_age = dict()
  for year in range(first_year, last_year + 1):
    this_season = Season()
    try:
      sorted_players = this_season.calcSeason('season/' + str(year) + 'Stats.txt', year, min_minutes_played, min_games)
    except IndexError:
      print(str(year))
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
      if fake_player not in players:
        continue
      player_index = players.index(fake_player)
      if not players[player_index].hasSeason(year):
        continue
      player_season = players[player_index].getSeason(year)
      player_season.setPer(float(advanced_stats[AdvancedReferenceColumns.per.value]))
      player_season.setBpm(float(advanced_stats[AdvancedReferenceColumns.bpm.value]))
      player_season.setVorp(float(advanced_stats[AdvancedReferenceColumns.vorp.value]))
      player = players[player_index]
      player.addSeason(year, player_season)
      players[player_index] = player
    advanced_file.close()

  end = time.clock()
  print 'time: ' + str(end-start)
  return players
