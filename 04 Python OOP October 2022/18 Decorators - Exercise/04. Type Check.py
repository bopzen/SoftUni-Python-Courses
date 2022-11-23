def type_check(instance):
    def decorator(function):
        def wrapper(arg):
            if type(arg) != instance:
                return "Bad Type"
            result = function(arg)
            return result
        return wrapper
    return decorator