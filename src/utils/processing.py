import pandas as pd

#Todo:
#read csv
#get rid of columns that are not needed
#add goal difference column
#add winner/loser column

pre_processed_df = pd.read_csv('data/raw/results.csv', delimiter=',', header=0)

#only necessary columns
data = ['date','home_team','away_team','home_score','away_score']
processed_df = pre_processed_df[data]

#add goal difference col
processed_df['goal_difference'] = abs(processed_df['home_score'] - processed_df['away_score'])

#add home and away result
#win is 1, loss is 0, draw is 0.5
def getWinner(homeGoal, awayGoal):
    if homeGoal > awayGoal:
        return [1, 0]
    elif awayGoal > homeGoal:
        return [0, 1]
    else:
        return [0.5, 0.5]


processed_df[['home_result', 'away_result']] = processed_df.apply(
    lambda row: pd.Series(getWinner(row['home_score'], row['away_score'])), axis=1)

processed_df['home_current_elo'] = processed_df.apply(
    lambda row: 0, axis=1
)

processed_df['away_current_elo'] = processed_df.apply(
    lambda row: 0, axis=1
)

#store the processed data in the data folder
processed_df.to_csv('data/processed/processed_results.csv', index=False)


