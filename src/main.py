import pandas as pd
import numpy as np
from utils.elo import updateRating

#todo
#read processed data
#store unique countries in dict with an initial rating
#go through each game
#   get home and away rating from ranklist
#   update rating in ranklist using data in row
df = pd.read_csv('data/processed/processed_results.csv')

unique_teams = np.unique(df[['home_team', 'away_team']])

def initRankList(teams, initialElo=1500):
    res = {}
    for team in teams:
        res[team] = initialElo
    return res

def getElo(teams, team):
    for teamName, elo in teams.items():
        if teamName == team:
            return elo

def updateTable(teams, homeTeam, homeElo, awayTeam, awayElo):
    for teamName in teams.keys():
        if teamName == homeTeam:
            teams[homeTeam] = homeElo
        elif teamName == awayTeam:
            teams[awayTeam] = awayElo
    return teams

def eloEngine():
    teams = initRankList(unique_teams)
    for row in df.itertuples():
        homeElo = getElo(teams, row.home_team)
        awayElo = getElo(teams, row.away_team)
        homeRes = row.home_result
        awayRes = row.away_result
        newHomeElo, newAwayElo = updateRating(homeElo, homeRes, awayElo, awayRes)
        teams = updateTable(teams, row.home_team, newHomeElo, row.away_team, newAwayElo)
    print(teams)
 
eloEngine()
















