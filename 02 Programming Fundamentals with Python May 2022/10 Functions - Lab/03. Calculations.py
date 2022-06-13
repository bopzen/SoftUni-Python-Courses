def operator_func(operator, number1, number2):
    result = None
    if operator == 'multiply':
        result = number1 * number2
    elif operator == 'divide':
        result = int(number1 / number2)
    elif operator == 'add':
        result = number1 + number2
    elif operator == 'subtract':
        result = number1 - number2
    return result


input_operator = input()
first_num = int(input())
secont_num = int(input())

print(operator_func(input_operator, first_num, secont_num))