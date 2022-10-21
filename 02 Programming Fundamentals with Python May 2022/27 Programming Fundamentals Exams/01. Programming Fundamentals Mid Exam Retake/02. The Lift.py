people = int(input())
lift_status = list(map(int,input().split()))
remaining_people = people
is_queue_finished = False
for index in range(len(lift_status)):
    if lift_status[index] < 4:
        people_get_on_lift = 4 - lift_status[index]
        if people_get_on_lift > remaining_people:
            lift_status[index] += remaining_people
            is_queue_finished = True
            break
        else:
            lift_status[index] += people_get_on_lift
            remaining_people -= people_get_on_lift
if is_queue_finished:
    print("The lift has empty spots!")
elif not is_queue_finished and remaining_people > 0:
    print(f"There isn't enough space! {remaining_people} people in a queue!")
print(" ".join(list(map(str,lift_status))))