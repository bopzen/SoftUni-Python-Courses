import re
words_dict = {}
mirror_words = []
text = input()
search_pattern = r"(@|#)([A-Za-z]{3}[A-Za-z]*)\1\1([A-Za-z]{3}[A-Za-z]*)\1"
result = re.finditer(search_pattern, text)
for match in result:
    words_dict[match.group(2)] = match.group(3)
if len(words_dict) > 0:
    print(f"{len(words_dict)} word pairs found!")
else:
    print("No word pairs found!")

for left_word, right_word in words_dict.items():
    if left_word == right_word[::-1]:
        mirror_words.append(f"{left_word} <=> {right_word}")
if len(mirror_words) > 0:
    print("The mirror words are:")
    print(", ".join(mirror_words))
else:
    print("No mirror words!")

