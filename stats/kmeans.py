import math
from numpy import array
from scipy.cluster.vq import kmeans, whiten
from copy import deepcopy
f = open('statline/2013perGameStats.txt', 'r')
arrs = []
arr = []
names = []
stats = ['points', 'o reb', 'd reb', 'assists', 'steals', 'blocks', 'turnovers', 'pfs', 'fgm', 'fga', 'ftm', 'fta', '3pm', '3pa']
for line in f:
  split = line.split('\t')
  #points
  arr.append(float(split[28][:len(split[28])-1]))
  #rebounds
  #arr.append(float(split[22]))
  #oreb
  arr.append(float(split[20]))
  #dreb
  arr.append(float(split[21]))
  #assists
  arr.append(float(split[23]))
  #steals
  arr.append(float(split[24]))
  #blocks
  arr.append(float(split[25]))
  #fgp
  #arr.append(float(split[12]))
  #ftp
  #arr.append(float(split[19]))
  #turnovers
  arr.append(float(split[26]))
  #pfs
  arr.append(float(split[27]))
  #fgm
  arr.append(float(split[10]))
  #fga
  arr.append(float(split[11]))
  #ftm
  arr.append(float(split[17]))
  #fta
  arr.append(float(split[18]))
  #3pm
  arr.append(float(split[13]))
  #3pa
  arr.append(float(split[14]))
  arrs.append(deepcopy(arr))
  arr = []
  names.append(split[1][:len(split[1])-1] + '-' + split[3])
features = array(arrs) #used to be named features
whitened = whiten(features)
cores,_ = kmeans(whitened, 13, 50)
pGroups = []

for i in range(len(whitened)):
  player = whitened[i]
  minVal = float('inf')
  minGroup = 0
  for j in range(len(cores)):
    overall = 0.0
    for k in range(len(whitened[i])):
      overall += (whitened[i][k] - cores[j][k])*(whitened[i][k] - cores[j][k])
    v = math.sqrt(overall)
    if minVal > v:
      minVal = v
      minGroup = j+1
  print names[i] + ' ' + str(minGroup)
print cores
for d in range(len(cores[0])):
  print ''
  print ''
  print stats[d]
  mP = 0.0
  for ars in cores:
    if ars[d] > mP:
      mP = ars[d]
  poi = []
  for ars in cores:
    poi.append(int((ars[d]/mP)*100))
  for m in range(100):
    if m in poi:
      print(str(poi.index(m)+1)),
    else:
      print(" "),
