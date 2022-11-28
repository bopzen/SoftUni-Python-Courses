import unittest

from project.mammal import Mammal


class MammalTest(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal('Lion', 'Cats', "Roar")

    def test_init_method(self):
        self.assertEqual('Lion', self.mammal.name)
        self.assertEqual('Cats', self.mammal.type)
        self.assertEqual('Roar', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound_method_success(self):
        result = self.mammal.make_sound()
        self.assertEqual('Lion makes Roar', result)

    def test_get_kingdom_method_success(self):
        result = self.mammal.get_kingdom()
        self.assertEqual('animals', result)

    def test_info_method_success(self):
        result = self.mammal.info()
        self.assertEqual("Lion is of type Cats", result)


if __name__ == '__main__':
    unittest.main()
