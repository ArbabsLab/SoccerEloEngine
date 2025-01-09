import math
import pandas as pd

#Todo for future
#adjust k based on how many goals were scored in game

def probability(rating1, rating2):
    p1 = (1.0/ (1.0 + pow(10, ((rating2 - rating1)/400))))
    p2 = (1.0/ (1.0 + pow(10, ((rating1 - rating2)/400))))

    return [p1, p2]


def updateRating(homeRating, homeResult, awayRating, awayResult, k=16):
    homeExpec, awayExpec = probability(homeRating, awayRating)

    newHomeRating = homeRating + k*(homeResult - homeExpec)
    newAwayRating = awayRating + k*(awayResult - awayExpec)
    return [math.ceil(newHomeRating), math.ceil(newAwayRating)]

