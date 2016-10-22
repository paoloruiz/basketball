from matplotlib import pyplot as plt
from scipy import stats

x = []
y = []
dataFile = open('minutes/minutesData.txt', 'r')
for line in dataFile:
  data = line.split(' ')
  x.append(float(data[0]))
  y.append(float(data[1]))
dataFile.close()

slope, intercept, r_value, p_value, stderr = stats.linregress(x, y)
print 'slope: ' + str(slope)
print 'intercept: ' + str(intercept)
print 'r_val: ' + str(r_value)
print 'p_value: ' + str(p_value)

plt.scatter(x, y)
plt.show()
