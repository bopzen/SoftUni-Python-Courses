def vowel_filter(function):
    def wrapper():
        result = function()
        vowels_result = [x for x in result if x.lower() in 'aoiuye']
        return vowels_result

    return wrapper