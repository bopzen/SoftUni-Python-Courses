def loading_bar(number):
    bar_length = number // 10
    empty_length = 10 - bar_length
    if bar_length == 10:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        print(f"{number}%", end=' ')
        print("[", end='')
        print("%" * bar_length, end='')
        print("." * empty_length, end='')
        print("]")
        print("Still loading...")


loading_bar(int(input()))