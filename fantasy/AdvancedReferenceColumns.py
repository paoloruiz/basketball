from enum import Enum
#The column index forbasketball reference's season page per game
class AdvancedReferenceColumns(Enum):
  rank = 0
  name = 1
  positions = 2
  age = 3
  team = 4
  games_played = 5
  minutes_played = 6
  per = 7
  true_shooting = 8
  three_point_attempt_rate = 9
  free_throw_rate = 10
  offensive_rebound_percentage = 11
  defensive_rebound_percentage = 12
  total_rebound_percentage = 13
  assist_percentage = 14
  steal_percentage = 15
  block_percentage = 16
  turnover_percentage = 17
  usage = 18
  blank = 19
  offensive_win_shares = 20
  defensive_win_shares = 21
  win_shares = 22
  win_shares_per_fortyeight = 23
  empty = 24
  offensive_bpm = 25
  defensive_bpm = 26
  bpm = 27
  vorp = 28
