clients = int(input())
total_bill = 0
for i in range(clients):
    bill = 0
    count_products = 0
    while True:
        command = input()
        if command == 'Finish':
            break
        if command == 'basket':
            bill += 1.5
            count_products += 1
        elif command == 'wreath':
            bill += 3.8
            count_products += 1
        elif command == 'chocolate bunny':
            bill += 7
            count_products += 1
    if count_products % 2 == 0:
        bill -= bill * 0.2
    print(f"You purchased {count_products} items for {bill:.2f} leva.")
    total_bill += bill
print(f"Average bill per client is: {total_bill/clients:.2f} leva.")
