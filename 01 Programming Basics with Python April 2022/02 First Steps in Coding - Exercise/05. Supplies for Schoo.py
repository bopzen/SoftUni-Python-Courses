pens = 5.8
markers = 7.2
cleaner = 1.2

amount_pens = int(input('amount_pens: '))
amount_markers = int(input('amount_markers: '))
amount_cleaner = int(input('amount_cleaner" '))
discount = int(input('discount: '))/100

total = amount_pens * pens + amount_markers * markers + amount_cleaner * cleaner
discount_amount = total * discount
total_with_discount = total - discount_amount
print(total_with_discount)