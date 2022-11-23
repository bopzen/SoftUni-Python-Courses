from functools import wraps


def logged(function):
    @wraps(function)
    def wrapper(*args):
        result = function(*args)
        return f"you called {function.__name__}({', '.join(str(arg) for arg in args)})\nit returned {result}"

    return wrapper