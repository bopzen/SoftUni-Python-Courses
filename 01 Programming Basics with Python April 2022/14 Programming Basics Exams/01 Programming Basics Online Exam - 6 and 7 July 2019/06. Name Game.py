winner = ''
win_points = 0
while True:
    name = input()
    points = 0
    if name == 'Stop':
        break
    for i in name:
        num = int(input())
        if chr(num) == i:
            points += 10
        else:
            points += 2
    if points >= win_points:
        win_points = points
        winner = name
print(f"The winner is {winner} with {win_points} points!")

