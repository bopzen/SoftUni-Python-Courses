char1 = input()
char2 = input()
text = input()
total_sum = 0
for ch in text:
    if min(ord(char1), ord(char2)) < ord(ch) < max(ord(char1), ord(char2)):
        total_sum += ord(ch)
print(total_sum)

