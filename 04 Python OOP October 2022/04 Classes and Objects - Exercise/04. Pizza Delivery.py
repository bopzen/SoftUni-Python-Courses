class PizzaDelivery:
    ordered = False

    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredient, quantity, price_per_quantity):
        if PizzaDelivery.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity
        self.price += quantity * price_per_quantity

    def remove_ingredient(self, ingredient, quantity, price_per_quantity):
        if PizzaDelivery.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        else:
            if quantity > self.ingredients[ingredient]:
                return f"Please check again the desired quantity of {ingredient}!"
            else:
                self.ingredients[ingredient] -= quantity
                self.price -= quantity * price_per_quantity

    def make_order(self):
        PizzaDelivery.ordered = True
        return f"You've ordered pizza {self.name} prepared with {', '.join(f'{key}: {value}' for key, value in self.ingredients.items())} and the price will be {self.price}lv."