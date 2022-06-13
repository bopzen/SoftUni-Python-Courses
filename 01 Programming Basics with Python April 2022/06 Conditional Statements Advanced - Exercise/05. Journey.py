budget = float(input())
season = input().lower()
destination =''
place = ''
cost = 0
if budget >1000:
    destination = 'Europe'
    place = 'Hotel'
    cost = budget * 0.9
elif budget >100:
    destination = 'Balkans'
    if season == 'summer':
        place = 'Camp'
        cost = budget * 0.4
    elif season == 'winter':
        place = 'Hotel'
        cost = budget * 0.8
elif budget <=100:
    destination = 'Bulgaria'
    if season == 'summer':
        place = 'Camp'
        cost = budget * 0.3
    elif season == 'winter':
        place = 'Hotel'
        cost = budget * 0.7
print(f'Somewhere in {destination}')
print(f'{place} - {cost:.2f}')