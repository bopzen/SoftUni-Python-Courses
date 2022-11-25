import unittest


class CarTest(unittest.TestCase):
    def setUp(self):
        self.car = Car('BMW', '3', 10, 60)

    def test_init_method(self):
        self.assertEqual('BMW', self.car.make)
        self.assertEqual('3', self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_exception_error(self):
        with self.assertRaises(Exception) as ee:
            self.car.make = ''
        self.assertEqual("Make cannot be null or empty!", str(ee.exception))

    def test_model_exception_error(self):
        with self.assertRaises(Exception) as ee:
            self.car.model = ''
        self.assertEqual("Model cannot be null or empty!", str(ee.exception))

    def test_fuel_consumption_exception_error(self):
        with self.assertRaises(Exception) as ee:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ee.exception))

    def test_fuel_capacity_exception_error(self):
        with self.assertRaises(Exception) as ee:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ee.exception))

    def test_fuel_amount_exception_error(self):
        with self.assertRaises(Exception) as ee:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ee.exception))

    def test_refuel_method_invalid_fuel_exception_error(self):
        with self.assertRaises(Exception) as ee:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ee.exception))

    def test_refuel_method_success(self):
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)
        self.car.refuel(100)
        self.assertEqual(60, self.car.fuel_amount)

    def test_drive_method_invalid_needed_exception_error(self):
        with self.assertRaises(Exception) as ee:
            self.car.drive(1000)
        self.assertEqual("You don't have enough fuel to drive!", str(ee.exception))

    def test_drive_method_success(self):
        self.car.fuel_amount = 10
        self.car.drive(10)
        self.assertEqual(9, self.car.fuel_amount)


if __name__ == '__main__':
    unittest.main()
