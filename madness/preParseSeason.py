import os
import sys
import shutil
f = open(str(sys.argv[1]) + 'se.txt', 'r')
g = open(str(sys.argv[1]) + 'copy.txt', 'w')
pl = set()
q = open('teamname.txt', 'r')
names = dict()
for line in q:
  p = line.split('\t')
  pLen = len(p[1])-1
  names[p[1][:pLen]] = p[0]
for line in f:
  if "Overall" in line or "3PA" in line:
    continue
  k = line.replace('\t\t', '\t0.0\t')
  ki = k.split('\t')
  kLen = len(ki[1])-1
  g.write(k.replace(ki[1], names[ki[1][:kLen]]))
f.close()
g.close()
shutil.copyfile(str(sys.argv[1]) + 'copy.txt', str(sys.argv[1]) + 'se.txt')
os.remove(str(sys.argv[1]) + 'copy.txt')
