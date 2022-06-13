letter_start = input()
letter_end = input()
letter_excluded = input()
start = ord(letter_start)
end = ord(letter_end)

counter = 0
for letter1 in range(start,end+1):
    if chr(letter1) == letter_excluded:
        continue
    for letter2 in range(start,end+1):
        if chr(letter2) == letter_excluded:
            continue
        for letter3 in range(start,end+1):
            if chr(letter3) == letter_excluded:
                continue
            counter += 1
            print(chr(letter1) + chr(letter2) + chr(letter3), end=' ')
print(counter)