import math
count_tournament = int(input())
starting_points = int(input())
wins = 0
points = starting_points
for i in range(count_tournament):
    stage = input()
    if stage == 'W':
        points +=2000
        wins +=1
    elif stage == 'F':
        points +=1200
    elif stage == 'SF':
        points +=720
average_points = math.floor((points - starting_points)/ count_tournament)
win_perc = wins / count_tournament * 100
print(f"Final points: {points}")
print(f"Average points: {average_points}")
print(f"{win_perc:.2f}%")