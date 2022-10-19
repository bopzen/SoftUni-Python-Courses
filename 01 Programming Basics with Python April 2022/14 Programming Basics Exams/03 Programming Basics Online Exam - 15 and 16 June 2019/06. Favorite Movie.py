counter = 0
is_limit_reached = False
best_score = 0
best_movie = ''
while True:
    movie = input()
    if movie == 'STOP':
        break
    counter += 1
    score = 0
    if counter == 7:
        is_limit_reached = True
        break
    for c in movie:
        if 65 <= ord(c) <= 90:
            score += ord(c) - len(movie)
        elif 97 <= ord(c) <= 122:
            score += ord(c) - 2 * len(movie)
        else:
            score += ord(c)
    if score > best_score:
        best_score = score
        best_movie = movie

if is_limit_reached:
    print("The limit is reached.")
print(f"The best movie for you is {best_movie} with {best_score} ASCII sum.")