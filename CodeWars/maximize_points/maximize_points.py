def maximize_points(team1, team2):
    team1_sorted = sorted(team1)
    team2_sorted = sorted(team2)
    i = 0
    j = 0
    wins = 0
    while j < len(team2) and i < len(team1):
        if team1_sorted[i] > team2_sorted[j]:
            i += 1
            j += 1
            wins += 1
        else:
            i += 1
    return wins