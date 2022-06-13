amount_needed = int(input())
funds_gathered = 0
counter = 1
counter_cc = 0
counter_cash = 0
amount_cc = 0
amount_cash = 0
while funds_gathered < amount_needed:
    purchase = input()
    if purchase == 'End':
        print("Failed to collect required money for charity.")
        break

    purchase = int(purchase)
    if counter % 2 ==0:
        if purchase >= 10:
            print('Product sold!')
            counter_cc +=1
            amount_cc += purchase
            funds_gathered += purchase
        else:
            print('Error in transaction!')
    else:
        if purchase <=100:
            print('Product sold!')
            counter_cash += 1
            amount_cash += purchase
            funds_gathered += purchase
        else:
            print('Error in transaction!')
    counter += 1
if funds_gathered >= amount_needed:
    average_cc = amount_cc / counter_cc
    average_cash = amount_cash / counter_cash
    print(f'Average CS: {average_cash:.2f}')
    print(f'Average CC: {average_cc:.2f}')