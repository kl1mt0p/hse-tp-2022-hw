#Тест корректности функций, содержащихся в файле functions.py

import unittest
from math import prod
from functions import _min, _max, _mult, _sum, numbers

class CorrectTest(unittest.TestCase):

    def setUp(self):
        print('Тестирование...')

    def test_min(self):
        self.assertEqual(_min(numbers), min(numbers))

    def test_max(self):
        self.assertEqual(_max(numbers), max(numbers))

    def test_sum(self):
        self.assertEqual(_sum(numbers), sum(numbers))

    def test_mult(self):
        self.assertEqual(_mult(numbers), prod(numbers))
    
    def tearDown(self):
        print('Тест пройден')


unittest.main()
    