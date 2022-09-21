from collections import deque
rows, cols = [int(x) for x in input().split()]
snake = deque(input())
matrix = [[0 for col in range(cols)] for row in range(rows)]
for row in range(rows):
    if row % 2 == 0:
        for col in range(cols):
            char = snake.popleft()
            matrix[row][col] = char
            snake.append(char)
    else:
        for col in range(cols-1, -1, -1):
            char = snake.popleft()
            matrix[row][col] = char
            snake.append(char)
for row in range(rows):
    print(''.join(str(x) for x in matrix[row]))



