class NbaPlayer:
  def __init__(self, name, position, year, season):
    self.name = name
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

  def __gt__(self, otherPlayer):
    return self.name > otherPlayer.name

  def __ge__(self, otherPlayer):
    return self.name >= otherPlayer.name

  def __lt__(self, otherPlayer):
    return self.name < otherPlayer.name

  def __le__(self, otherPlayer):
    return self.name <= otherPlayer.name

  def __eq__(self, otherPlayer):
    return self.name == otherPlayer.name

  def __ne__(self, otherPlayer):
    return self.name != otherPlayer.name

  def __cmp__(self, otherPlayer):
    if self > otherPlayer:
      return 1
    elif self < otherPlayer:
      return -1
    else:
      return 0
