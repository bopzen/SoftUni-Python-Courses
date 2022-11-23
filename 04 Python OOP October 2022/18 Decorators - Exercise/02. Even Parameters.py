def even_parameters(function):
    def wrapper(*args):
        for arg in args:
            if isinstance(arg, str) or arg % 2 != 0:
                return "Please use only even numbers!"
        result = function(*args)
        return result
    return wrapper