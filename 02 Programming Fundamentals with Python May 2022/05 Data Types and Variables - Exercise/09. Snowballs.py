n = int(input())
best_snowball_value = 0
best_snowball_weight = 0
best_time_needed = 0
best_quality = 0
for i in range(n):
    snowball_weight = int(input())
    time_needed = int(input())
    quality = int(input())
    snowball_value = int((snowball_weight / time_needed) ** quality)
    if snowball_value > best_snowball_value:
        best_snowball_value = snowball_value
        best_snowball_weight = snowball_weight
        best_time_needed = time_needed
        best_quality = quality
print(f"{best_snowball_weight} : {best_time_needed} = {best_snowball_value} ({best_quality})")