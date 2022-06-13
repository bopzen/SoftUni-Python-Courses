upper_limit_num1 = int(input())
upper_limit_num2 = int(input())
upper_limit_num3 = int(input())
if upper_limit_num2 > 7:
    upper_limit_num2 = 7
is_prime = True
for num1 in range(1, upper_limit_num1+1):
    if num1 % 2 == 0:
        for num2 in range(2, upper_limit_num2+1):
            is_prime = True
            for p in range(2,num2):
                if num2 % p == 0:
                    is_prime = False
                    break
            if is_prime:
                for num3 in range(1, upper_limit_num3+1):
                    if num3 % 2 == 0:
                        print(f"{num1} {num2} {num3}")