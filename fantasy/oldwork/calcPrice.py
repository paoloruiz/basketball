import os
import sys
price_pivot = 12.0
f = open(sys.argv[1] + '.txt', 'r')
for line in f:
  g = line.split('\t')
  name = g[0]
  score = float(g[1])
  init_price = (score/40.0)*100.0
  print name + '\t' + str(init_price + (init_price - price_pivot)*1.7)
