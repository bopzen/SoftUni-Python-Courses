import unittest


class IntegerListTests(unittest.TestCase):
    def setUp(self):
        self.integers = IntegerList(1, 2, 'a', False, 3)

    def test_init_method(self):
        self.assertEqual([1, 2, 3], self.integers._IntegerList__data)

    def test_add_method_type_not_int_exception_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integers.add('Test')
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_method_adding_element(self):
        self.integers.add(4)
        self.assertEqual([1, 2, 3, 4], self.integers._IntegerList__data)

    def test_remove_index_method_invalid_index_exception_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integers.remove_index(5)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_index_method_success(self):
        result = self.integers.remove_index(1)
        self.assertEqual([1, 3], self.integers._IntegerList__data)
        self.assertEqual(2, result)

    def test_get_method_invalid_index_exception_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integers.get(5)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_method_success(self):
        result = self.integers.get(1)
        self.assertEqual(2, result)

    def test_insert_method_invalid_index_exception_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integers.insert(5, 5)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_method_invalid_element_exception_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integers.insert(2, '5')
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_method_success(self):
        self.integers.insert(2, 5)
        self.assertEqual([1, 2, 5, 3], self.integers._IntegerList__data)

    def test_get_biggest_method(self):
        result = self.integers.get_biggest()
        self.assertEqual(3, result)

    def test_get_index_success(self):
        result = self.integers.get_index(1)
        self.assertEqual(0, result)

if __name__ == '__main__':
    unittest.main()
