movie = input()
hall = input()
sold_tickets = int(input())
profit = 0
if movie == 'A Star Is Born':
    if hall == 'normal':
        profit += sold_tickets * 7.5
    elif hall == 'luxury':
        profit += sold_tickets * 10.5
    elif hall == 'ultra luxury':
        profit += sold_tickets * 13.5
elif movie == 'Bohemian Rhapsody':
    if hall == 'normal':
        profit += sold_tickets * 7.35
    elif hall == 'luxury':
        profit += sold_tickets * 9.45
    elif hall == 'ultra luxury':
        profit += sold_tickets * 12.75
elif movie == 'Green Book':
    if hall == 'normal':
        profit += sold_tickets * 8.15
    elif hall == 'luxury':
        profit += sold_tickets * 10.25
    elif hall == 'ultra luxury':
        profit += sold_tickets * 13.25
elif movie == 'The Favourite':
    if hall == 'normal':
        profit += sold_tickets * 8.75
    elif hall == 'luxury':
        profit += sold_tickets * 11.55
    elif hall == 'ultra luxury':
        profit += sold_tickets * 13.95

print(f"{movie} -> {profit:.2f} lv.")
