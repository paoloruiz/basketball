import math
from numpy import array
from scipy.cluster.vq import kmeans, whiten
from copy import deepcopy
f = open('2013perGameStats.txt', 'r')
arrs = []
arr = []
names = []
for line in f:
  split = line.split('\t')
  #pofloats
  arr.append(float(split[28][:len(split[28])-1]))
  #rebounds
  arr.append(float(split[22]))
  #assists
  arr.append(float(split[23]))
  #steals
  arr.append(float(split[24]))
  #blocks
  arr.append(float(split[25]))
  #fgp
  arr.append(float(split[12]))
  #ftp
  arr.append(float(split[19]))
  #turnovers
  arr.append(float(split[26]))
  arrs.append(deepcopy(arr))
  arr = []
  names.append(split[1])
features = array(arrs)
whitened = whiten(features)
cores,_ = kmeans(whitened, 14)
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
