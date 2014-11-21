import math
import operator
f = open('NbaOutcomes.txt', 'r')
teamRanks = dict()
teamLosses = dict()
teamWins = dict()
for line in f:
  fs = line.split('\t')
  away = fs[2]
  home = fs[3].replace('@ ', '')
  if away not in teamRanks:
    teamRanks[away] = 1.0/30
  if home not in teamRanks:
    teamRanks[home] = 1.0/30
  diff = int(fs[4].split(' : ')[0]) - int(fs[4].split(' : ')[1])
  if diff > 0:
    if away not in teamWins:
      teamWins[away] = [(home, diff)]
    else:
      wins = teamWins[away]
      wins.append((home, diff))
      teamWins[away] = wins
    if home not in teamLosses:
      teamLosses[home] = [(away, diff)]
    else:
      losses = teamLosses[home]
      losses.append((away, diff))
      teamLosses[home] = losses
  else:
    if home not in teamWins:
      teamWins[home] = [(away, abs(diff))]
    else:
      wins = teamWins[home]
      wins.append((away, abs(diff)))
      teamWins[home] = wins
    if away not in teamLosses:
      teamLosses[away] = [(home, abs(diff))]
    else:
      losses = teamLosses[away]
      losses.append((home, abs(diff)))
      teamLosses[away] = losses
teams = teamRanks.keys()
max_iterations = 500
damping = 0.85
min_delta = 0.0000001


closeGameMax = 5
midGameMax = 11
#switch to not using powers, and instead considering 1-4 point wins worth a certain amount, 5-10 worth a certain amount of the whole and so on

#Not penalizing enough for losses
for i in range(max_iterations):
  diff = 0
  for node in teams:
    rank = 0.005
    defeatedTeams = []
    if node in teamWins:
      defeatedTeams = teamWins[node]
    for defeated in defeatedTeams:
      lossScore = 0.0
      #
      scoreUnit = 2.0
      if defeated[1] <= closeGameMax:
        scoreUnit = 1.0
      elif defeated[1] <= midGameMax:
        scoreUnit = 1.5
      #
      tLosses = []
      if defeated[0] in teamLosses:
        tLosses = teamLosses[defeated[0]]
      for loss in tLosses:
        #lossScore += math.sqrt(loss[1])
        if defeated[1] <= closeGameMax:
          lossScore += 1.0
        elif defeated[1] <= midGameMax:
          lossScore += 1.5
        else:
          lossScore += 2.0
        #
      #rank += damping * teamRanks[defeated[0]] * math.sqrt(defeated[1]) / lossScore
      rank += damping * teamRanks[defeated[0]] * scoreUnit / lossScore
    diff += abs(teamRanks[node] - rank)
    teamRanks[node] = rank
  if diff < min_delta:
    break
sortedRanks = sorted(teamRanks.items(), key=operator.itemgetter(1))
print sortedRanks
#for team in sortedRanks:
#  print team[0]
#  print team[1]*7500
