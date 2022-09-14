stack = list(map(int, input().split()))
rack_capacity = int(input())
needed_racks = 1
sum_clothes = 0
while stack:
    sum_clothes += stack[-1]
    if sum_clothes < rack_capacity:
        stack.pop()
    elif sum_clothes == rack_capacity:
        stack.pop()
        if stack:
            needed_racks += 1
            sum_clothes = 0
    else:
        needed_racks += 1
        sum_clothes = 0

print(needed_racks)