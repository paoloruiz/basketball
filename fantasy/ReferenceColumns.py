from enum import Enum
#The column index forbasketball reference's season page per game
class ReferenceColumns(Enum):
  rank = 0
  name = 1
  positions = 2
  age = 3
  team = 4
  games_played = 5
  games_started = 6
  minutes_played = 7
  field_goals = 8
  field_goal_attempts = 9
  field_goal_percentage = 10
  three_pointers = 11
  three_pointer_attempts = 12
  three_pointer_percentage = 13
  two_pointers = 14
  two_pointer_attempts = 15
  two_pointer_percentage = 16
  effective_field_goal_percentage = 17
  free_throws = 18
  free_throw_attempts = 19
  free_throw_percentage = 20
  offensive_rebounds = 21
  defensive_rebounds = 22
  rebounds = 23
  assists = 24
  steals = 25
  blocks = 26
  turnovers = 27
  personal_fouls = 28
  points = 29
