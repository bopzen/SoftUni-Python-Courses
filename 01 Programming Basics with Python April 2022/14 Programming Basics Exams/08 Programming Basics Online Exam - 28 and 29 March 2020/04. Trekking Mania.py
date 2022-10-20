count_groups = int(input())
trekkers_musala = 0
trekkers_monblan = 0
trekkers_kilimanjaro = 0
trekkers_k2 = 0
trekkers_everest = 0
total_trekkers = 0
for i in range(count_groups):
    trekkers_in_group = int(input())
    total_trekkers += trekkers_in_group
    if trekkers_in_group <= 5:
        trekkers_musala +=trekkers_in_group
    elif trekkers_in_group <= 12:
        trekkers_monblan +=trekkers_in_group
    elif trekkers_in_group <= 25:
        trekkers_kilimanjaro +=trekkers_in_group
    elif trekkers_in_group <= 40:
        trekkers_k2 +=trekkers_in_group
    else:
        trekkers_everest +=trekkers_in_group
musala_percent = trekkers_musala / total_trekkers *100
monblan_percent = trekkers_monblan / total_trekkers *100
kilimanjaro_percent = trekkers_kilimanjaro / total_trekkers *100
k2_percent = trekkers_k2 / total_trekkers *100
everest_percent = trekkers_everest / total_trekkers *100

print(f'{musala_percent:.2f}%')
print(f'{monblan_percent:.2f}%')
print(f'{kilimanjaro_percent:.2f}%')
print(f'{k2_percent:.2f}%')
print(f'{everest_percent:.2f}%')
