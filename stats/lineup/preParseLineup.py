import os
import sys
import shutil
f = open(str(sys.argv[1]) + 'lineups.txt', 'r')
g = open(str(sys.argv[1]) + 'copy.txt', 'w')
for line in f:
  m = line.split('\t')
  if 'Rk' in line or 'Poss' in line:
    continue
  g.write(line.replace('\t\t', '\t0.0\t'))
f.close()
g.close()
shutil.copyfile(str(sys.argv[1]) + 'copy.txt', str(sys.argv[1]) + 'lineups.txt')
os.remove(str(sys.argv[1]) + 'copy.txt')
