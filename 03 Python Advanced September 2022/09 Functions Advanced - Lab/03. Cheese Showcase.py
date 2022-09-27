def sorting_cheeses(**kwargs):
    sorted_result = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []
    for key, value in sorted_result:
        sorted_value = sorted(value, reverse=True)
        result.append(key)
        result.extend(sorted_value)
    return '\n'.join([str(x) for x in result])