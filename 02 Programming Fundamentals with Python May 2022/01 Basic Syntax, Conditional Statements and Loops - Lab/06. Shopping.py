budget = int(input())

while True:
    price = input()
    if price == 'End':
        break
    price = int(price)
    if price > budget:
        print("You went in overdraft!")
        break
    budget -= price
if price == 'End' and budget>=0:
    print("You bought everything needed.")