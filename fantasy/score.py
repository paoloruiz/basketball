class Score:
  def __init__(self, name, score, extra = 0.0):
    self.name = name
    self.score = score
    self.extra = extra
  def __gt__(self, nb2):
    return self.score < nb2.score
  def __ge__(self, nb2):
    return self.score <= nb2.score
  def __lt__(self, nb2):
    return self.score > nb2.score
  def __le__(self, nb2):
    return self.score >= nb2.score
  def __eq__(self, nb2):
    return self.score == nb2.score
  def __ne__(self, nb2):
    return self.score != nb2.score
  def __cmp__(self, nb2):
    if self > nb2:
      return 1
    elif self < nb2:
      return -1
    else:
      return 0
