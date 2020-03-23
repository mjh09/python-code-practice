def alternatingSums(a):
    switch = True
    team_1 = []
    team_2 = []
    for weight in a:
        if switch:
            team_1.append(weight)
            switch = False
        else:
            team_2.append(weight)
            switch = True
    return [sum(team_1), sum(team_2)]
