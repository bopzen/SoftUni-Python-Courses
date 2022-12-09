from project.plantation import Plantation


import unittest


class TestPlantation(unittest.TestCase):

    def setUp(self):
        self.plantation = Plantation(10)
        self.plants = {'Ivan': ['flower1', 'flower2'], 'Gosho': ['flower3', 'flower4']}
        self.workers = ['Ivan', 'Gosho']

    def test_init_method(self):
        self.assertEqual(10, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_setter_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1
        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_method_already_hired_exception(self):
        self.plantation.workers = self.workers
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker('Ivan')
        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker_method_success(self):
        result = self.plantation.hire_worker('Ivan')
        self.assertEqual("Ivan successfully hired.", result)
        self.assertEqual(['Ivan'], self.plantation.workers)

    def test_overriding_len_method(self):
        self.plantation.plants = self.plants
        self.assertEqual(4, len(self.plantation))

    def test_planting_method_invalid_worker_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting('Pesho', 'flower1')
        self.assertEqual("Worker with name Pesho is not hired!", str(ve.exception))

    def test_planting_method_size_limit_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation = Plantation(3)
            self.plantation.workers = self.workers
            self.plantation.plants = self.plants
            self.plantation.planting('Ivan', 'flower3')
        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_method_worker_with_plants_success(self):
        self.plantation.workers = self.workers
        self.plantation.plants = self.plants
        result = self.plantation.planting('Ivan', 'flower3')
        self.assertEqual("Ivan planted flower3.", result)
        self.assertEqual(
            {
            'Ivan': ['flower1', 'flower2', 'flower3'],
            'Gosho': ['flower3', 'flower4']
            }
            , self.plantation.plants)

    def test_planting_method_worker_without_plants_success(self):
        self.plantation.workers = self.workers
        self.plantation.plants = {
            'Ivan': ['flower1', 'flower2']
            }
        result = self.plantation.planting('Gosho', 'flower1')
        self.assertEqual("Gosho planted it's first flower1.", result)
        self.assertEqual(
            {
            'Ivan': ['flower1', 'flower2'],
            'Gosho': ['flower1']
            }
            , self.plantation.plants)

    def test_overriding_str_method(self):
        self.plantation.workers = self.workers
        self.plantation.plants = self.plants
        self.assertEqual(
            "Plantation size: 10\n"
            "Ivan, Gosho\n"
            "Ivan planted: flower1, flower2\n"
            "Gosho planted: flower3, flower4"
        , str(self.plantation)
        )

    def test_overriding_repr_method(self):
        self.plantation.workers = self.workers
        self.assertEqual(
            "Size: 10\n"
            "Workers: Ivan, Gosho"
        , repr(self.plantation)
        )


if __name__ == '__main__':
    unittest.main()