movie = input()
days = int(input())
tickets = int(input())
ticket_price = float(input())
cinema_perc = int(input())

income = days * tickets * ticket_price
profit = income - income * cinema_perc / 100

print(f"The profit from the movie {movie} is {profit:.2f} lv.")


