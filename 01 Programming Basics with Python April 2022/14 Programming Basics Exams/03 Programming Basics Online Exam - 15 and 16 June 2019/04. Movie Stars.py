budget = float(input())

while True:
    name = input()
    if name == 'ACTION':
        break
    if len(name) > 15:
        salary = budget * 0.2
    else:
        salary = float(input())
    budget -= salary
    if budget <0:
        print(f"We need {abs(budget):.2f} leva for our actors.")
        break
if name == 'ACTION':
    print(f"We are left with {budget:.2f} leva.")
