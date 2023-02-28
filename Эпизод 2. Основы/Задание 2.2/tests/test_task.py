import unittest
import random
import task
import math


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_1(self):
        N = 3
        a = []
        for i in range(N):
            a.append(random.randint(-10, 10))
        s = 0
        for i in range(N):
            if a[i] > 0:
                s += a[i]
        self.assertEqual(task.task_1(a), s, msg="Test1")

    def test_2(self):
        N = 10
        a = []
        for i in range(N):
            a.append(random.randint(1, 10))
        avg = sum(a)/len(a)
        self.assertEqual(task.task_2(a),avg, msg="Task 2 Test 1")

    def test_3(self):
        N = 10
        a = []
        for i in range(N):
            a.append(random.randint(0, 10))
        dispersion = 0
        avg = sum(a) / N
        for i in a:
            dispersion += (i - avg) ** 2
        dispersion = math.sqrt(dispersion / N)
        self.assertEqual(task.task_3(a),dispersion, msg="Task 3 Test 1")
