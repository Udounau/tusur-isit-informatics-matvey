def team_weights(weights):
    k = 0
    team1 = []
    team2 = []
    for i in weights:
        k+=1
        if k % 2 == 1:
            team1.append(i)
        else:
            team2.append(i)
    return (sum(team1), sum(team2))