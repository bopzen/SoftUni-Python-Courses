time = int(input())
count_scenes = int(input())
time_scene = int(input())
time_prep = time * 0.15
needed_time = count_scenes * time_scene + time_prep

if time >= needed_time:
    time_left = int(round(time - needed_time,0))
    print(f"You managed to finish the movie on time! You have {time_left} minutes left!")
else:
    time_needed = int(round(needed_time - time,0))
    print(f"Time is up! To complete the movie you need {time_needed} minutes.")

