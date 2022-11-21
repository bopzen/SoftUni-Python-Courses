def read_next(*args):
    for arg in args:
        result = list(arg)
        for element in result:
            yield element