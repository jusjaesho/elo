import math
import csv

games = []

with open('nfl_games_2019.csv') as csvfile:
	games_list = csv.reader(csvfile)
	for row in games_list:
		games.append(row)

teams = {}

def match(winner, loser):

	# constants
	k = 34
	
	# If either of the teams do not exist, add them to the dictionary with the default rating of 1500
	if winner not in teams:
		teams[winner] = 1500

	if loser not in teams:
		teams[loser] = 1500

	# Get each team's win probability
	winner_prob = 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (teams[winner] - teams[loser]) / 400))
	loser_prob = 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (teams[loser] - teams[winner]) / 400))

	# Assign new ratings
	teams[winner] = teams[winner] + k * (1 - winner_prob)
	teams[loser] = teams[loser] + k * (0 - loser_prob)

for game in games:
	match(game[0], game[1])

for key, value in teams.items():
	teams[key] = round(value)

# Sort teams from highest rank to smallest
final_rankings = sorted(teams.items(), key=lambda x: x[1], reverse=True)

# print teams by line to the console
# for team in final_rankings:
# 	print(team[0], round(team[1]))

with open('elo_results.csv','w') as result_file:
    wr = csv.writer(result_file)
    wr.writerows(final_rankings)





