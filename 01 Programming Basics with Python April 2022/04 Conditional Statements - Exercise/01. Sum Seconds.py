time1 = int(input())
time2 = int(input())
time3 = int(input())
total_time_sec = time1 + time2 + time3
total_time_min = total_time_sec // 60
remaining_sec = total_time_sec % 60
if remaining_sec >= 10:
    print(f"{total_time_min}:{remaining_sec}")
else:
    print(f"{total_time_min}:0{remaining_sec}")