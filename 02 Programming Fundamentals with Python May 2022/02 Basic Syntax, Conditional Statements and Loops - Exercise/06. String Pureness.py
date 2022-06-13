n = int(input())
is_pure = True
for i in range(n):
    text = input()
    is_pure = True
    for c in text:
        if c == ',' or c == '.' or c == '_':
            is_pure = False
            break
    if is_pure:
        print(f"{text} is pure.")
    else:
        print(f"{text} is not pure!")