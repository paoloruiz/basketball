from scipy import stats
from PredictionStats import PredictionStats

outfile = open('output/formulae.txt', 'w')
for statToPredict in PredictionStats.statsToPredictLoop.value:
  for statToUse in PredictionStats.statsToLoop.value:
    x = []
    y = []
    dataFile = open(statToPredict + '/' + statToUse + 'Data.txt', 'r')
    for line in dataFile:
      data = line.split(' ')
      x.append(float(data[0]))
      y.append(float(data[1]))
    dataFile.close()

    slope, intercept, r_value, p_value, stderr = stats.linregress(x, y)
    print 'Predicting ' + statToPredict + ' by ' + statToUse
    print 'slope: ' + str(slope)
    print 'intercept: ' + str(intercept)
    print 'r_val: ' + str(r_value)
    print 'p_value: ' + str(p_value)
    outfile.write(str(slope) + ' ' + str(intercept) + ' ' + str(r_value * r_value) + '\n')
outfile.close()
