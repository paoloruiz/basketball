import SeasonsIndex

players = SeasonsIndex.parseSeasons()
#Need to figure out a way to make this work with multiple different dimensions at once
minutesData = open('minutes/minutesData.txt', 'w')
for player in players:
  startYear = player.getFirstYear()
  nextYear = startYear + 1
  while player.hasSeason(nextYear):
    minutesData.write(str(player.getSeason(startYear).mp) + ' ' + str(player.getSeason(nextYear).mp) + '\n')
    startYear += 1
    nextYear += 1
minutesData.close()
