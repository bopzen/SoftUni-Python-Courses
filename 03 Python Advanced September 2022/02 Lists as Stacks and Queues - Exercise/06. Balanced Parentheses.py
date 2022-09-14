parentheses = input()
stack = []
is_balanced = True
for element in parentheses:
    if element in ['{', '[', '(']:
        stack.append(element)
    elif element == '}':
        if not stack or stack[-1] != '{':
            is_balanced = False
            break
        else:
            stack.pop()
    elif element == ']':
        if not stack or stack[-1] != '[':
            is_balanced = False
            break
        else:
            stack.pop()
    elif element == ')':
        if not stack or stack[-1] != '(':
            is_balanced = False
            break
        else:
            stack.pop()

if is_balanced:
    print('YES')
else:
    print('NO')