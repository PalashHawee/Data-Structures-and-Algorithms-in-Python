# Time O(n) and Space O(k) where n is the
#number of competitions and K is the number of teams 

HOME_TEAM_WON=1
def tournamentWinner(competitions, results):
    # Write your code here.
    currentBestTeam=""
	scores={currentBestTeam:0}
	for i, competition in enumerate(competitions):
		result=results[i]
		homeTeam, awayTeam=competition
		
		winningTeam=homeTeam if result==HOME_TEAM_WON else awayTeam
		
		updateScores(winningTeam, 3, scores)
		
		if scores[winningTeam] > scores[currentBestTeam]:
			currentBestTeam=winningTeam
	return currentBestTeam

def updateScores(team, points, scores):
	if team not in scores:
		scores[team]=0
		
	scores[team]+=points
