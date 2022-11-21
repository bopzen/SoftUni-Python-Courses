class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.dict_list = list(self.dictionary.items())

    def __iter__(self):
        return self

    def __next__(self):
        if not self.dict_list:
            raise StopIteration
        return self.dict_list.pop(0)