import os
import sys
import math
from ReferenceColumns import ReferenceColumns
from itertools import izip
from nbaplayer import NbaPlayer
class Season:
  def __init__(self, age = None, year = None, name = None, position = None, point = None, assist = None, rebound = None, steal = None, block = None, turnover = None, fg = None, ft = None, tp = None, mp = None):
    if age is None:
      return
    self.age = age
    self.year = year
    self.name.value = name
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
    self.mp = mp
    self.per = 0.0
    self.vorp = 0.0
    self.bpm = 0.0
    self.scores = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

  def calcZ(self, average_points, standard_deviation_points, average_assists, standard_deviation_assists, average_rebounds, standard_deviation_rebounds, average_steals, standard_deviation_steals, average_blocks, standard_deviation_blocks, average_turnovers, standard_deviation_turnovers, average_field_goal_percentage, standard_deviation_field_goal_percentage, average_free_throw_percentage, standard_deviation_free_throw_percentage, average_three_pointers, standard_deviation_three_pointers):
    self.scores[0] = (self.points - average_points)/standard_deviation_points
    self.scores[1] = (self.assists - average_assists)/standard_deviation_assists
    self.scores[2] = (self.rebounds - average_rebounds)/standard_deviation_rebounds
    self.scores[3] = (self.steals - average_steals)/standard_deviation_steals
    self.scores[4] = (self.blocks - average_blocks)/standard_deviation_blocks
    self.scores[5] = -(self.turnovers - average_turnovers)/standard_deviation_turnovers
    self.scores[6] = (self.fgp - average_field_goal_percentage)/standard_deviation_field_goal_percentage
    self.scores[7] = (self.ftp - average_free_throw_percentage)/standard_deviation_free_throw_percentage
    self.scores[8] = (self.tpm - average_three_pointers)/standard_deviation_three_pointers

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
    return str(self.age) + str(self.year) + str(self.name.value) + str(self.positions) + str(self.points) + str(self.assists) + str(self.rebounds) + str(self.steals) + str(self.blocks) + str(self.turnovers) + str(self.fgp) + str(self.ftp) + str(self.tpm) + str(self.mp)

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

  def setPer(self, per):
    self.per = per

  def setVorp(self, vorp):
    self.vorp = vorp

  def setBpm(self, bpm):
    self.bpm = bpm

  def dot_product(self, v1, v2):
    return sum(map(lambda x: x[0] * x[1], izip(v1, v2)))

  def rev_similarity(self, v1,v2):
    prod = self.dot_product(v1, v2)
    len1 = math.sqrt(self.dot_product(v1, v1))
    len2 = math.sqrt(self.dot_product(v2, v2))
    if len1*len2 == 0:
      return 1.0
    return prod/(len1*len2)

  def calcSeason(self, season_season_file_name, year):
    season_file = open(season_season_file_name, 'r')
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
    mp = 0.0
    num_players = 0
    for line in season_file:
      #player - name position year season
      season_array = line.split('\t')
      print(season_array)
      #season - age, year, name, position, point, assist, rebound, steal, block, turnover, fg, ft, tp, mp
      season = Season(season_array[ReferenceColumns.age.value], year, season_array[ReferenceColumns.name.value], str(season_array[ReferenceColumns.positions.value]), float(season_array[ReferenceColumns.points.value]), float(season_array[ReferenceColumns.assists.value]), float(season_array[ReferenceColumns.rebounds.value]), float(season_array[ReferenceColumns.steals.value]), float(season_array[ReferenceColumns.blocks.value]), float(season_array[ReferenceColumns.turnovers.value]), float(season_array[ReferenceColumns.field_goal_percentage.value]), float(season_array[ReferenceColumns.free_throw_percentage.value]), float(season_array[ReferenceColumns.three_pointers.value]), float(season_array[ReferenceColumns.minutes_played.value]))
      points += float(season_array[ReferenceColumns.points.value])
      assists += float(season_array[ReferenceColumns.assists.value])
      rebounds += float(season_array[ReferenceColumns.rebounds.value])
      steals += float(season_array[ReferenceColumns.steals.value])
      blocks += float(season_array[ReferenceColumns.blocks.value])
      turnovers += float(season_array[ReferenceColumns.turnovers.value])
      fg += float(season_array[ReferenceColumns.field_goal_percentage.value])
      ft += float(season_array[ReferenceColumns.free_throw_percentage.value])
      tp += float(season_array[ReferenceColumns.three_pointers.value])
      mp += float(season_array[ReferenceColumns.minutes_played.value])
      season.calcZ(1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
      player = NbaPlayer(season_array[ReferenceColumns.name.value], season_array[ReferenceColumns.positions.value], year, season)
      players.append(player);
      num_players += 1
    all_players = []
    standard_deviation_points = 0.0
    standard_deviation_assists = 0.0
    standard_deviation_rebounds = 0.0
    standard_deviation_steals = 0.0
    standard_deviation_blocks = 0.0
    standard_deviation_turnovers = 0.0
    standard_deviation_field_goal_percentage = 0.0
    standard_deviation_free_throw_percentage = 0.0
    standard_deviation_three_pointers = 0.0
    points = points/num_players
    assists = assists/num_players
    rebounds = rebounds/num_players
    steals = steals/num_players
    blocks = blocks/num_players
    turnovers = turnovers/num_players
    fg = fg/num_players
    ft = ft/num_players
    tp = tp/num_players
    for player in players:
      player_season = player.getSeason(year)
      standard_deviation_points += ((player_season.points - points) * (player_season.points - points))
      standard_deviation_assists += ((player_season.assists - assists) * (player_season.assists - assists))
      standard_deviation_rebounds += ((player_season.rebounds - rebounds) * (player_season.rebounds - rebounds))
      standard_deviation_steals += ((player_season.steals - steals) * (player_season.steals - steals))
      standard_deviation_blocks += ((player_season.blocks - blocks) * (player_season.blocks - blocks))
      standard_deviation_turnovers += ((player_season.turnovers - turnovers) * (player_season.turnovers - turnovers))
      standard_deviation_field_goal_percentage += ((player_season.fgp - fg) * (player_season.fgp - fg))
      standard_deviation_free_throw_percentage += ((player_season.ftp - ft) * (player_season.ftp - ft))
      standard_deviation_three_pointers += ((player_season.tpm - tp) * (player_season.tpm - tp))
    standard_deviation_points = standard_deviation_points/num_players
    standard_deviation_assists = standard_deviation_assists/num_players
    standard_deviation_rebounds = standard_deviation_rebounds/num_players
    standard_deviation_steals = standard_deviation_steals/num_players
    standard_deviation_blocks = standard_deviation_blocks/num_players
    standard_deviation_turnovers = standard_deviation_turnovers/num_players
    standard_deviation_field_goal_percentage = standard_deviation_field_goal_percentage/num_players
    standard_deviation_free_throw_percentage = standard_deviation_free_throw_percentage/num_players
    standard_deviation_three_pointers = standard_deviation_three_pointers/num_players
    for player in players:
      player_season = player.getSeason(year)
      player_season.calcZ(points, math.sqrt(standard_deviation_points), assists, math.sqrt(standard_deviation_assists), rebounds, math.sqrt(standard_deviation_rebounds), steals, math.sqrt(standard_deviation_steals), blocks, math.sqrt(standard_deviation_blocks), turnovers, math.sqrt(standard_deviation_turnovers), fg, math.sqrt(standard_deviation_field_goal_percentage), ft, math.sqrt(standard_deviation_free_throw_percentage), tp, math.sqrt(standard_deviation_three_pointers))
      player.addSeason(year, player_season)
      all_players.append(player)
    season_file.close()
    return all_players
