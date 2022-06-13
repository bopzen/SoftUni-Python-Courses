junior_riders = int(input())
senior_riders = int(input())
track_type = input()
entry_fee = 0
total_riders = junior_riders + senior_riders
if track_type == 'trail':
    entry_fee = junior_riders * 5.5 + senior_riders * 7
elif track_type == 'cross-country':
    entry_fee = junior_riders * 8 + senior_riders * 9.5
    if total_riders >=50:
        entry_fee -= entry_fee * 0.25
elif track_type == 'downhill':
    entry_fee = junior_riders * 12.25 + senior_riders * 13.75
elif track_type == 'road':
    entry_fee = junior_riders * 20 + senior_riders * 21.5
entry_fee-=entry_fee*0.05
print(f'{entry_fee:.2f}')