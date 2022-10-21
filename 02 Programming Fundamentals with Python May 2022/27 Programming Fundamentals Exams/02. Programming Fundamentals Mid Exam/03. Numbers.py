list_numbers = list(map(int,input().split()))
average = sum(list_numbers)/len(list_numbers)
list_above_average = list(filter(lambda x: x > average,list_numbers))
list_above_average.sort(reverse = True)
list_top_5 = [list_above_average[num] for num in range(min(5,len(list_above_average)))]
if len(list_top_5) == 0:
    print("No")
else:
    print(" ".join(map(str,list_top_5)))
