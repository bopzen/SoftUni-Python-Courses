import math
series = input()
seasons = int(input())
episodes = int(input())
time = float(input())

time_with_ads = time + time * 0.2

total_time = math.floor(seasons * episodes * time_with_ads + seasons*10)

print(f"Total time needed to watch the {series} series is {total_time} minutes.")


