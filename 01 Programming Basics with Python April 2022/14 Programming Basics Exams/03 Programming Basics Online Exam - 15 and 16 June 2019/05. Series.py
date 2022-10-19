budget = float(input())
count_series = int(input())
cost = 0
for i in range(count_series):
    name = input()
    price = float(input())
    if name == 'Thrones':
        price -= price * 0.5
    elif name == 'Lucifer':
        price -= price * 0.4
    elif name == 'Protector':
        price -= price * 0.3
    elif name == 'TotalDrama':
        price -= price * 0.2
    elif name == 'Area':
        price -= price * 0.1
    cost += price

diff = abs(budget - cost)
if cost > budget:
    print(f"You need {diff:.2f} lv. more to buy the series!")
else:
    print(f"You bought all the series and left with {diff:.2f} lv.")
