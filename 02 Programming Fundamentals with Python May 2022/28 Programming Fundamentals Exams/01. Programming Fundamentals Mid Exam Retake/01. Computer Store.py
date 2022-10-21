total = 0
while True:
    command = input()
    if command == 'special' or command == 'regular':
        break
    price = float(command)
    if price < 0:
        print('Invalid price!')
        continue
    total += price
taxes = total * 0.2
total_with_taxes = total + taxes
if total == 0:
    print('Invalid order!')
else:
    if command == 'special':
        final_price = total_with_taxes - total_with_taxes * 0.1
    elif command == 'regular':
        final_price = total_with_taxes
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {final_price:.2f}$")