from unittest import TestCase, main
# from testing_lab.car_manager import Car


class TestCar(TestCase):

    def setUp(self):
        self.car = Car("Moskvich", "Aleko", 20, 65)

    def test_correct_initializing(self):
        self.assertEqual("Moskvich", self.car.make)
        self.assertEqual("Aleko", self.car.model)
        self.assertEqual(20, self.car.fuel_consumption)
        self.assertEqual(65, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_no_make_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_no_model_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_zero_fuel_consumption_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_zero_fuel_capacity_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_negative_fuel_amount_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_negative_refuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_more_than_capacity(self):
        self.car.refuel(self.car.fuel_capacity + 10)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_drive_more_than_possible_raise_exception(self):
        self.car.fuel_amount = 20

        with self.assertRaises(Exception) as ex:
            self.car.drive(1000)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_valid_distance_expect_fuel_amount_reduce(self):
        self.car.fuel_amount = 65
        self.car.drive(100)

        self.assertEqual(self.car.fuel_amount, 45)


if __name__ == '__main__':
    main()

