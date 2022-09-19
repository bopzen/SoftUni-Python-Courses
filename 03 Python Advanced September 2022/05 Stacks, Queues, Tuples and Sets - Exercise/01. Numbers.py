sequence1 = set(map(int, input().split()))
sequence2 = set(map(int, input().split()))
lines = int(input())
for _ in range(lines):
    command = input().split()
    action = command.pop(0)
    seq_number = command.pop(0)
    if action == 'Add':
        if seq_number == 'First':
            for number in command:
                sequence1.add(int(number))
        elif seq_number == 'Second':
            for number in command:
                sequence2.add(int(number))
    elif action == 'Remove':
        if seq_number == 'First':
            for number in command:
                if int(number) in sequence1:
                    sequence1.remove(int(number))
        elif seq_number == 'Second':
            for number in command:
                if int(number) in sequence2:
                    sequence2.remove(int(number))
    elif action == 'Check' and seq_number == 'Subset':
        if sequence1 < sequence2 or sequence2 < sequence1:
            print('True')
        else:
            print('False')
print(', '.join([str(x) for x in sorted(sequence1)]))
print(', '.join([str(x) for x in sorted(sequence2)]))