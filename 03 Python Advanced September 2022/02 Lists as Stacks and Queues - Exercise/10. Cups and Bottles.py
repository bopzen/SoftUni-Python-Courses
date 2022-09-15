from collections import deque

cups = deque(list(map(int,input().split())))
bottles = list(map(int,input().split()))
wasted_water = 0
fail = False
while cups:
    current_cup = cups[0]
    if bottles:
        current_bottle = bottles.pop()
        if current_bottle >= current_cup:
            wasted_water += current_bottle - current_cup
            cups.popleft()
        else:
            while True:
                current_cup -= current_bottle
                if current_cup <= 0:
                    wasted_water += -current_cup
                    cups.popleft()
                    break
                if bottles:
                    current_bottle = bottles.pop()
                else:
                    fail = True
                    break
    else:
        fail = True
        break

if fail:
    print('Cups: ' + ' '.join(str(x) for x in cups))
else:
    print('Bottles: ' + ' '.join(str(x) for x in bottles))
print(f'Wasted litters of water: {wasted_water}')
