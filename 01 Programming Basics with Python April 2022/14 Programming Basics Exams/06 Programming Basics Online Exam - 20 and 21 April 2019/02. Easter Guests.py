import math
count_guests = int(input())
budget = int(input())
kozunak = math.ceil(count_guests / 3)
eggs = count_guests * 2
total_cost = kozunak * 4 + eggs * 0.45
if budget >= total_cost:
    money_left = budget - total_cost
    print(f"Lyubo bought {kozunak} Easter bread and {eggs} eggs.")
    print(f'He has {money_left:.2f} lv. left.')
else:
    money_needed = total_cost - budget
    print("Lyubo doesn't have enough money.")
    print(f'He needs {money_needed:.2f} lv. more.')