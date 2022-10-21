size = 6
deposits = {
    'Water': 0,
    'Metal': 0,
    'Concrete': 0
}

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

current_row, current_col = 0, 0

matrix = [input().split() for _ in range(6)]

for row in matrix:
    for element in row:
        if element == 'E':
            current_row = matrix.index(row)
            current_col = row.index(element)

commands = input().split(", ")

for command in commands:
    current_row += directions[command][0]
    current_col += directions[command][1]
    if current_row < 0:
        current_row = size - 1
    elif current_row > size - 1:
        current_row = 0
    if current_col < 0:
        current_col = size - 1
    elif current_col > size - 1:
        current_col = 0
    if matrix[current_row][current_col] == 'R':
        print(f"Rover got broken at ({current_row}, {current_col})")
    elif matrix[current_row][current_col] == 'W':
        deposits['Water'] += 1
        print(f"Water deposit found at ({current_row}, {current_col})")
    elif matrix[current_row][current_col] == 'M':
        deposits['Metal'] += 1
        print(f"Metal deposit found at ({current_row}, {current_col})")
    elif matrix[current_row][current_col] == 'C':
        deposits['Concrete'] += 1
        print(f"Concrete deposit found at ({current_row}, {current_col})")

if deposits['Water'] > 0 and deposits['Metal'] and deposits['Concrete'] > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")