rooms = int(input())
free_chairs = 0
for room in range(1, rooms+1):
    list_chairs_visitors = input().split()
    chairs = len(list_chairs_visitors[0])
    visitors = int(list_chairs_visitors[1])
    free_chairs += chairs - visitors
    if chairs - visitors < 0:
        print(f"{abs(chairs - visitors)} more chairs needed in room {room}")
if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")