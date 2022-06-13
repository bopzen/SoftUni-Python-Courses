start_number = int(input())
end_number = int(input())
magic_number = int(input())
counter = 0
flag = False
num1 = start_number
num2 = start_number
for num1 in range (start_number,end_number+1):
    for num2 in range (start_number,end_number+1):
        counter += 1
        if num1 + num2 == magic_number:
            flag = True
            break
    if flag:
        break
if flag:
    print(f"Combination N:{counter} ({num1} + {num2} = {magic_number})")
else:
    print(f"{counter} combinations - neither equals {magic_number}")