import sys
per = dict()
for year in range(2001, 2014):
  """
  f = open('advanced/' + str(year) + 'advanced.txt', 'r')
  for line in f:
    m = line.split('\t')
    per[m[1].strip()+ str(year)] = float(m[7])
  f.close()
  """
  f = open('rapm/' + str(year) + 'rapm.txt', 'r')
  for line in f:
    m = line.split('\t')
    per[m[0].strip() + str(year)] = float(m[3])
  f.close()
for year in range(2001, 2014):
  f = open('lineup/' + str(year) + 'lineups.txt', 'r')
  for line in f:
    m = line.split('\t')
    if float(m[5]) < 200.0:
      continue
    players = m[1].split('|')
    totPer = 0.0
    for player in players:
      player = player.strip()
      totPer += per[player + str(year)]
    print str(totPer) + '\t' + m[19].replace('\n', '')
  f.close()
