jobs = list(map(int, input().split(", ")))
index = int(input())
cycles = 0
target_task = jobs[index]

jobs_list = []
for i in range(len(jobs)):
    if jobs[i] < target_task:
        jobs_list.append(jobs[i])
    elif jobs[i] == target_task and i < index:
        jobs_list.append(jobs[i])
jobs_list.append(target_task)

print(sum(jobs_list))