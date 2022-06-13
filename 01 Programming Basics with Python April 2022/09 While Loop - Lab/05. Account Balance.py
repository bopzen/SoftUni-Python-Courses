total = 0

while True:
    deposit = input()
    if deposit == 'NoMoreMoney':
        break
    else:
        deposit = float(deposit)
        if deposit < 0:
            print('Invalid operation!')
            break
        else:
            print(f'Increase: {deposit:.2f}')
            total += deposit
print(f"Total: {total:.2f}")