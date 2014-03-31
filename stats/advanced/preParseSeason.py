import os
import sys
import shutil
f = open(str(sys.argv[1]) + 'advanced.txt', 'r')
g = open(str(sys.argv[1]) + 'copy.txt', 'w')
pl = set()
for line in f:
  if "Player" in line:
    continue
  m = line.split('\t')
  if m[1] in pl:
    continue
  pl.add(m[1])
  g.write(line.replace('\t\t', '\t0.0\t').replace('*', ''))
f.close()
g.close()
shutil.copyfile(str(sys.argv[1]) + 'copy.txt', str(sys.argv[1]) + 'advanced.txt')
os.remove(str(sys.argv[1]) + 'copy.txt')
