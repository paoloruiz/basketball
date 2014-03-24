import os
import sys
import shutil
f = open(str(sys.argv[1]) + 'se.txt', 'r')
g = open('teamname.txt', 'r')
names = dict()
for line in g:
  m = line.split('\t')
  lenM = len(m[1])-1
  names[m[1][:lenM]] = m[0]
for line in f:
  n = line.split('\t')
  stringLen = len(n[1])-1
  if n[1][:stringLen] not in names:
    print n[1][:stringLen] + ' is not found'
