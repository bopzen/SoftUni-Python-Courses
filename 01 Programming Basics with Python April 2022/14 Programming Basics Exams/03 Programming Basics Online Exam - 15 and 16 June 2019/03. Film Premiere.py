movie = input()
package = input()
count_tickets = int(input())
cost = 0
if movie == 'John Wick':
    if package == 'Drink':
        cost = count_tickets * 12
    elif package == 'Popcorn':
        cost = count_tickets * 15
    elif package == 'Menu':
        cost = count_tickets * 19
elif movie == 'Star Wars':
    if package == 'Drink':
        cost = count_tickets * 18
    elif package == 'Popcorn':
        cost = count_tickets * 25
    elif package == 'Menu':
        cost = count_tickets * 30
elif movie == 'Jumanji':
    if package == 'Drink':
        cost = count_tickets * 9
    elif package == 'Popcorn':
        cost = count_tickets * 11
    elif package == 'Menu':
        cost = count_tickets * 14

if movie == 'Star Wars' and count_tickets >= 4:
    cost -= cost * 0.3
if movie == 'Jumanji' and count_tickets == 2:
    cost -= cost * 0.15

print(f"Your bill is {cost:.2f} leva.")