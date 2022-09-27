def math_operations(*args, **kwargs):
    counter = 1
    result = ''
    for element in args:
        if counter == 1:
            kwargs['a'] += element
            counter += 1
        elif counter == 2:
            kwargs['s'] -= element
            counter += 1
        elif counter == 3:
            if element != 0:
                kwargs['d'] /= element
            counter += 1
        elif counter == 4:
            kwargs['m'] *= element
            counter =1
    sorted_result = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    for key, value in sorted_result:
        result += f"{key}: {value:.1f}\n"
    return result