from CodeWars.maximize_points.maximize_points import maximize_points

def test_team1_wins_every_game_sorted():
    assert maximize_points([2, 3, 4], [1, 2, 3]) == 3

def test_team1_wins_every_game_unsorted():
    assert maximize_points([3, 2, 4], [1, 2, 3]) == 3

def test_team1_loses_every_game_sorted():
    assert maximize_points([2, 3, 4], [4, 5, 6]) == 0

def test_team1_loses_every_game_unsorted():
    assert maximize_points([2, 4, 3], [4, 6, 6]) == 0

def test_duplicate_numbers():
    assert maximize_points([1, 2, 3, 3], [1, 1, 2, 5]) == 3