text = input()
chars = [ch for ch in text]
unique_chars = sorted(list(set(chars)))
for element in unique_chars:
    print(f'{element}: {chars.count(element)} time/s')