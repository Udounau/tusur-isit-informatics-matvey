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
team_weights([13, 27, 49])       # (62, 27)    13 + 49 и 27
team_weights([50, 60, 70, 80])   # (120, 140)
team_weights([])                 # (0, 0)