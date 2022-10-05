with open('text.txt', 'r') as file_text, open('output.txt', 'w') as file_output:
    lines = file_text.readlines()
    for index in range(len(lines)):
        lines[index] = lines[index].replace('\n', '')
        count_letters = 0
        count_punctuations = 0
        for ch in lines[index]:
            if ch.isalnum():
                count_letters += 1
            else:
                if ch != ' ':
                    count_punctuations += 1
        file_output.write(f'Line {index+1}: {lines[index]} ({count_letters})({count_punctuations})\n')