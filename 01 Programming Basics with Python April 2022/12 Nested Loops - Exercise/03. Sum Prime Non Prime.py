sum_prime = 0
sum_non_prime = 0
is_non_prime = False
command = input()
while command != 'stop':
    num = int(command)
    if num < 0:
        print("Number is negative.")
        command = input()
        continue
    if num <=1:
        sum_non_prime += num
        command = input()
        continue

    for i in range(2, num):
        if num % i == 0:
            is_non_prime = True
            break
    if is_non_prime:
        sum_non_prime += num
    else:
        sum_prime += num

    is_non_prime = False
    command = input()

print(f"Sum of all prime numbers is: {sum_prime}")

print(f"Sum of all non prime numbers is: {sum_non_prime}")