text = input()
parentheses = []
for i in range(len(text)):
    if text[i] == "(":
        parentheses.append(i)
    elif text[i] == ")":
        start_index = parentheses.pop()
        end_index = i + 1
        print(text[start_index : end_index])