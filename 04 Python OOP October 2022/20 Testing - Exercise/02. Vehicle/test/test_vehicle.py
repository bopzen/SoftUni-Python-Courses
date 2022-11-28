import unittest

from project.vehicle import Vehicle


class VehicleTest(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(100, 300)

    def test_init_method(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(300, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_method_not_enough_fuel_exception_error(self):
        with self.assertRaises(Exception) as ee:
            self.vehicle.drive(1000)
        self.assertEqual("Not enough fuel", str(ee.exception))

    def test_drive_method_success(self):
        self.vehicle.drive(10)
        self.assertEqual(87.5, self.vehicle.fuel)

    def test_refuel_method_too_much_fuel_exception_error(self):
        with self.assertRaises(Exception) as ee:
            self.vehicle.refuel(1000)
        self.assertEqual("Too much fuel", str(ee.exception))

    def test_refuel_method_success(self):
        self.vehicle.fuel = 10
        self.vehicle.refuel(10)
        self.assertEqual(20, self.vehicle.fuel)

    def test_str_method_success(self):
        result = self.vehicle.__str__()
        expected = "The vehicle has 300 " \
               "horse power with 100 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()