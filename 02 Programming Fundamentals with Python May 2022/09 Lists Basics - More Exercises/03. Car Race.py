list_numbers = input().split()
left_side = list_numbers[0:len(list_numbers)//2]
right_side = list_numbers[-1:len(list_numbers)//2:-1]
sum_left = 0
sum_right = 0

for element in left_side:
    if int(element) == 0:
        sum_left *= 0.8
    else:
        sum_left += int(element)
for element in right_side:
    if int(element) == 0:
        sum_right *= 0.8
    else:
        sum_right += int(element)
if sum_left > sum_right:
    winner = 'right'
else:
    winner = 'left'
print(f"The winner is {winner} with total time: {min(sum_left,sum_right):.1f}")