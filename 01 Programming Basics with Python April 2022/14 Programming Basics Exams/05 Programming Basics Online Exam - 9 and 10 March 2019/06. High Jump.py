target_height = int(input())
height = target_height - 30
count_jumps = 0
attempts = 0
while height <= target_height:
    jump_height = int(input())
    count_jumps += 1
    if jump_height > height and height < target_height:
        height += 5
        attempts = 0
    elif jump_height > height and height == target_height:
        attempts = 0
        break
    else:
        attempts += 1
    if attempts == 3:
        break

if attempts == 3:
    print(f"Tihomir failed at {height}cm after {count_jumps} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {height}cm after {count_jumps} jumps.")

