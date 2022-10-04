import re
words_dict = {}
pattern = r'[A-z]+'
with open('./words.txt', 'r') as file_words:
    words = file_words.read().split()
for word in words:
    words_dict[word] = 0
with open('./input.txt', 'r') as file_input:
    for line in file_input:
        all_line_words = re.findall(pattern, line.lower())
        for word in words:
            words_dict[word] += all_line_words.count(word)
sorted_words_dict = sorted(words_dict.items(), key=lambda x: -x[1])
with open('./output.txt', 'w') as file_output:
    for word, count in sorted_words_dict:
        file_output.write(f'{word} - {count}\n')