from season import Season
from PredictionStats import PredictionStats

year_to_predict = 2017
min_mins_played = 10.0
min_games_played = 20

statsToPredict = PredictionStats.statsToPredictLoop.value
statsToUse = PredictionStats.statsToLoop.value

season_predict = Season()
players = season_predict.calcSeason('season/' + str(year_to_predict) + 'Stats.txt', year_to_predict, min_mins_played, min_games_played)

formulae = []
formulae_rvals = []
formulae_f = open('output/formulae.txt', 'r')
for statPredict in statsToPredict:
  formulae_overall = []
  formulae_rv = 0.0
  for statUse in statsToUse:
    slope, intercept, r_val = map(float, formulae_f.readline().split(' '))
    formulae_overall.append((slope, intercept, r_val))
    formulae_rv += r_val
  formulae.append(formulae_overall)
  formulae_rvals.append(formulae_rv)
formulae_f.close()

for player in players:
  predictionVal = player.name
  player_season = player.getSeason(year_to_predict)
  player_stat_pred = []
  for formulas in range(len(formulae)):
    stat = 0.0
    player_stat = player_season.getStatsByLoopVar( formulas )
    for formula in range(len(formulae[formulas])):
      slope, intercept, r_val = formulae[formulas][formula]
      stat += (float(slope) * float(player_stat) + float(intercept)) * float(r_val) / float(formulae_rvals[formulas])
    #player_stat_pred.append(stat / len(formulae[formulas]))
    player_stat_pred.append(stat)
  for i in range(0, 6):
    predictionVal += ' ' + str(player_stat_pred[i])
  predictionVal += ' ' + str(player_stat_pred[-1])
  print(predictionVal)
