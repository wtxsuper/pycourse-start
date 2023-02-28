import unittest
import math
import task

class TestCase(unittest.TestCase):
    def test_first_task_1(self):
        a, b = 4, 3
        first = math.sqrt(a * b) - 3
        self.assertEqual(task.task_1(a, b), first)

    def test_second_task_1(self):
        a, b = 2, 2
        second = math.log10(2)
        self.assertEqual(task.task_1(a, b), second)

    def test_third_task_1(self):
        a, b = 3, 4
        third = math.log(a * a * a + 1) / b
        self.assertEqual(task.task_1(a, b), third)

# пример 2
    def test_first_task_2(self):
        a, b = 3, 4
        first = math.tan(a/b)+1
        self.assertEqual(task.task_2(a, b), first)

    def test_second_task_2(self):
        a, b = 2, 2
        second = math.tan(-1)
        self.assertEqual(task.task_2(a, b), second)

    def test_third_task_2(self):
        a, b = 4, 3
        third = math.sqrt(a*b-5)/a
        self.assertEqual(task.task_2(a, b), third)

# пример 3
    def test_first_task_3(self):
        a,b=4,3
        first = math.log10(a*b)+21
        self.assertEqual(task.task_3(a, b), first)

    def test_second_task_3(self):
        a, b = 2, 2
        second = math.tan(-5)
        self.assertEqual(task.task_3(a, b), second, msg="task_3")

    def test_third_task_3(self):
        a, b = 3, 4
        third = math.log(3*a/b)+1
        self.assertEqual(task.task_3(a, b), third)

# пример 4
    def test_first_task_4(self):
        a,b=4,3
        first = math.sqrt(a*b-1)
        self.assertEqual(task.task_4(a, b), first)

    def test_second_task_4(self):
        a, b = 2, 2
        second = math.log10(255)
        self.assertEqual(task.task_4(a, b), second)

    def test_third_task_4(self):
        a, b = 3, 4
        third = math.tan(a-5)/b
        self.assertEqual(task.task_4(a, b), third)

# пример 5
    def test_first_task_5(self):
        a,b=4,3
        first = math.log(a/b)+31
        self.assertEqual(task.task_5(a, b), first)

    def test_second_task_5(self):
        a, b = 2, 2
        second = math.tan(-25)
        self.assertEqual(task.task_5(a, b), second)

    def test_third_task_5(self):
        a, b = 3, 4
        third = math.cos(a*5-1)/a
        self.assertEqual(task.task_5(a, b), third)

# пример 6
    def test_first_task_6(self):
        a,b=3,4
        first = math.sqrt(b/a+1)
        self.assertEqual(task.task_6(a, b), first)

    def test_second_task_6(self):
        a, b = 2, 2
        second = math.sqrt(25)
        self.assertEqual(task.task_6(a, b), second)

    def test_third_task_6(self):
        a, b = 4, 3
        third = math.log10(a*a*a-5)/b
        self.assertEqual(task.task_6(a, b), third)

if __name__ == '__main__':
    unittest.main()