def concatenate(*args,**kwargs):
    result = ''
    for element in args:
        result += element
    for key, value in kwargs.items():
        if key in result:
            result = result.replace(key,value)
    return result