import unittest

import os 
import sys
sys.path.append(os.path.abspath(".."))

import utils

class Utilのテスト(unittest.TestCase):

    def test_小数第n位で四捨五入(self):
        received = utils.ceil(x = 0.1234567890, digit = 3)
        expected = 0.123
        self.assertEqual(received, expected)


    def test_リストの平均(self):
        received = utils.average([1, 2.0, 3.3])
        expected = 2.1
        self.assertEqual(received, expected)


    def test_転置行列を求める(self):
        received = utils.T([
            [0,1,2],
            [3,4,5]
            ])
        expected = [
            [0,3],
            [1,4],
            [2,5]
            ]
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
