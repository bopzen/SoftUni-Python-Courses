voucher = int(input())
tickets_count = 0
others_counts = 0
while True:
    purchase = input()
    if purchase == 'End':
        break
    if len(purchase) > 8:
        price = ord(purchase[0]) + ord(purchase[1])
        if price > voucher:
            break
        else:
            voucher -= price
            tickets_count +=1
    else:
        price = ord(purchase[0])
        if price > voucher:
            break
        else:
            voucher -= price
            others_counts +=1
print(tickets_count)
print(others_counts)