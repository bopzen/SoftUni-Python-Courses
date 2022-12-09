from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    receipt_id = 1

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def __check_if_client_is_registered(self, phone_number):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return True
        return False

    def __validate_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

    def __get_client(self, client_phone_number):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                return client

    def register_client(self, client_phone_number):
        if self.__check_if_client_is_registered(client_phone_number):
            raise Exception("The client has already been registered!")
        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            if meal.__class__.__name__ in ["Starter", "MainDish", "Dessert"]:
                self.menu.append(meal)

    def show_menu(self):
        self.__validate_menu()
        return "\n".join(meal.details() for meal in self.menu)

    def add_meals_to_shopping_cart(self, client_phone_number, **meal_names_and_quantities):
        self.__validate_menu()
        if not self.__check_if_client_is_registered(client_phone_number):
            self.register_client(client_phone_number)
        client = self.__get_client(client_phone_number)

        meals_to_order = []
        current_bill = 0

        for meal_name, quantity in meal_names_and_quantities.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    if meal.quantity >= quantity:
                        meals_to_order.append(meal)
                        current_bill += meal.price * quantity
                        break
                    else:
                        raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")
            else:
                raise Exception(f"{meal_name} is not on the menu!")

        client.shopping_cart.extend(meals_to_order)
        client.bill += current_bill

        for meal_name, quantity in meal_names_and_quantities.items():
            client.ordered_meals[meal_name] = quantity
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity -= quantity

        return f"Client {client_phone_number} successfully ordered {', '.join(m.name for m in client.shopping_cart)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number):
        client = self.__get_client(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal_name, quantity in client.ordered_meals.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity += quantity

        client.shopping_cart = []
        client.ordered_meals = {}
        client.bill = 0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number):
        client = self.__get_client(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        result = f"Receipt #{self.receipt_id} with total amount of {client.bill:.2f} was successfully paid for {client_phone_number}."
        self.receipt_id += 1
        client.shopping_cart = []
        client.ordered_meals = {}
        client.bill = 0

        return result

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."



