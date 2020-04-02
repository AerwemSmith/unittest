import unittest
from SoftWare import MaxSquence as M


class MyTest(unittest.TestCase):

    def test_Max1(self):
        n = 5
        arr = [-1, -2, -3, -4, -5]
        self.assertEqual(M.MaxSquence(n, arr), 0)

    def test_Max2(self):
        n = 6
        arr = [-2, 11, -4, 13, -5, -2]
        self.assertEqual(M.MaxSquence(n, arr), 20)

    def test_Max3(self):
        n = 7
        arr = [10, 9, 7, 6, 5, 8, 12]
        self.assertEqual(M.MaxSquence(n, arr), 57)


