def create_fibonacci_sequence(number):
    if number == 0:
        fibonacci = []
    elif number == 1:
        fibonacci = [0]
    else:
        fibonacci = [0, 1]
        for _ in range(number-2):
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci


def locate_num(sequence, num):
    for index in range(len(sequence)):
        if sequence[index] == num:
            print(f"The number - {num} is at index {index}")
            break
    else:
        print(f"The number {num} is not in the sequence")
