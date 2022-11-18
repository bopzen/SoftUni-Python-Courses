class vowels:
    All_VOWELS = 'AOIUYEaoiuye'
    def __init__(self, text):
        self.text = text
        self.vowels_int_text = [ch for ch in text if ch in vowels.All_VOWELS]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.vowels_int_text:
            raise StopIteration
        return self.vowels_int_text.pop(0)