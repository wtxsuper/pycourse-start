import unittest
import math
import task


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_1(self):

        a = [4, 6, 11, 3, 9, 6, 5, 7, 4, 2]
        a.sort()
        print(a)


        value = 6
        id = ''
        mid = len(a) // 2
        low = 0
        high = len(a) - 1

        while a[mid] != value and low <= high:
            if value > a[mid]:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2

        if low > high:
            id = "No value"
        else:
            id = str(mid)

        self.assertEqual(task.task_1(a, value), id, msg="task_1")

    def test_2(self):
        n = 3
        flag = True
        if n < 2:
            flag = False
        if n == 2:
            flag = True
        limit = math.sqrt(n)
        i = 2
        while i <= limit:
            if n % i == 0:
                flag = False
            i += 1

        self.assertEqual(task.task_2(n), flag, msg="task_2")
