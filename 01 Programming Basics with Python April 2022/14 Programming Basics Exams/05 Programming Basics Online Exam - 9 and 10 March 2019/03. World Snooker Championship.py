stage = input()
tickets_class = input()
tickets_count = int(input())
picture = input()

if stage == 'Quarter final':
    if tickets_class == 'Standard':
        ticket_price = 55.5
    elif tickets_class == 'Premium':
        ticket_price = 105.2
    elif tickets_class == 'VIP':
        ticket_price = 118.9
elif stage == 'Semi final':
    if tickets_class == 'Standard':
        ticket_price = 75.88
    elif tickets_class == 'Premium':
        ticket_price = 125.22
    elif tickets_class == 'VIP':
        ticket_price = 300.4
elif stage == 'Final':
    if tickets_class == 'Standard':
        ticket_price = 110.1
    elif tickets_class == 'Premium':
        ticket_price = 160.66
    elif tickets_class == 'VIP':
        ticket_price = 400
total_price = ticket_price * tickets_count
if picture == 'Y':
    if total_price >4000:
        total_price -=total_price * 0.25
    elif total_price >2500:
        total_price -=total_price * 0.1
        total_price += tickets_count * 40
    else:
        total_price += tickets_count * 40
elif picture == 'N':
    if total_price >4000:
        total_price -=total_price * 0.25
    elif total_price >2500:
        total_price -=total_price * 0.1
print(f'{total_price:.2f}')

    
