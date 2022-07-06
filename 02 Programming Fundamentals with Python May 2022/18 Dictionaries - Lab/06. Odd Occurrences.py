list_words = input().lower().split()
dict_words = {}

for element in list_words:
    if element not in dict_words:
        dict_words[element] = 0
    dict_words[element] += 1

for key, value in dict_words.items():
    if value % 2 != 0:
        print(key, end=" ")