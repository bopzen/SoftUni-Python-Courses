def sum_numbers(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def add_and_subtract(number1, number2, number3):
    return subtract(sum_numbers(number1,number2), number3)


a = int(input())
b = int(input())
c = int(input())
print(add_and_subtract(a, b, c))
