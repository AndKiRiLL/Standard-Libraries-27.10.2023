import numpy as np

# Задание 1
'''
def ListToNumpy(list):
    list = np.array(list, dtype = float)
    return list

a = [[1, 2 ,3], [4, 5, 6]]

print(ListToNumpy(a))
'''

# Задание 2
'''
def ShapeSizeCalc(arr):

    shape = np.shape(arr)
    size = np.size(arr)

    return f"Ответ: shape = {shape}, size = {size}"

array = np.array([[1, 2, 3], [4, 5, 6]])

print(ShapeSizeCalc(array))
'''

# Задание 3
'''
#НЕДОДЕЛАНО
def ArrayIndexing(arr=[], rows=0, val=0):
    for i in len(arr):
        arr.append(arr[i])
        arr_new = np.array(arr)
    return

array_ = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
rows_ = (0, 1)
val_ = 2

print(ArrayIndexing(array_, rows_, val_))
'''

import matplotlib.pyplot as plt

# 1. Нарисуйте график линейной функции: y = 6x – 2
'''
x = np.linspace(0, 10, 50)
y = 6 * x - 2

plt.title('Зависимость: y = 6x - 2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.plot(x,y)
plt.show()
'''


# 3. Постройте столбчатую диаграмму для данных:
'''
item = ['tomatoes', 'cucumbers', 'pumpkin', 'beet', 'radish', 'potato']
counts = [100, 65, 12, 47, 89, 256]

plt.bar(item, counts)
plt.title('Vegetables')
plt.ylabel('Counts')
plt.show()
'''

# Задание 1
# Стандартная библиотека. Модуль calendar.
'''
import calendar

print(calendar.isleap(2027))
print(calendar.weekday(1995, 6, 25))
print(calendar.calendar(2023))
'''

# Задание 2
# Репозиторий PyPI. Пакет FuzzyWuzzy.
'''
from fuzzywuzzy import fuzz

print(fuzz.ratio('Плохой код на самом деле не плохой.', 'Его просто не так поняли.'))
print(fuzz.ratio('Работает? Не трогай.', 'Работает? Не трогай.'))
print(fuzz.ratio('Работает? Не трогай.', 'Работает? Не трогай!'))
'''