def even_odd_filter(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if key == 'odd':
            result[key] = (list(filter(lambda x: x % 2 != 0, value)))
        elif key == 'even':
            result[key] = (list(filter(lambda x: x % 2 == 0, value)))
    result_sorted = sorted(result.items(), key=lambda x: -len(x[1]))
    result_dict = {}
    for key, value in result_sorted:
        result_dict[key] = value
    return result_dict