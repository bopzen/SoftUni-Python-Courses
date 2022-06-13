def factorial(number1, number2):
    factorial1 = 1
    factorial2 = 1
    for i in range(1, number1+1):
        factorial1 *= i
    for i in range(1, number2+1):
        factorial2 *= i
    division = factorial1 / factorial2
    print(f"{division:.2f}")


factorial(int(input()), int(input()))