tickets = input().split(",")
tickets = [element.strip() for element in tickets]


def count_next(symbol, left, right):
    counter = 6
    for i in range(7,11):
        if i * symbol in left and i * symbol in right:
            counter += 1
    return counter


for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
        continue
    left_ticket = ticket[:int(len(ticket)/2)]
    right_ticket = ticket[int(len(ticket)/2):]
    if 6 * '@' in left_ticket and 6 * '@' in right_ticket:
        count = count_next("@",left_ticket, right_ticket)
        symbol = '@'
    elif 6 * '#' in left_ticket and 6 * '#' in right_ticket:
        count = count_next('#', left_ticket, right_ticket)
        symbol = '#'
    elif 6 * '$' in left_ticket and 6 * '$' in right_ticket:
        count = count_next('$', left_ticket, right_ticket)
        symbol = '$'
    elif 6 * '^' in left_ticket and 6 * '^' in right_ticket:
        count = count_next('^', left_ticket, right_ticket)
        symbol = '^'
    else:
        print(f'ticket "{ticket}" - no match')
        continue

    if count != 10:
        print(f'ticket "{ticket}" - {count}{symbol}')
    else:
        print(f'ticket "{ticket}" - {count}{symbol} Jackpot!')

