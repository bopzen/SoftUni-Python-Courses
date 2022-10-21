def naughty_or_nice_list(kids_names, *args, **kwargs):
    kids_dict = {
        'Nice': [],
        'Naughty': [],
        'Not found': []
    }
    result = []
    for arg in args:
        arg_elements = arg.split('-')
        number, category = int(arg_elements[0]), arg_elements[1]
        count_number = 0
        index_element = 0
        for element in kids_names:
            if element[0] == number:
                index_element = kids_names.index(element)
                count_number += 1
        if count_number == 1:
            kids_dict[category].append(kids_names[index_element][1])
            kids_names.pop(index_element)

    for name, category in kwargs.items():
        count_name = 0
        index_element = 0
        for element in kids_names:
            if element[1] == name:
                index_element = kids_names.index(element)
                count_name += 1
        if count_name == 1:
            kids_dict[category].append(name)
            kids_names.pop(index_element)
    for element in kids_names:
        kids_dict['Not found'].append(element[1])

    for category, name in kids_dict.items():
        if name:
            result.append(f"{category}: {', '.join(name)}")
    return '\n'.join(result)