def get_magic_triangle(number):
    matrix = [[1], [1, 1]]
    for row in range(2, number):
        line = []
        for index in range(row+1):
            if index-1 < 0:
                neighbor_one = 0
            else:
                neighbor_one = matrix[row-1][index-1]
            if index == row:
                neighbor_two = 0
            else:
                neighbor_two = matrix[row-1][index]
            line.append(neighbor_one + neighbor_two)
        matrix.append(line)
    return matrix