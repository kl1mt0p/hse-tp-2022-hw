#Построение графика зависимости времени выполнения функции поиска суммы чисел от размера входного файла

import matplotlib.pyplot as gr
import time
from functions import _sum, numbers

timecodes = []
value = []

for step in range(0, len(numbers), 5000):
    curr_list = numbers[0:1000+step]
    value.append(len(curr_list))
    start = time.time()
    _sum(curr_list)
    end = time.time()
    res = end - start
    timecodes.append(res)

gr.title('Соотношение времени выполнения к размеру файла', fontsize=12, fontweight='bold')
gr.xlabel('Размер файла, кол-во чисел')
gr.ylabel('Затраченное время, сек')
gr.plot(value, timecodes, linewidth=3)
gr.show()