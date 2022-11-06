# Тест на считывание данных из файла (проверяем, считалось ли хоть что-то)

import unittest
from functions import numbers


class EmptyTest(unittest.TestCase):

    def setUp(self):
        print('Тестирование...')

    def test_numbers(self):
        self.assertNotEqual(len(numbers), 0, 'Пустой файл')

    def tearDown(self):
        print('Тест пройден')


unittest.main()
