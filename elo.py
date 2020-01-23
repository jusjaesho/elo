import math

games = [
	{"Jason DeLucia": "Trent Jenkins"},
	{"Gerard Gordeau": "Teila Tuli"},
	{"Kevin Rosier": "Zane Frazier"},
	{"Royce Gracie": "Art Jimmerson"},
	{"Ken Shamrock": "Patrick Smith"},
	{"Gerard Gordeau": "Kevin Rosier"},
	{"Royce Gracie": "Ken Shamrock"},
	{"Royce Gracie": "Gerard Gordeau"},
	{"Royce Gracie": "Minoki Ichihara"},
	{"Jason DeLucia": "Scott Baker"},
	{"Remco Pardoel": "Alberto Cerro Leon"},
	{"Orlando Wiet": "Robert Lucarelli"},
	{"Frank Hamaker": "Thaddeus Luster"},
	{"Johnny Rhodes": "David Levicki"},
	{"Patrick Smith": "Ray Wizard"},
	{"Scott Morris": "Sean Daugherty"},
	{"Royce Gracie": "Jason DeLucia"},
	{"Remco Pardoel": "Orlando Wiet"},
	{"Johnny Rhodes": "Fred Ettish"},
	{"Patrick Smith": "Scott Morris"},
	{"Royce Gracie": "Remco Pardoel"},
	{"Patrick Smith": "Johnny Rhodes"},
	{"Royce Gracie": "Patrick Smith"},
	{"Royce Gracie": "Kimo Leopoldo"},
	{"Harold Howard": "Roland Payne"},
	{"Ken Shamrock": "Christophe Leininger"},
	{"Keith Hackney": "Emmanuel Yarborough"},
	{"Ken Shamrock": "Felix Mitchell"},
	{"Steve Jennum": "Harold Howard"},
	{"Guy Mezger": "Jason Fairn"},
	{"Marcus Bossett": "Eldo Dias Xavier"},
	{"Joe Charles": "Kevin Rosier"},
	{"Dan Severn": "Anthony Macias"},
	{"Steve Jennum": "Melton Bowen"},
	{"Keith Hackney": "Joe Son"},
	{"Royce Gracie": "Ron van Clief"},
	{"Dan Severn": "Marcus Bossett"},
	{"Royce Gracie": "Keith Hackney"},
	{"Royce Gracie": "Dan Severn"},
	{"Guy Mezger": "John Dowdy"},
	{"Dave Beneteau": "Asbel Cancio"},
	{"Dan Severn": "Joe Charles"},
	{"Oleg Taktarov": "Ernie Verdicia"},
	{"Todd Medina": "Larry Cureton"},
	{"Jon Hess": "Andy Anderson"},
	{"Dan Severn": "Oleg Taktarov"},
	{"Dave Beneteau": "Todd Medina"},
	{"Dan Severn": "Dave Beneteau"},
	{"Ken Shamrock": "Royce Gracie"},
	{"Anthony Macias": "He-Man Ali Gipson"},
	{"Joel Sutton": "Jack McLaughlin"},
	{"Oleg Taktarov": "Dave Beneteau"},
	{"Patrick Smith": "Rudyard Moncayo"},
	{"Paul Varelans": "Cal Worsham"},
	{"Tank Abbott": "John Matua"},
	{"Oleg Taktarov": "Anthony Macias"},
	{"Tank Abbott": "Paul Varelans"},
	{"Oleg Taktarov": "Tank Abbott"},
	{"Ken Shamrock": "Dan Severn"},
	{"Scott Bessac": "David Hood"},
	{"Onassis Parungao": "Francesco Maturi"},
	{"Joel Sutton": "Geza Kalman"},
	{"Marco Ruas": "Larry Cureton"},
	{"Remco Pardoel": "Ryan Parker"},
	{"Mark Hall": "Harold Howard"},
	{"Paul Varelans": "Gerry Harris"},
	{"Marco Ruas": "Remco Pardoel"},
	{"Paul Varelans": "Mark Hall"},
	{"Marco Ruas": "Paul Varelans"},
	{"Ken Shamrock": "Oleg Taktarov"}
	]

people = {}

def match(winner, loser):

	# constants

	k = 24
	
	# If either of the players do not exist, add them to the dictionary with the default rating of 1500
	
	if winner not in people:
		people[winner] = 1500

	if loser not in people:
		people[loser] = 1500

	# Get each player's win probability

	winner_prob = 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (people[winner] - people[loser]) / 400))
	loser_prob = 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (people[loser] - people[winner]) / 400))

	# Assign new ratings

	people[winner] = people[winner] + k * (1 - winner_prob)
	people[loser] = people[loser] + k * (0 - loser_prob)

for game in games:
	for key, value in game.items():
		match(key, value)

final_rankings = sorted(people.items(), key=lambda x: x[1], reverse=True)

for person in final_rankings:
	print(person[0], round(person[1]))


