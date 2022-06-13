available_1lev = int(input())
available_2leva = int(input())
available_5leva = int(input())
amount = int(input())

for c1 in range(available_1lev+1):
    for c2 in range(available_2leva+1):
        for c5 in range(available_5leva+1):
            if c1 * 1 + c2 * 2 + c5 * 5 == amount:
                print(f"{c1} * 1 lv. + {c2} * 2 lv. + {c5} * 5 lv. = {amount} lv.")