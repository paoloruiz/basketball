#we'll use statlines to generate our names.

#intake the start year and end year to gather upon
import sys

names = set()
year = str(sys.argv[1])
f = open('../statline/' + str(year) + 'perGameStats.txt', 'r')
for line in f:
  stats = line.split('\t')
  names.add(stats[1][:len(stats[1])-1].replace('*', '') + '\t' + stats[4])
f.close()
f = open('names.txt', 'w')
for name in names:
  f.write(name + '\n')
f.close()
