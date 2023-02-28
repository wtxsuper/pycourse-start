import unittest
import math
import task


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_1(self):
        n = 10
        x = 0
        for i in range(1, n + 1):
            x += 1 / i
        self.assertEqual(task.task_1(n), x)

    def test_2(self):
        n = 17
        x = 0
        y = 1
        for i in range(1,n+1,2):
            x += y/i
        self.assertEqual(task.task_2(1,n), x)


    def test_3(self):
        n = 10
        x = math.factorial(n)
        self.assertEqual(task.task_3(n),x)

    def test_4(self):
        n = 9
        x = 1
        y = 1
        for i in range(2,n+1):
            x *= (y+i)/i
        self.assertEqual(task.task_4(1,n), x)

    def test_5(self):
        n = 3
        x = 0
        y = 1
        for i in range(1,n+1):
            x += (y*i)/(2*i)
        self.assertEqual(task.task_5(1,n), x)

    def test_6(self):
        def f(num):
            z = 1
            for i in range(2, num + 2, 2):
                z *= i
            return z

        n = 20
        self.assertEqual(task.task_6(n), f(n))
