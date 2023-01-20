from unittest import TestCase, main

# from project.train.train import Train


class TrainTest(TestCase):
    def setUp(self) -> None:
        self.train = Train("ExpresTrain", 3)

    def test_correct_init(self):
        train = Train("TestName", 3)
        self.assertEqual("TestName", train.name)
        self.assertEqual(3, train.capacity)
        self.assertEqual([], train.passengers)

    def test_add_adds_passengers_and_return_proper_string(self):
        passenger_name = "Vladi"
        result = self.train.add(passenger_name)

        self.assertEqual(f"Added passenger {passenger_name}", result)
        self.assertTrue(passenger_name in self.train.passengers)
        self.assertEqual(1, len(self.train.passengers))

    def test_add_raises_when_capacity_is_reached(self):
        self.train.passengers = ["Vladi", "Alek", "Filip"]

        with self.assertRaises(ValueError) as ve:
            self.train.add("Desi")
        self.assertEqual("Train is full", str(ve.exception))

    def test_add_already_added_passenger(self):
        passenger_name = "Vladi"
        self.train.passengers = [passenger_name]

        with self.assertRaises(ValueError) as ve:
            self.train.add(passenger_name)
        self.assertEqual(f"Passenger {passenger_name} Exists", str(ve.exception))

    def test_remove_passengers(self):
        removed_passenger = "Filip"
        self.train.passengers = ["Vladi", "Alek", "Filip"]
        result = self.train.remove(removed_passenger)

        self.assertEqual(f"Removed {removed_passenger}", result)

    def test_remove_not_exist_passenger_raise(self):
        removed_passenger = "Desi"
        self.train.passengers = ["Vladi", "Alek", "Filip"]

        with self.assertRaises(ValueError) as ve:
            self.train.remove(removed_passenger)

        self.assertEqual("Passenger Not Found", str(ve.exception))


if __name__ == "__main__":
    main()