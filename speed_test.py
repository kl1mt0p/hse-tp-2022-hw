#Тест для проверки скорости работы функций, содержащихся в файле functions.py

import unittest
import time
from functions import _min, _max, _mult, _sum, numbers

class SpeedTest(unittest.TestCase):

    def setUp(self):
        self.start_time = 0
        self.end_time = 0
        print('Тестирование...')

    def test_time_min(self):
        print('Функция поиска минимума:')
        self.start_time = time.time()
        _min(numbers)
        self.end_time = time.time()
    
    def test_time_max(self):
        print('Функция поиска максимума:')
        self.start_time = time.time()
        _max(numbers)
        self.end_time = time.time()
    
    def test_time_sum(self):
        print('Функция поиска суммы чисел:')
        self.start_time = time.time()
        _sum(numbers)
        self.end_time = time.time()
    
    def test_time_mult(self):
        print('Функция поиска произведения чисел:')
        self.start_time = time.time()
        _mult(numbers)
        self.end_time = time.time()

    def tearDown(self):
        print('Тест пройден')
        print(f'Время выполнения для файла длиной {len(numbers)} равно {(self.end_time-self.start_time)} секунд.')

unittest.main()