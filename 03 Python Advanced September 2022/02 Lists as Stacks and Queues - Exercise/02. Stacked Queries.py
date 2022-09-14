stack = []
n = int(input())
for _ in range(n):
    query = input().split()
    if query[0] == '1':
        number = int(query[1])
        stack.append(number)
    elif query[0] == '2':
        if len(stack):
            stack.pop()
    elif query[0] == '3':
        if len(stack):
            print(max(stack))
    elif query[0] == '4':
        if len(stack):
            print(min(stack))
if len(stack):
    print(', '.join(map(str, [stack[i] for i in range(len(stack)-1, -1, -1)])))