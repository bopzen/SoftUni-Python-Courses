def calculate_expression(expression):
    a, op, b = expression.split()
    try:
        a = float(a)
        b = float(b)
        result = 0

        if op == '+':
            result = a + b
        elif op == '-':
            result = a- b
        elif op == '*':
            result = a * b
        elif op == '/':
            result = a / b
        elif op == '^':
            result = a ** b
        print(f"{result:.2f}")
    except ZeroDivisionError:
        print('Cannot divide by 0')
    except ValueError:
        print('Invalid input')

