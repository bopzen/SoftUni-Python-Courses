import sys

count_movies = int(input())
best_movie = ''
worst_movie = ''
best_rating = 0
worst_rating = sys.maxsize
total_rating = 0
for i in range(count_movies):
    movie = input()
    rating = float(input())
    if rating > best_rating:
        best_rating = rating
        best_movie = movie
    if rating < worst_rating:
        worst_rating = rating
        worst_movie = movie
    total_rating += rating
average_rating = total_rating / count_movies
print(f"{best_movie} is with highest rating: {best_rating:.1f}")
print(f"{worst_movie} is with lowest rating: {worst_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")

