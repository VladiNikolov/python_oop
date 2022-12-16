from unittest import TestCase, main

# from python_oop.testing_lab.cat import Cat


class CatTest(TestCase):

    def test_correct_init(self):
        cat = Cat("TestName")
        self.assertEqual("TestName", cat.name)
        self.assertFalse(cat.fed)
        self.assertFalse(cat.sleepy)
        self.assertEqual(0, cat.size)

    def test_correct_cat_size_increase_after_eating(self):
        cat = Cat("TestName")

        cat.eat()
        self.assertEqual(1, cat.size)

    def test_cat_is_fed_after_eating(self):
        cat = Cat("TestName")

        cat.eat()
        self.assertTrue(cat.fed)

    def test_cat_is_sleepy_after_eating(self):
        cat = Cat("TestName")

        cat.eat()
        self.assertTrue(cat.sleepy)

    def test_cat_is_fed_and_eating_again_raise(self):
        cat = Cat("TestName")
        cat.fed = True

        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_no_sleep_if_no_fed_raises(self):
        cat = Cat("TestName")

        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_is_not_sleepy_after_sleeping(self):
        cat = Cat("TestName")
        cat.fed = True
        cat.sleepy = True

        cat.sleep()
        self.assertFalse(cat.sleepy)
#       self.assertEqual(False, cat.sleepy)


if __name__ == "__main__":
    main()