class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.counter = 1
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > self.number:
            raise StopIteration
        index = self.index
        if self.index == len(self.sequence)-1:
            self.index = 0
        else:
            self.index +=1
        self.counter += 1
        return self.sequence[index]