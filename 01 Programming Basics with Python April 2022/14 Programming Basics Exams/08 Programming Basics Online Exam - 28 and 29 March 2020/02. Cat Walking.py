time_walks = int(input())
count_walks = int(input())
calories = int(input())
burned = time_walks*count_walks*5
if burned >= calories*0.5:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {burned}. ')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {burned}.')