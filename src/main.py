import pandas as pd
import numpy as np
from utils.elo import updateRating

class Team():
    def __init__(self, currElo, peakElo, gamesPlayed):
        self.currElo = currElo
        self.peakElo = peakElo
        self.gamesPlayed = gamesPlayed
    
    def update(self, newElo):
        self.currElo = newElo
        self.peakElo = max(self.peakElo, newElo)
        self.gamesPlayed += 1

#todo
#read processed data
#store unique countries in dict with an initial rating
#go through each game
#   get home and away rating from ranklist
#   update rating in ranklist using data in row
df = pd.read_csv('data/processed/processed_results.csv')

unique_teams = np.unique(df[['home_team', 'away_team']])


def initRankList(teams, initialElo=1500):
    return {team: Team(initialElo, initialElo, 0) for team in teams}


def getElo(teams, team):
    return teams[team].currElo


def updateTable(teams, homeTeam, homeElo, awayTeam, awayElo):
    teams[homeTeam] = homeElo
    teams[awayTeam] = awayElo

    return teams


def eloEngine():
    teams = initRankList(unique_teams)
    home_elos = [] 
    away_elos = [] 

    for row in df.itertuples():

        homeElo = getElo(teams, row.home_team)
        awayElo = getElo(teams, row.away_team)
  
        homeRes = row.home_result
        awayRes = row.away_result
       
        newHomeElo, newAwayElo = updateRating(homeElo, homeRes, awayElo, awayRes)

        teams[row.home_team].update(newHomeElo)
        teams[row.away_team].update(newAwayElo)

        home_elos.append(newHomeElo)
        away_elos.append(newAwayElo)

    df['home_current_elo'] = home_elos
    df['away_current_elo'] = away_elos

    return teams


def main():
    data = eloEngine()
    output_df = pd.DataFrame.from_dict(data, orient='index', columns=['Current Elo'])
    output_df.reset_index(inplace=True)
    output_df.rename(columns={'index': 'Team'}, inplace=True)

    output_df.to_csv('src/outputs/CondensedData_df.csv', index=False)
    df.to_csv('src/outputs/EloOverTime_df.csv', index=False)

main()

















