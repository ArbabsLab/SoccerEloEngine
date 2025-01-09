import pandas as pd
import numpy as np
from main import eloEngine
# Mock data for testing purposes
mock_data = [
    {'home_team': 'Team A', 'away_team': 'Team B', 'home_result': 1, 'away_result': 0},  # Team A wins
    {'home_team': 'Team C', 'away_team': 'Team D', 'home_result': 0, 'away_result': 1},  # Team D wins
    {'home_team': 'Team A', 'away_team': 'Team C', 'home_result': 1, 'away_result': 0},  # Team A wins
    {'home_team': 'Team B', 'away_team': 'Team D', 'home_result': 0, 'away_result': 1},  # Team D wins
    {'home_team': 'Team A', 'away_team': 'Team D', 'home_result': 1, 'away_result': 1},  # Draw
]


df = pd.DataFrame(mock_data)

unique_teams = np.unique(df[['home_team', 'away_team']])

def runTests():
    print("Running Elo Engine Test...\n")
    teams_final_ratings = eloEngine()
    print(teams_final_ratings)
    

runTests()
