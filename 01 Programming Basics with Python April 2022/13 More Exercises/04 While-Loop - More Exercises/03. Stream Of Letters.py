is_met_c = False
is_met_n = False
is_met_o = False
word = ''

while True:
    if is_met_c and is_met_o and is_met_n:
        print(word, end=' ')
        is_met_c = False
        is_met_n = False
        is_met_o = False
        word = ''

    text_input = input()
    if text_input == 'End':
        break

    if not 65 <= ord(text_input) <= 90 and not 97 <= ord(text_input) <= 122:
        continue

    if text_input == 'c' and is_met_c == False:
        is_met_c = True
        continue
    elif text_input == 'c' and is_met_c == True:
        word += 'c'

    if text_input == 'n' and is_met_n == False:
        is_met_n = True
        continue
    elif text_input == 'n' and is_met_n == True:
        word += 'n'

    if text_input == 'o' and is_met_o == False:
        is_met_o = True
        continue
    elif text_input == 'o' and is_met_o == True:
        word += 'o'

    if text_input != 'c' and text_input != 'n' and text_input != 'o':
        word += text_input