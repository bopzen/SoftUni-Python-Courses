from project.shopping_cart import ShoppingCart
import unittest


class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart('Shop', 1000)

    def test_init_method(self):
        self.assertEqual('Shop', self.cart.shop_name)
        self.assertEqual(1000, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_shop_name_validation_starts_capital_letter(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = 'shop'
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_shop_name_validation_isalpha(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = 'Shop1'
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_add_to_cart_method_product_price_above_100_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart('product', 100)
        self.assertEqual("Product product cost too much!", str(ve.exception))

    def test_add_to_cart_method_product_correct(self):
        self.cart.products = {'P1': 10}
        result = self.cart.add_to_cart('P2', 50)
        self.assertEqual({'P1': 10, 'P2': 50}, self.cart.products)
        self.assertEqual("P2 product was successfully added to the cart!", result)

    def test_remove_from_cart_product_name_does_not_exist(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart('product')
        self.assertEqual("No product with name product in the cart!", str(ve.exception))

    def test_remove_from_cart_product_valid(self):
        self.cart.products = {'P1': 10, 'P2': 20}
        result = self.cart.remove_from_cart('P2')
        self.assertEqual({'P1': 10}, self.cart.products)
        self.assertEqual("Product P2 was successfully removed from the cart!", result)

    def test_overriding_add_method_valid(self):
        self.cart1 = ShoppingCart('ShopA', 1000)
        self.cart1.products = {'P1': 10, 'P2': 20}
        self.cart2 = ShoppingCart('ShopB', 1000)
        self.cart2.products = {'P3': 30, 'P4': 40}
        result = self.cart1.__add__(self.cart2)
        expected = ShoppingCart('ShopAShopB', 2000)
        expected.products = {'P1': 10, 'P2': 20, 'P3': 30, 'P4': 40}
        self.assertEqual(expected.shop_name, result.shop_name)
        self.assertEqual(expected.budget, result.budget)
        self.assertEqual(expected.products, result.products)

    def test_buy_products_method_total_sum_above_budget(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.budget = 19.53
            self.cart.products = {'P1': 10, 'P2': 20}
            self.cart.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with 10.47lv!", str(ve.exception))

    def test_buy_products_method_valid_total_sum(self):
        self.cart.budget = 50
        self.cart.products = {'P1': 10.54, 'P2': 20}
        result = self.cart.buy_products()
        self.assertEqual('Products were successfully bought! Total cost: 30.54lv.', result)


if __name__ == '__main__':
    unittest.main()