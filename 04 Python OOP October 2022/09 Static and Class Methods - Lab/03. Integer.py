class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if type(float_value) != float:
            return "value is not a float"
        result = int(float_value // 1)
        return cls(result)

    @classmethod
    def from_roman(cls, value):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(value)):
            if i > 0 and rom_val[value[i]] > rom_val[value[i - 1]]:
                result += rom_val[value[i]] - 2 * rom_val[value[i - 1]]
            else:
                result += rom_val[value[i]]
        return cls(result)

    @classmethod
    def from_string(cls, value):
        if type(value) != str:
            return 'wrong type'
        try:
            result = int(value)
            return cls(result)
        except:
            return 'wrong type'