class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.counter = 0
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >= self.count:
            raise StopIteration
        number = self.num
        self.num += self.step
        self.counter += 1
        return number