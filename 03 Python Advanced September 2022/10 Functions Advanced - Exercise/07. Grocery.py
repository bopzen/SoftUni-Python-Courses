def grocery_store(**kwargs):
    result = ''
    sorted_result = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    for key, value in sorted_result:
        result += f"{key}: {value}\n"
    return result