class NbaPlayer:
  def __init__(self, name, position, year, season):
    self.name = name
    self.position = position
    self.s = {}
    self.s[year] = season

  def getSeason(self, year):
    return self.s[year]

  def addSeason(self, year, season):
    self.s[year] = season

  def hasSeason(self, year):
    return year in self.s

  def addPSeason(self, year, player):
    self.s[year] = player.getSeason(year)

  def __gt__(self, nb2):
    return self.name > nb2.name

  def __ge__(self, nb2):
    return self.name >= nb2.name

  def __lt__(self, nb2):
    return self.name < nb2.name

  def __le__(self, nb2):
    return self.name <= nb2.name

  def __eq__(self, nb2):
    return self.name == nb2.name

  def __ne__(self, nb2):
    return self.name != nb2.name

  def __cmp__(self, nb2):
    if self > nb2:
      return 1
    elif self < nb2:
      return -1
    else:
      return 0
