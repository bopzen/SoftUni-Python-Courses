fuel = input()
liters = float(input())
club_card = input()
if fuel == 'Gas':
    if liters >25:
        if club_card == 'Yes':
            total = liters*0.93
            total-=liters*0.08
            total-=total*0.1
        else:
            total = liters * 0.93
            total -= total * 0.1
    elif liters >=20:
        if club_card == 'Yes':
            total = liters*0.93
            total-=liters*0.08
            total-=total*0.08
        else:
            total = liters * 0.93
            total -= total * 0.08
    else:
        if club_card == 'Yes':
            total = liters*0.93
            total-=liters*0.08
        else:
            total = liters * 0.93
elif fuel == 'Gasoline':
    if liters >25:
        if club_card == 'Yes':
            total = liters*2.22
            total-=liters*0.18
            total-=total*0.1
        else:
            total = liters * 2.22
            total -= total * 0.1
    elif liters >=20:
        if club_card == 'Yes':
            total = liters*2.22
            total-=liters*0.18
            total-=total*0.08
        else:
            total = liters * 2.22
            total -= total * 0.08
    else:
        if club_card == 'Yes':
            total = liters*2.22
            total-=liters*0.18
        else:
            total = liters * 2.22
elif fuel == 'Diesel':
    if liters >25:
        if club_card == 'Yes':
            total = liters*2.33
            total-=liters*0.12
            total-=total*0.1
        else:
            total = liters * 2.33
            total -= total * 0.1
    elif liters >=20:
        if club_card == 'Yes':
            total = liters*2.33
            total-=liters*0.12
            total-=total*0.08
        else:
            total = liters * 2.33
            total -= total * 0.08
    else:
        if club_card == 'Yes':
            total = liters*2.33
            total-=liters*0.12
        else:
            total = liters * 2.33
print(f'{total:.2f} lv.')