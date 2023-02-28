import unittest

import task


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_1(self):
        a = 'hello world1'
        d = {}
        for i in a:
            if i.isalpha():
                if i.lower() in d:
                    d[i.lower()] += 1
                else:
                    d[i.lower()] = 1

        self.assertEqual(task.task_1(a), d, msg="task_1")

    def test_2(self):
        a = [1, 4, 6, 7, 4, 8, 8]
        b = sum(set(a))

        self.assertEqual(task.task_2(a), b, msg="task_2")


    def test_3(self):
        cities = ['Moscow', 'Paris', 'Kiev', 'Minsk']

        str = ''
        for i in cities:
            str += i + ',' + ' '
        str =str[0:-2] + '.'


        self.assertEqual(task.task_3(cities), str, msg="task_3")

    def test_4(self):
        a = [1, 2, 3, 4, 5, 6, 7, 8]
        b = [6, 7, 8, 9, 0]

        c = list(set(a) & set(b))


        self.assertEqual(task.task_4(a,b), c, msg="task_4")