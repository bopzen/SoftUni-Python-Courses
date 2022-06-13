starting_number = int(input())
ending_number = int(input())
magic_number = int(input())
counter = 0
is_found = False
for i in range(starting_number,ending_number+1):
    for j in range(starting_number,ending_number+1):
        counter +=1
        if i + j == magic_number:
            is_found = True
            break
    if is_found:
        break
if is_found:
    print(f"Combination N:{counter} ({i} + {j} = {magic_number})")
else:
    print(f"{counter} combinations - neither equals {magic_number}")