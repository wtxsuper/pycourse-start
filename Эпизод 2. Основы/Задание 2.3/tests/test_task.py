import unittest

import task


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_1(self):
        string = "Придет осень, за все спросит"
        result_list = []
        for i in string.split(' '):
            if i != '':
                result_list.append(i)
        ans = len(result_list[-1])
        self.assertEqual(task.task_1(string), ans, msg="test1")

    def test_2(self):
        string = "Без труда не вытащить рыбку из пруда"
        result_list = []
        for i in string.split(' '):
            if i != '':
                result_list.append(i)
        for i in range(0, len(result_list) - 1, 2):
            result_list[i], result_list[i + 1] = result_list[i + 1], result_list[i]
        ans = ' '.join(result_list)
        print(ans)
        self.assertEqual(task.task_2(string),ans, msg="Task 2 Test 1")

    def test_3(self):
        string = "Этот текст для задания на алгоритмы"
        tmp_list = []
        count = 0
        for i in string.split(' '):
            if i != ' ':
                tmp_list.append(i)
        for i in range(0, len(tmp_list) - 1):
            if tmp_list[i][-1] == tmp_list[i + 1][0]:
                count += 1
        self.assertEqual(task.task_3(string),count, msg="Task 3 Test 1")


