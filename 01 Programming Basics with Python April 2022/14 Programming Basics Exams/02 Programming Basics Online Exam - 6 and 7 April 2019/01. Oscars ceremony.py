rent = int(input())
statues = rent - rent * 0.3
cathering = statues - statues * 0.15
sound = cathering / 2
total = rent + statues + cathering + sound
print(f'{total:.2f}')