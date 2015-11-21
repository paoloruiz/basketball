class NbaPlayer:
  def __init__(self, name, position, year, season):
    self.name = name.strip()
    self.position = position
    self.seasons = {}
    self.seasons[year] = season
    self.first_year = year

  def getSeason(self, year):
    return self.seasons[year]

  def addSeason(self, year, season):
    self.seasons[year] = season
    self.first_year = min(self.first_year, year)

  def hasSeason(self, year):
    return year in self.seasons

  def addPSeason(self, year, player):
    self.seasons[year] = player.getSeason(year)
    self.first_year = min(self.first_year, year)

  def getFirstYear(self):
    return self.first_year

  def __gt__(self, other_player):
    return self.name > other_player.name

  def __ge__(self, other_player):
    return self.name >= other_player.name

  def __lt__(self, other_player):
    return self.name < other_player.name

  def __le__(self, other_player):
    return self.name <= other_player.name

  def __eq__(self, other_player):
    return self.name == other_player.name

  def __ne__(self, other_player):
    return self.name != other_player.name

  def __cmp__(self, other_player):
    if self > other_player:
      return 1
    elif self < other_player:
      return -1
    else:
      return 0
