def age_assignment(*args, **kwargs):
    name_age = {}
    result = ''
    for name in args:
        name_age[name] = kwargs[name[0]]
    sorted_result = sorted(name_age.items(), key=lambda x: x[0])
    for key, value in sorted_result:
        result += f"{key} is {value} years old.\n"
    return result