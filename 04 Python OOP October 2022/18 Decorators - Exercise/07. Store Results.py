class store_results:

    _log_file = 'results.txt'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        result = self.func(*args)
        text = f"Function '{self.func.__name__}' was called. Result: {result}"
        with open(self._log_file, 'a') as opened_file:
            opened_file.write(text + '\n')

        return result