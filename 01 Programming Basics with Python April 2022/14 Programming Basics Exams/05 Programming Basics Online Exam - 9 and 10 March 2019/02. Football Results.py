result1 = input()
result2 = input()
result3 = input()
won = 0
lost = 0
draw = 0
if result1[0] > result1[2]:
    won +=1
elif result1[0] < result1[2]:
    lost +=1
else:
    draw +=1

if result2[0] > result2[2]:
    won +=1
elif result2[0] < result2[2]:
    lost +=1
else:
    draw +=1

if result3[0] > result3[2]:
    won +=1
elif result3[0] < result3[2]:
    lost +=1
else:
    draw +=1

print(f'Team won {won} games.')
print(f'Team lost {lost} games.')
print(f'Drawn games: {draw}')