from collections import deque


def read_robots():
    result = {}
    robots_input = input().split(";")
    for robot in robots_input:
        robot_details = robot.split("-")
        name = robot_details[0]
        processing_time = int(robot_details[1])
        result[name] = processing_time
    return result


def read_products():
    result = deque()
    while True:
        command = input()
        if command == 'End':
            break
        result.append(command)
    return result


def convert_seconds(hours, minutes, seconds):
    return hours * 60 * 60 + minutes * 60 + seconds


def convert_time(time_in_seconds):
    hours = time_in_seconds // 3600
    minutes = (time_in_seconds % 3600) // 60
    seconds = (time_in_seconds % 3600) % 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


robots = read_robots()
available_robots = [robot for robot in robots.keys()]
processing_robots = {}
starting_time = [int(x) for x in input().split(":")]
time_seconds = convert_seconds(starting_time[0], starting_time[1], starting_time[2])

products = read_products()

while products:
    time_seconds = (time_seconds + 1) % (24 * 60 * 60)
    for robot_name in [robot for robot in processing_robots.keys()]:
        processing_robots[robot_name] -= 1
        if processing_robots[robot_name] <= 0:
            processing_robots.pop(robot_name)

    current_product = products.popleft()
    for robot_name in available_robots:
        if robot_name not in processing_robots:
            processing_robots[robot_name] = robots[robot_name]
            print(f'{robot_name} - {current_product} [{convert_time(time_seconds)}]')
            break
    else:
        products.append(current_product)