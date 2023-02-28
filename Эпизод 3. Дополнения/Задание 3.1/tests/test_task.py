import math
import unittest

import task


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_1(self):
        text = 'First sent. Second sent and. Third sent and other.'



        mas = text.rstrip('.').split('.')

        d = {sent.strip(): len(sent.strip().split(' ')) for sent in mas}


        self.assertEqual(task.task_1(text), d, msg="task_1")


    def test_2(self):
        x1,y1,x2,y2 = 2,5,4,9


        self.assertEqual(task.task_2(x1,y1,x2,y2), math.sqrt((x1-x2)**2 + (y1-y2)**2), msg="task_2")
