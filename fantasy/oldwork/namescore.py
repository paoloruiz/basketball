class NameScore:
  def __init__(self, name, score):
    self.name = name
    self.score = score
  def __gt__(self, nb2):
    return self.name < nb2.name
  def __ge__(self, nb2):
    return self.name <= nb2.name
  def __lt__(self, nb2):
    return self.name > nb2.name
  def __le__(self, nb2):
    return self.name >= nb2.name
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
