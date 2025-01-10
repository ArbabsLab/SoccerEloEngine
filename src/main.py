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
    return teams.get(team, 1500)
    """
    for teamName, elo in teams.items():
        if teamName == team:
            return elo
    """
   
def updateTable(teams, homeTeam, homeElo, awayTeam, awayElo):
    teams[homeTeam] = homeElo
    teams[awayTeam] = awayElo

    return teams
    

def eloEngine():
    teams = initRankList(unique_teams)
    home_elos = []  # List to hold updated home Elo values
    away_elos = []  # List to hold updated away Elo values
    
    # Iterate through the dataframe, calculating new Elo scores
    for row in df.itertuples():
        homeElo = getElo(teams, row.home_team)
        awayElo = getElo(teams, row.away_team)
        homeRes = row.home_result
        awayRes = row.away_result
        newHomeElo, newAwayElo = updateRating(homeElo, homeRes, awayElo, awayRes)
        
        # Append the new Elo values for later assignment
        home_elos.append(newHomeElo)
        away_elos.append(newAwayElo)
        
        # Update the teams dictionary in memory
        teams[row.home_team] = newHomeElo
        teams[row.away_team] = newAwayElo

    # Assign the new Elo values to the DataFrame at once
    df['home_current_elo'] = home_elos
    df['away_current_elo'] = away_elos

    print(df.head(5))
    return teams


def main():
    data = eloEngine()
    output_df = pd.DataFrame.from_dict(data, orient='index', columns=['Current Elo'])
    output_df.reset_index(inplace=True)
    output_df.rename(columns={'index': 'Team'}, inplace=True)

    output_df.to_csv('src/outputs/output_df.csv', index=False)

main()


















