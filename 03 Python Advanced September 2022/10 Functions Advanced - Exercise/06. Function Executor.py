def func_executor(*args):
    result = []
    for key, value in args:
        result_func = key(*value)
        result.append(f"{key.__name__} - {result_func}")
    return '\n'.join(result)