curr_command = input()
steps_count = 0
while curr_command != 'Going home':
    steps = int(curr_command)
    steps_count+=steps
    if steps_count >= 10000:
        break
    curr_command = input()
if curr_command == 'Going home':
    steps_home = int(input())
    steps_count +=steps_home
if steps_count >=10000:
    steps_over = steps_count - 10000
    print("Goal reached! Good job!")
    print(f"{steps_over} steps over the goal!")
else:
    steps_under = 10000 - steps_count
    print(f"{steps_under} more steps to reach goal.")