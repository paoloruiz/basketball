f = open('preseason.txt', 'r')
g = open('parsedPreseason.txt', 'w')
for line in f:
  a = line.split('\t')
  b = a[0] + '\t' + a[1] + '\t' + a[3] + '\t' + a[3] + '\t' + a[2] + '\t' + a[4] + '\t' + a[4] + '\t' + a[5] + '\t' + a[6] + '\t' + a[7] + '\t' + a[8] + '\t' + a[9] + '\t' + a[10] + '\t' + a[11] + '\t' + a[11] + '\t' + a[11] + '\t' + a[11] + '\t' + a[12] + '\t' + a[13] + '\t' + a[14] + '\t' + a[17] + '\t' + a[18] + '\t' + a[19] + '\t' + a[20] + '\t' + a[21] + '\t' + a[22] + '\t' + a[15] + '\t' + a[16] + '\t' + a[23]
  g.write(b)
f.close()
g.close()
