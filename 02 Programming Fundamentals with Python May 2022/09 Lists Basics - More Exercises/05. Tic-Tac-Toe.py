first_line = input().split()
second_line = input().split()
third_line = input().split()
winner = ''
for x in range(3):
    if first_line[x] == second_line [x] == third_line[x]:
        winner = first_line[x]
if first_line[0] == first_line[1] == first_line[2]:
    winner = first_line[0]
elif second_line[0] == second_line[1] == second_line[2]:
    winner = second_line[0]
elif third_line[0] == third_line[1] == third_line[2]:
    winner = third_line[0]
elif first_line[0] == second_line[1] == third_line[2] or first_line[2] == second_line[1] == third_line[0]:
    winner = second_line[1]

if winner == '1':
    print("First player won")
elif winner == '2':
    print("Second player won")
else:
    print("Draw!")