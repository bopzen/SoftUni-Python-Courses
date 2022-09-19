from collections import deque

expression = input().split()
calculation = deque()
for element in expression:
    if element == '+':
        current_result = int(calculation.popleft())
        while calculation:
            current_result += int(calculation.popleft())
        calculation.append(current_result)
    elif element == '-':
        current_result = int(calculation.popleft())
        while calculation:
            current_result -= int(calculation.popleft())
        calculation.append(current_result)
    elif element == '*':
        current_result = int(calculation.popleft())
        while calculation:
            current_result *= int(calculation.popleft())
        calculation.append(current_result)
    elif element == '/':
        current_result = int(calculation.popleft())
        while calculation:
            current_result //= int(calculation.popleft())
        calculation.append(current_result)
    else:
        calculation.append(int(element))
print(*calculation)