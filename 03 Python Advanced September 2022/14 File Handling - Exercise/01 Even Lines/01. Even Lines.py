symbols = ["-", ",", ".", "!", "?"]
line_index = 0
with open('text.txt', 'r') as file:
    lines = file.readlines()
    for index in range(0, len(lines), 2):
        line = lines[index]
        for symbol in symbols:
            line = line.replace(symbol, '@')
        reversed_line = reversed(line.split())
        print(' '.join(reversed_line))