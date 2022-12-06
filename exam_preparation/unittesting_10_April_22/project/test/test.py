
from unittest import TestCase, main

from project.movie import Movie


class TestMovie(TestCase):
    def setUp(self) -> None:
        self.movie = Movie("Rocky", 1990, 10)

    def test_correct_init(self):
        self.assertEqual("Rocky", self.movie.name)
        self.assertEqual(1990, self.movie.year)
        self.assertEqual(10, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_setter_raises_error_with_empty_string(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''

        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_year_setter_raises_error_wear_less_then(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1883

        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_append_name_when_does_not_exist(self):
        first = "Vladi"
        second = "Desi"
        self.movie.add_actor(first)
        self.movie.add_actor(second)

        self.assertEqual([first, second], self.movie.actors)

    def test_add_actor_return_error_message_with_duplicate_name(self):
        name = "Vladi"
        self.movie.actors = [name]

        result = self.movie.add_actor(name)
        self.assertEqual(f"{name} is already added in the list of actors!", result)
        self.assertEqual([name], self.movie.actors)

    def test_gt_returns_true_when_first_movie_has_greater_rating(self):
        another_movie_name = "The Matrix"
        another_movie = Movie(another_movie_name, 2004, 8)

        first_result = self.movie > another_movie
        second_result = another_movie > self.movie
        self.assertEqual(f'"{self.movie.name}" is better than "{another_movie_name}"', first_result)
        self.assertEqual(f'"{self.movie.name}" is better than "{another_movie_name}"', second_result)

    def test_repr_returns_proper_string(self):
        actors = ["Pesho", "Gosho"]
        self.movie.actors = actors

        actual_result = repr(self.movie)
        expected_result = f"Name: {self.movie.name}\n" \
               f"Year of Release: {self.movie.year}\n" \
               f"Rating: {self.movie.rating:.2f}\n" \
               f"Cast: {', '.join(actors)}"

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()
