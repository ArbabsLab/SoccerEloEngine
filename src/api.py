from fastapi import FastAPI
import pandas as pd

app = FastAPI()

data = pd.read_csv("src/outputs/CondensedData_df.csv")
data_over_time = pd.read_csv("src/outputs/EloOverTime_df.csv")

@app.get("/")
def root():
    return {"Message": "Welcome to the Soccer Elo Engine API"}

@app.get("/teams")
def getRecords():
    return data.to_dict(orient="records")

@app.get("/team/{team_name}")
def getTeamInfo(team_name: str):
    teamData = data[data["Team"] == team_name]
    if teamData.empty:
        return {"Error": f"Team '{team_name}' not found"}
    return teamData.to_dict(orient="records")

@app.get("/TopTeams/")
def getTopTeams(count: int = 10):
    top_teams = data.nlargest(count, "Current_Elo")
    return top_teams.to_dict(orient="records")


def probability(rating1, rating2):
    p1 = (1.0/ (1.0 + pow(10, ((rating2 - rating1)/400))))
    p2 = (1.0/ (1.0 + pow(10, ((rating1 - rating2)/400))))

    return [p1, p2]

@app.get("/predict/{team_one}/{team_two}")
def predictMatch(team_one: str, team_two: str):
    team1_data = data[data["Team"] == team_one]
    team2_data = data[data["Team"] == team_two]

    if team1_data.empty or team2_data.empty:
        return {"Error": "One or both teams not found"}

    team1_elo = team1_data["Current_Elo"].values[0]
    team2_elo = team2_data["Current_Elo"].values[0]


    team1_prob = probability(team1_elo, team2_elo)[0]
    team2_prob = 1 - team1_prob

    return {
        f"{team_one} Win Probability": team1_prob,
        f"{team_two} Win Probability": team2_prob
    }
