num_bottles = int(input())
total_ml = num_bottles * 750
left_ml = total_ml
counter = 1
counter_dishes = 0
counter_pots = 0
is_enough = False
while left_ml >=0:
    loaded = input()
    if loaded == 'End':
        is_enough = True
        break
    loaded = int(loaded)
    if counter % 3 == 0:
        left_ml -= loaded * 15
        counter_pots += loaded
    else:
        left_ml -= loaded * 5
        counter_dishes += loaded
    counter +=1
if is_enough or left_ml == 0:
    print(f"Detergent was enough!")
    print(f"{counter_dishes} dishes and {counter_pots} pots were washed.")
    print(f"Leftover detergent {left_ml} ml.")
else:
    print(f"Not enough detergent, {abs(left_ml)} ml. more necessary!")