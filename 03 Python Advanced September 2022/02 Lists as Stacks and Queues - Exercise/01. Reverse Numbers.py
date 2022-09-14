integers = input().split()
stack = []

while len(integers):
    stack.append(integers.pop())

print(' '.join(stack))