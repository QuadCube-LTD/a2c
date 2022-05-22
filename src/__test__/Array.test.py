import unittest

import os 
import sys
sys.path.append(os.path.abspath("../"))

from Array import Array

class Arrayのテスト(unittest.TestCase):

    def test_組込みlistの継承である(self):
        received = Array(1,2,3)
        self.assertEqual(isinstance(received, list), True)


    def test_各要素に対して操作(self):
        received = Array(1,2,3).map_(lambda x: x+1)
        expected = Array(2,3,4)
        self.assertEqual(received, expected)


    def test_全ての要素を区切り文字で結合(self):
        received = Array(1,2,3).join_(sep="-")
        expected = "1-2-3"
        self.assertEqual(received, expected)


if __name__ == '__main__':
    unittest.main()
