hour_exam = int(input())
minutes_exam = int(input())
hour_arrival = int(input())
minutes_arrival = int(input())
late = 'Late'
on_time = 'On time'
early = 'Early'
exam_time = hour_exam * 60 + minutes_exam
arrival_time = hour_arrival * 60 + minutes_arrival
time_diff = arrival_time - exam_time
student_arrival = late
if time_diff <-30:
    student_arrival = early
elif time_diff <=0:
    student_arrival = on_time
result = ''
if time_diff != 0:
    hours_diff = abs(time_diff) // 60
    minutes_diff = abs(time_diff) % 60
    if hours_diff >0:
        result = f'{hours_diff}:{minutes_diff:02} hours'
    else:
        result = f'{minutes_diff} minutes'
    if time_diff < 0:
        result+= ' before the start'
    else:
        result += ' after the start'
print(student_arrival)
if result:
    print(result)