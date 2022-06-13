command = input()
while command != 'End':
    if command == 'SoftUni':
        command = input()
        continue
    for c in command:
        print(c*2, end='')
    print()
    command = input()