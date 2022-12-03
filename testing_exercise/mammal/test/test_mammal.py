from unittest import TestCase, main
from testing_exercise.mammal.project.mammal import Mammal
# from project.mammal import Mammal - whit this import submit in judge


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("TestName", "MammalType", "Krqk")

    def test_correct_initializing(self):
        self.assertEqual("TestName", self.mammal.name)
        self.assertEqual("MammalType", self.mammal.type)
        self.assertEqual("Krqk", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    # def test_correct_make_sound(self):
    #     self.assertEqual("TestName makes Krqk", self.mammal.make_sound())

    def test_correct_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual("TestName makes Krqk", result)


    # def test_get_kingdom(self):
    #     self.assertEqual("animals", self.mammal.get_kingdom())

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)


    # def test_correct_info(self):
    #     self.assertEqual("TestName is of type MammalType", self.mammal.info())

    def test_correct_info(self):
        result = self.mammal.info()
        self.assertEqual("TestName is of type MammalType", result)

if __name__ == '__main__':
    main()