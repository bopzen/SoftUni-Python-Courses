list_numbers = list(map(int,input().split(", ")))
boundary = 10
while len(list_numbers) > 0:
    list_boundary = list(filter(lambda x: x <= boundary,list_numbers))
    list_numbers = list(filter(lambda x: x > boundary,list_numbers))
    print(f"Group of {boundary}'s: {list_boundary}")
    boundary += 10