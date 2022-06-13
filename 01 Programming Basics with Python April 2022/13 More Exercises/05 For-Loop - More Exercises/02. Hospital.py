period = int(input())
doctors = 7
checked_per_day = 0
unchecked_per_day = 0
total_checked = 0
total_unchecked = 0
for i in range(1,period+1):
    patients_per_day = int(input())
    if i % 3 == 0:
        if total_unchecked > total_checked:
            doctors +=1
    if patients_per_day > doctors:
        checked_per_day = doctors
        unchecked_per_day = patients_per_day - checked_per_day
    else:
        checked_per_day = patients_per_day
        unchecked_per_day = 0
    total_checked += checked_per_day
    total_unchecked +=unchecked_per_day
print(f'Treated patients: {total_checked}.')
print(f'Untreated patients: {total_unchecked}.')