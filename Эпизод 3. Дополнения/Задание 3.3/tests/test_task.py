import unittest
import task


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_1(self):
        lis = [1, 2, 3, 44, 5, 5, 5, 7, 8, 8, 8, 8, 9, 10]
        max = lis[0]
        max_count = lis.count(max)
        for n in lis:
            if lis.count(n) > max_count:
                max = n
            max_count = lis.count(n)
        self.assertEqual(task.task_1(lis), max, msg="task_1")

    def test_2(self):
        x = [1, 6, 4, 2, 8, 5, 4, 2]
        y = [6, 3, 2, 4, 5, 3, 6, 1]

        correct = True
        for i in range(8):
            for j in range(i + 1, 8):
                if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                    correct = False

            if correct:
                flag = 'NO'
            else:
                flag = 'YES'
        self.assertEqual(task.task_2(x, y), flag, msg="task_2")

    def test_3(self):
        x = 4
        y = 5
        xc = 7
        yc = 1
        r = 2
        in_circle = (x - xc) * (x - xc) + (y - yc) * (y - yc) <= r * r
        self.assertEqual(task.task_3(x, y, xc, yc, r), in_circle, msg="task_3")

    def test_4(self):
        counter = 0
        lis = [1, 3, 5, 2, 7, 3, 9, 4, 6, 3, 7]
        for i in range(1, len(lis) - 1):
            if lis[i - 1] < lis[i] > lis[i + 1]:
                counter += 1
        self.assertEqual(task.task_4(lis), counter, msg="task_4")

    def test_5(self):
        alpha = ' abcdefghijklmnopqrstuvwxyz'
        key = 2
        itog = ''
        b = []
        with open('file.txt', 'r') as f:
            for line in f:
                line = line.lower().strip()
                for i in line:
                    mesto = alpha.find(i)

                    new_m = mesto + key

                    itog += alpha[new_m]
                b.append(itog)
                itog = ''

        self.assertEqual(task.task_5(key), b, msg="task_5")
