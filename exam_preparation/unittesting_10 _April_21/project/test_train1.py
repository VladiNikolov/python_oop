from unittest import TestCase, main

from project.train.train import Train


class TestTrain(TestCase):

    def test_correct_init(self):
        train = Train('TrainName', 4)
        self.assertEqual("TrainName", train.name)
        self.assertEqual(4, train.capacity)
        self.assertEqual([], train.passengers)

    def test_correct_add_new_passenger(self):
        train = Train('TrainName', 4)
        added_passenger = "Vladi"
        result = train.add(added_passenger)
        self.assertEqual(f"Added passenger {added_passenger}", result)

    def test_add_passenger_when_train_is_full_raise(self):
        train = Train('TrainName', 4)
        train.passengers = ["Vladi", "Desi", "Alek", "Filip"]

        with self.assertRaises(ValueError) as ve:
            train.add("Pesho")
        self.assertEqual("Train is full", str(ve.exception))

    def test_add_already_exist_passenger_raise(self):
        train = Train('TrainName', 4)
        train.passengers = ["Vladi", "Desi"]

        with self.assertRaises(ValueError) as ve:
            train.add("Vladi")
        self.assertEqual(f"Passenger Vladi Exists", str(ve.exception))

    def test_correct_removed_passenger(self):
        train = Train('TrainName', 4)
        train.passengers = ["Vladi", "Desi"]
        removed_passenger = "Vladi"
        result = train.remove(removed_passenger)
        self.assertEqual(f"Removed {removed_passenger}", result)

    def test_remove_passenger_if_not_in_passenger_list_raise(self):
        train = Train('TrainName', 4)
        train.passengers = ["Vladi", "Desi", "Alek", "Filip"]
        removed_not_exist_name = "Gosho"

        with self.assertRaises(ValueError) as ve:
            train.remove(removed_not_exist_name)
        self.assertEqual("Passenger Not Found", str(ve.exception))






