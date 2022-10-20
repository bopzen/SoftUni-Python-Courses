days = int(input())
total_amount = 0
day_wins = 0
for d in range(days):
    count_wins = 0
    count_losses = 0
    day_amount = 0
    while True:
        sport = input()
        if sport == 'Finish':
            break
        result = input()
        if result == 'win':
            count_wins += 1
            day_amount += 20
        elif result == 'lose':
            count_losses += 1
    if count_wins > count_losses:
        day_wins += 1
        day_amount += day_amount * 0.1
    total_amount += day_amount

if day_wins > days - day_wins:
    total_amount += total_amount * 0.2
    print(f"You won the tournament! Total raised money: {total_amount:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_amount:.2f}")
