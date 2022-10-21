def shopping_cart(*args):
    meals = {}
    meal_limits = {'Soup': 3,
                   'Pizza': 4,
                   'Dessert': 2,
                   }
    meals = {'Soup': [],
                   'Pizza': [],
                   'Dessert': [],
                   }
    result = ''
    for element in args:
        if element == 'Stop':
            break
        if len(meals[element[0]]) < meal_limits[element[0]] and element[1] not in meals[element[0]]:
            meals[element[0]].append(element[1])
    for products in meals.values():
        if len(products) > 0:
            break
    else:
        return "No products in the cart!"

    meals_sorted = sorted(meals.items(), key=lambda x: (-len(x[1]), x[0]))
    for meal, product in meals_sorted:
        result += f"{meal}:\n"
        for element in sorted(product):
            result += f" - {element}\n"
    return result