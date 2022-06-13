change = float(input())
change_left = int(change * 100)

count_2lev = 0
count_1lev = 0
count_50st = 0
count_20st = 0
count_10st = 0
count_5st = 0
count_2st = 0
count_1st = 0

while change_left >0:
    if change_left // 200 > 0:
        count_2lev += change_left // 200
        change_left -= count_2lev * 200
    elif change_left // 100 > 0:
        count_1lev += change_left // 100
        change_left -= count_1lev * 100
    elif change_left // 50 > 0:
        count_50st += change_left // 50
        change_left -= count_50st * 50
    elif change_left // 20 > 0:
        count_20st += change_left // 20
        change_left -= count_20st * 20
    elif change_left // 10 > 0:
        count_10st += change_left // 10
        change_left -= count_10st * 10
    elif change_left // 5 > 0:
        count_5st += change_left // 5
        change_left -= count_5st * 5
    elif change_left // 2 > 0:
        count_2st += change_left // 2
        change_left -= count_2st * 2
    elif change_left // 1 > 0:
        count_1st += change_left // 1
        change_left -= count_1st * 1
count = count_2lev + count_1lev + count_50st + count_20st + count_10st + count_5st + count_2st + count_1st
print(count)