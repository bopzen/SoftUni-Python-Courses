lines = int(input())
list_command = []
for i in range(lines):
    command = input()
    list_command.append(command)
balanced = 0
for element in list_command:
    if element == '(':
        balanced += 1
        if balanced > 1:
            break
    elif element == ')':
        balanced -= 1
if balanced == 0:
    print('BALANCED')
else:
    print('UNBALANCED')