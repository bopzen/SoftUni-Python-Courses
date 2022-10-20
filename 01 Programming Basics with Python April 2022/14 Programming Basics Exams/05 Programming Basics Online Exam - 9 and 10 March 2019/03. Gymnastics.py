country = input()
instrument = input()
difficulty = 0
performance = 0
if country == 'Russia':
    if instrument == 'ribbon':
        difficulty = 9.1
        performance = 9.4
    elif instrument == 'hoop':
        difficulty = 9.3
        performance = 9.8
    elif instrument == 'rope':
        difficulty = 9.6
        performance = 9
elif country == 'Bulgaria':
    if instrument == 'ribbon':
        difficulty = 9.6
        performance = 9.4
    elif instrument == 'hoop':
        difficulty = 9.55
        performance = 9.75
    elif instrument == 'rope':
        difficulty = 9.5
        performance = 9.4
elif country == 'Italy':
    if instrument == 'ribbon':
        difficulty = 9.2
        performance = 9.5
    elif instrument == 'hoop':
        difficulty = 9.45
        performance = 9.35
    elif instrument == 'rope':
        difficulty = 9.7
        performance = 9.150
total_score = difficulty + performance
percent = (20 - total_score)/20*100
print(f'The team of {country} get {total_score:.3f} on {instrument}.')
print(f"{percent:.2f}%")