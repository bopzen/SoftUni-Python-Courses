from project.movie import Movie
import unittest


class TestMovie(unittest.TestCase):
    def setUp(self):
        self.movie = Movie('Name', 2000, 5.5)
        self.actors = ['Actor1', 'Actor2']

    def test_init_method(self):
        self.assertEqual('Name', self.movie.name)
        self.assertEqual(2000, self.movie.year)
        self.assertEqual(5.5, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_setter_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''
        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_year_setter_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886
        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_method_new_actor(self):
        self.movie.add_actor('Actor1')
        self.assertEqual(['Actor1'], self.movie.actors)

    def test_add_actor_method_existing_actor_error(self):
        self.movie.actors = self.actors
        result = self.movie.add_actor('Actor1')
        self.assertEqual("Actor1 is already added in the list of actors!", result)

    def test_overriding_gt_method_better(self):
        self.other_movie = Movie('Name2', 2000, 5)
        result = self.movie.__gt__(self.other_movie)
        self.assertEqual('"Name" is better than "Name2"', result)

    def test_overriding_gt_method_worse(self):
        self.other_movie = Movie('Name2', 2000, 6)
        result = self.movie.__gt__(self.other_movie)
        self.assertEqual('"Name2" is better than "Name"', result)

    def test_overriding_repr_method(self):
        self.movie.actors = self.actors
        self.assertEqual(
            "Name: Name\n"
            "Year of Release: 2000\n"
            "Rating: 5.50\n"
            "Cast: Actor1, Actor2"
        , self.movie.__repr__())


if __name__ == '__main__':
    unittest.main()