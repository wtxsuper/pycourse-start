import unittest
import task


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_1(self):
        N = 5
        factorial = 1
        if N < 0:
            print("Для отрицательных чисел факториал не определен")
        elif N == 0:
            print("Факториал 0 равен 1")
        else:
            for i in range(1, N + 1):
                factorial = factorial * i
        self.assertEqual(task.task_1(N), factorial, msg="test1")

    def test_2(self):
        a = 0
        b = 1
        N = 7
        for i in range(3, N + 1):
            c = a + b
            a = b
            b = c

        self.assertEqual(task.task_2(N), b, msg="test2")

    def test_3(self):
        N = 100
        lst = [1, N]
        for i in range(2, 1 + int(N ** 0.5)):
            if N % i == 0:
                lst.extend({N // i, i})

        self.assertEqual(task.task_3(N), sorted(lst), msg="test3")
