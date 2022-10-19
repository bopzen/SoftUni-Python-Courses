import math
most_powerful_word = ''
max_sum_ascii = 0
while True:
    sum_ascii = 0
    word = input()
    if word == 'End of words':
        break
    for c in word:
        sum_ascii += ord(c)
    first_letter = word[0].lower()
    if first_letter == 'a' or first_letter == 'e' or first_letter == 'i' or first_letter == 'o' or first_letter == 'u' or first_letter == 'y':
        sum_ascii = sum_ascii * len(word)
    else:
        sum_ascii = math.floor(sum_ascii/len(word))
    if sum_ascii > max_sum_ascii:
        max_sum_ascii = sum_ascii
        most_powerful_word = word
print(f"The most powerful word is {most_powerful_word} - {max_sum_ascii}" )

