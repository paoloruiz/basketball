#we'll use statlines to generate our names.

#intake the start year and end year to gather upon
import sys

names = set()
for year in range(int(sys.argv[1]), int(sys.argv[2])):
  f = open('../statline/' + str(year) + 'perGameStats.txt', 'r')
  for line in f:
    stats = line.split('\t')
    # we don't want the extra space at the end
    names.add(stats[1][:len(stats[1])-1])
  f.close()
f = open('names.txt', 'w')
for name in names:
  f.write(name + '\n')
f.close()
