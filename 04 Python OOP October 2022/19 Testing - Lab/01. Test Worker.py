import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.person = Worker('Ivan Ivanov', 2000, 20)

    def test_init_method(self):
        self.assertEqual('Ivan Ivanov', self.person.name)
        self.assertEqual(2000, self.person.salary)
        self.assertEqual(20, self.person.energy)

    def test_rest_method_energy_increment(self):
        self.person.rest()
        self.assertEqual(21, self.person.energy)

    def test_work_method_negative_energy_exception_error(self):
        self.person.energy = 0
        with self.assertRaises(Exception) as ex:
            self.person.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_work_method_money_increased(self):
        self.person.work()
        self.assertEqual(2000, self.person.money)

    def test_work_method_energy_decreased(self):
        self.person.work()
        self.assertEqual(19, self.person.energy)

    def test_get_info_method_correct_output(self):
        self.assertEqual('Ivan Ivanov has saved 0 money.', self.person.get_info())

if __name__ == '__main__':
  unittest.main()