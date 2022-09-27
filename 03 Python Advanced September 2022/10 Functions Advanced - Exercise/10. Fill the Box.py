def fill_the_box (height, length, width, *args):
    volume = height * length * width
    filled = 0
    cubes = 0
    for element in args:
        if element == 'Finish':
            break
        cubes += element
    if filled + cubes > volume:
        cubes_left = filled + cubes - volume
        return f"No more free space! You have {cubes_left} more cubes."
    else:
        filled += cubes
        return f"There is free space in the box. You could put {volume-filled} more cubes."