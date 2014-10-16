class DraftPlayer:
  def __init__(self, name, pts, ast, reb, stl, blk, tos, fgp, ftp, tpm):
    self.name = name
    self.scores = [pts, ast, reb, stl, blk, tos, fgp, ftp, tpm]

  def getScores(self):
    return self.scores
