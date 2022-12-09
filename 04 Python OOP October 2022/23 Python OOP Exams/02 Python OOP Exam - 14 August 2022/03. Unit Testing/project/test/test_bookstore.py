from project.bookstore import Bookstore


import unittest


class TestBookstore(unittest.TestCase):
    def setUp(self):
        self.store = Bookstore(15)
        self.books = {'Book1': 10, 'Book2': 3}

    def test_init_method(self):
        self.assertEqual(15, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store.total_sold_books)

    def test_books_limit_setter_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = 0

        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

    def test_overriding_len_method(self):
        self.store.availability_in_store_by_book_titles = self.books
        self.assertEqual(13, len(self.store))

    def test_receive_book_method_book_limit_exception(self):
        self.store.availability_in_store_by_book_titles = self.books

        with self.assertRaises(Exception) as ee:
            self.store.receive_book('Book3', 3)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ee.exception))

    def test_receive_book_method_new_book_success(self):
        result = self.store.receive_book('Book3', 2)

        self.assertEqual("2 copies of Book3 are available in the bookstore.", result)
        self.assertEqual({'Book3': 2}, self.store.availability_in_store_by_book_titles)

    def test_receive_book_method_existing_book_success(self):
        self.store.availability_in_store_by_book_titles = self.books

        result = self.store.receive_book('Book2', 1)

        self.assertEqual("4 copies of Book2 are available in the bookstore.", result)

    def test_sell_book_method_book_title_exception(self):
        with self.assertRaises(Exception) as ee:
            self.store.sell_book('Book3', 2)

        self.assertEqual("Book Book3 doesn't exist!", str(ee.exception))

    def test_sell_book_method_not_enough_exception(self):
        self.store.availability_in_store_by_book_titles = self.books

        with self.assertRaises(Exception) as ee:
            self.store.sell_book('Book1', 11)

        self.assertEqual("Book1 has not enough copies to sell. Left: 10", str(ee.exception))

    def test_sell_book_method_success(self):
        self.store.availability_in_store_by_book_titles = self.books

        result = self.store.sell_book('Book2', 3)

        self.assertEqual("Sold 3 copies of Book2", result)
        self.assertEqual(3, self.store.total_sold_books)
        self.assertEqual({'Book1': 10, 'Book2': 0}, self.store.availability_in_store_by_book_titles)

    def test_overriding_str_method(self):
        self.store.availability_in_store_by_book_titles = self.books

        self.assertEqual(
            "Total sold books: 0\n"
            "Current availability: 13\n"
            " - Book1: 10 copies\n"
            " - Book2: 3 copies",
            str(self.store)
        )


if __name__ == '__main__':
    unittest.main()