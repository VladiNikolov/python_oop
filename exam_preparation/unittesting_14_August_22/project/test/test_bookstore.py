from unittest import TestCase, main

from project.bookstore import Bookstore

from exam_preparation.unittesting_14_August_22.project.bookstore import Bookstore



class TestBookstore(TestCase):

    def setUp(self):
        self.store = Bookstore(15)
        self.books = {
            "Java for dummies": 10,
            "C++ Bible": 3,
        }

    def test_correct_initializing(self):
        self.assertEqual(15, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store.total_sold_books)

    def test_invalid_book_limit_set_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = 0

        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

    def test_correct__len__method(self):
        self.store.availability_in_store_by_book_titles = self.books
        self.assertEqual(13, len(self.store))

    def test_not_enough_space_to_receive_book_raises_exception(self):
        self.store.availability_in_store_by_book_titles = self.books

        with self.assertRaises(Exception) as ex:
            self.store.receive_book("Python Advanced", 3)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_add_new_book_correct(self):
        result = self.store.receive_book("Python Advanced", 2)

        self.assertEqual("2 copies of Python Advanced are available in the bookstore.", result)
        self.assertEqual({"Python Advanced":  2}, self.store.availability_in_store_by_book_titles)

    def test_add_existing_book_correct(self):
        self.store.availability_in_store_by_book_titles = self.books

        result = self.store.receive_book("C++ Bible", 1)

        self.assertEqual("4 copies of C++ Bible are available in the bookstore.", result)

    def test_sell_book_that_does_not_exist_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.sell_book("Python Advanced", 2)

        self.assertEqual("Book Python Advanced doesn't exist!", str(ex.exception))

    def test_sell_more_copies_then_available_raises_exception(self):
        self.store.availability_in_store_by_book_titles = self.books

        with self.assertRaises(Exception) as ex:
            self.store.sell_book("Java for dummies", 11)

        self.assertEqual("Java for dummies has not enough copies to sell. Left: 10", str(ex.exception))

    def test_successfully_selling_a_book(self):
        self.store.availability_in_store_by_book_titles = self.books

        result = self.store.sell_book("C++ Bible", 3)

        self.assertEqual("Sold 3 copies of C++ Bible", result)
        self.assertEqual(3, self.store.total_sold_books)
        self.assertEqual({
            "Java for dummies": 10,
            "C++ Bible": 0,
        }, self.store.availability_in_store_by_book_titles)

    def test_correct__str__method(self):
        self.store.availability_in_store_by_book_titles = self.books

        self.assertEqual(
            "Total sold books: 0\n"
            "Current availability: 13\n"
            " - Java for dummies: 10 copies\n"
            " - C++ Bible: 3 copies",
            str(self.store)
        )

if __name__ == '__main__':
    main()
