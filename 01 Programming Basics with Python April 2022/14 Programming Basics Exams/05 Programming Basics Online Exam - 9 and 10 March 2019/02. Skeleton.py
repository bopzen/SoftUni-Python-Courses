control_minutes = int(input())
control_seconds = int(input())
alley_length = float(input())
speed_100m = int(input())
control_time_sec = control_minutes * 60 + control_seconds
slowing_down = (alley_length / 120) * 2.5
marin_time = alley_length * speed_100m /100 - slowing_down
if marin_time <= control_time_sec:
    print(f'Marin Bangiev won an Olympic quota!')
    print(f'His time is {marin_time:.3f}.')
else:
    diff = marin_time - control_time_sec
    print(f'No, Marin failed! He was {diff:.3f} second slower.')