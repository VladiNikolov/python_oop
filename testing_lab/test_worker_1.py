from unittest import TestCase, main

from python_oop.testing_lab.worker import Worker


class WorkerTest(TestCase):

    def test_correct_init(self):
        worker = Worker("TestName", 200, 100)
        self.assertEqual("TestName", worker.name)
        self.assertEqual(200, worker.salary)
        self.assertEqual(100, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_work_with_equal_energy_raises(self):
        worker = Worker("TestName", 200, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_work_with_negative_energy_raises(self):
        worker = Worker("TestName", 200, -10)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_workers_correct_increase_salary(self):
        worker = Worker("TestName", 200, 100)

        worker.work()
        self.assertEqual(200, worker.money)

        worker.work()
        self.assertEqual(400, worker.money)

    def test_workers_correct_decrease_energy_with_work_method(self):
        worker = Worker("TestName", 200, 100)

        worker.work()
        self.assertEqual(99, worker.energy)

    def test_workers_correct_increase_energy_with_rest_method(self):
        worker = Worker("TestName", 200, 100)

        worker.rest()
        self.assertEqual(101, worker.energy)

    def test_correct_get_info(self):
        worker = Worker("TestName", 200, 100)

        result = worker.get_info()
        self.assertEqual("TestName has saved 0 money.", result)

if __name__ == "__main__":
    main()
