numbers = input().split("|")
matrix = [number.split() for number in numbers]
flatten = [num for row in range(len(matrix)-1, -1, -1) for num in matrix[row]]
print(*flatten)