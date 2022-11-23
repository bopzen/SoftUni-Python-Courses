from time import time


def exec_time(function):
    def wrapper(*args):
        t1 = time()
        function(*args)
        t2 = time()
        return t2 - t1
    return wrapper