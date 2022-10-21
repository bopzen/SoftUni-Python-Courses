from collections import deque

eggs = deque(list(map(int, input().split(', '))))
paper = list(map(int, input().split(', ')))
filled_boxes = 0

while eggs and paper:
    egg = eggs.popleft()
    if egg <= 0:
        continue
    elif egg == 13:
        paper[0], paper[-1] = paper[-1], paper[0]
    else:
        wrapped_egg = egg + paper.pop()
        if wrapped_egg <= 50:
            filled_boxes += 1

if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join([str(egg) for egg in eggs])}")
if paper:
    print(f"Pieces of paper left: {', '.join([str(p) for p in paper])}")