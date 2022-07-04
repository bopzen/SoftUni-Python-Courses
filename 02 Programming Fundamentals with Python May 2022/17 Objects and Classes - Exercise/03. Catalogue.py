class Catalogue:
    def __init__(self,name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        return [element for element in self.products if element[0] == first_letter]

    def __repr__(self):
        result = ""
        result += f"Items in the {self.name} catalogue:\n"
        result += f"\n".join(sorted(self.products))
        return result