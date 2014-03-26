import os
import sys
import shutil
f = open(str(sys.argv[1]) + 'lineups.txt', 'r')
g = open(str(sys.argv[1]) + 'parsedlineups.txt', 'w')
for line in f:
  m = line.split('\t')
  n = m[0].split(' - ')
  n[4] = n[4][:len(n[4])-6]
  o = ''
  for p in n:
    q = p.split(',')
    o += q[1] + ' ' + q[0] + ','
  o = o[:len(o)-1]
  g.write(o + '\t' + m[22])
f.close()
g.close()
