list_population = list(map(int,input().split(",")))
minimum_wealth = int(input())
for i in range(len(list_population)):
    if list_population[i] < minimum_wealth:
        needed_wealth = minimum_wealth - list_population[i]
        while list_population[i] < minimum_wealth:
            wealthiest = max(list_population)
            if wealthiest == minimum_wealth:
                break
            wealthiest_index = list_population.index(wealthiest)
            if list_population[wealthiest_index] > minimum_wealth:
                extra_wealth = list_population[wealthiest_index] - minimum_wealth
                if extra_wealth >= needed_wealth:
                    list_population[i] += needed_wealth
                    list_population[wealthiest_index] -= needed_wealth
                    break
                else:
                    list_population[i] += extra_wealth
                    list_population[wealthiest_index] -= extra_wealth
    else:
        continue
if min(list_population) < minimum_wealth:
    print("No equal distribution possible")
else:
    print(list_population)
