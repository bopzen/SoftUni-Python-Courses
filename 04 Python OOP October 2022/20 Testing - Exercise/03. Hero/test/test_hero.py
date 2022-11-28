import unittest

from project.hero import Hero


class HeroTest(unittest.TestCase):
    def setUp(self):
        self.hero = Hero('Ivan', 1, 100, 100)
        self.enemy = Hero('Gosho', 1, 50, 50)

    def test_init_method(self):
        self.assertEqual('Ivan', self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_battle_method_username_validation_exception_error(self):
        with self.assertRaises(Exception) as ee:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ee.exception))

    def test_battle_method_health_validation_exception_error(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_method_enemy_health_validation_exception_error(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight Gosho. He needs to rest", str(ve.exception))

    def test_battle_method_draw(self):
        self.hero = Hero('Ivan', 1, 100, 100)
        self.enemy = Hero('Gesho', 1, 100, 100)
        result = self.hero.battle(self.enemy)
        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, self.enemy.health)
        self.assertEqual('Draw', result)

    def test_battle_method_win(self):
        self.hero = Hero('Ivan', 1, 100, 100)
        self.enemy = Hero('Gosho', 1, 80, 80)
        result = self.hero.battle(self.enemy)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(25, self.hero.health)
        self.assertEqual(105, self.hero.damage)
        self.assertEqual('You win', result)

    def test_battle_method_lose(self):
        self.hero = Hero('Ivan', 1, 80, 80)
        self.enemy = Hero('Gosho', 1, 100, 100)
        result = self.hero.battle(self.enemy)
        self.assertEqual(2, self.enemy.level)
        self.assertEqual(25, self.enemy.health)
        self.assertEqual(105, self.enemy.damage)
        self.assertEqual("You lose", result)

    def test_str_method_success(self):
        result = self.hero.__str__()
        expected = f"Hero Ivan: 1 lvl\n" \
               f"Health: 100\n" \
               f"Damage: 100\n"
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()