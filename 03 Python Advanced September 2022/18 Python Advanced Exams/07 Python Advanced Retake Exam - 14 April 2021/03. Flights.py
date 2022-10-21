def flights(*args):
    flights_dict = {}
    flights_list = []
    for arg in args:
        if arg == 'Finish':
            break
        flights_list.append(arg)

    for index in range(0, len(flights_list) - 1, 2):
        if flights_list[index] not in flights_dict:
            flights_dict[flights_list[index]] = 0
        flights_dict[flights_list[index]] += flights_list[index + 1]
    return flights_dict