
print("Handball Tournament")
print()

# Win = 50 points
# Tie = 10 points
# Loss = 0 points

team_1 = ("A", 5, 1)
team_2 = ("B", 3, 1)
team_3 = ("C", 2, 1)
team_4 = ("D", 8, 1)

teams = [team_1, team_2, team_3, team_4]

for team in teams:
    name, win, tie = team

    print(f"TEAM NAME: {name}")

    total_pts = win * 50 + tie * 10

    if total_pts <= 150:
        print("Rank 4")
    elif total_pts <= 200:
        print("Rank 3")
    elif total_pts <= 300:
        print("Rank 2")
    else:
        print("Rank 1")

    print("Total points:", total_pts)
