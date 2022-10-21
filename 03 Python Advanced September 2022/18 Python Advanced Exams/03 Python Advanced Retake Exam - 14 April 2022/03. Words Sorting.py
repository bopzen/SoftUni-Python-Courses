def words_sorting(*words):
    words_dict = {}
    sum_ascii_values = 0
    for word in words:
        ascii_value = 0
        for ch in word:
            ascii_value += ord(ch)
        words_dict[word] = ascii_value
        sum_ascii_values += ascii_value
    if sum_ascii_values % 2 == 0:
        sorted_words_dict = sorted(words_dict.items(), key=lambda x: x[0])
    else:
        sorted_words_dict = sorted(words_dict.items(), key=lambda x: -x[1])

    return "\n".join([f"{key} - {value}" for key, value in sorted_words_dict])