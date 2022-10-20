count_kozunak = int(input())
max_baker_score = 0
best_baker = ''
for i in range(count_kozunak):
    baker_score = 0
    baker = input()
    while True:
        rating = input()
        if rating == 'Stop':
            break

        baker_score += int(rating)
    print(f"{baker} has {baker_score} points.")
    if baker_score > max_baker_score:
        max_baker_score = baker_score
        best_baker = baker
        print(f"{best_baker} is the new number 1!")
print(f"{best_baker} won competition with {max_baker_score} points!")