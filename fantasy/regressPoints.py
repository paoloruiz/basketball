import matplotlib.pyplot as plt
from scipy import stats

plot_file = open('bpm.txt', 'r')
pairs = []
for line in plot_file:
  pair = line.split(',')
  pairs.append((float(pair[0].replace('(', '').strip()), float(pair[1].replace(')', '').strip())))
plot_file.close()

x, y = zip(*pairs)
slope, intercept, r_value, p_value, stderr = stats.linregress(x, y)

print 'slope: ' + str(slope)
print 'intercept: ' + str(intercept)
print 'r_value: ' + str(r_value)
print 'r_squared: ' + str(r_value**2)
print 'p_value: ' + str(p_value)
print 'stderr: ' + str(stderr)

plt.scatter(x, y)
plt.show()
