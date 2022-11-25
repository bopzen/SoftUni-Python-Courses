import unittest


class CatTests(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("Tom")

    def test_eat_method_cat_size_increased(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_eat_method_if_cat_is_fed(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_eat_method_fed_exception_error(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_sleep_method_not_fed_exception_error(self):
        self.cat.fed = False
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_sleep_method_not_sleepy_after_sleeping(self):
        self.cat.fed = True
        self.cat.sleepy = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)
        
        
if __name__ == '__main__':
    unittest.main()