#Функции для поиска минимума/максимума, суммы и произведения числе в исходном файле

from cmath import inf

name = input()
with open(f'{name}', 'r') as file:
    numbers = [int(val) for val in file.readline().split()]


def _min(mas):
    if len(mas) == 0:
        return 'Пустой файл'
    minn = inf
    for val in mas:
        if val < minn:
            minn = val
    return minn

def _max(mas):
    if len(mas) == 0:
        return 0
    maxx = -inf
    for val in mas:
        if val > maxx:
            maxx = val
    return maxx

def _sum(mas):
    if len(mas) == 0:
        return 'Пустой файл'
    summ = 0
    for val in mas:
        summ += val
    return summ

def _mult(mas):
    if len(mas) == 0:
        return 'Пустой файл'
    if 0 in mas:
        return 0
    mult = 1
    for val in mas:
        mult *= val
    return mult
