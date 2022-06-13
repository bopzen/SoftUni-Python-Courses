actor_name = input()
academy_points = float(input())
count_jury = int(input())
points = 0
previous_points = academy_points
for i in range(count_jury):
    jury_name = input()
    jury_points = float(input())
    points = previous_points + len(jury_name) * jury_points / 2
    if points > 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!')
        break
    previous_points = points
if points <= 1250.5:
    points_needed = 1250.5 - points
    print(f'Sorry, {actor_name} you need {points_needed:.1f} more!')