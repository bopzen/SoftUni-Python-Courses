from modules.fibonacci import *

sequence = []
while True:
    command = input()
    if command == 'Stop':
        break
    command_args = command.split()
    if command_args[0] == 'Create':
        number = int(command_args[-1])
        sequence = create_fibonacci_sequence(number)
    else:
        number = int(command_args[-1])
        locate_num(sequence, number)
