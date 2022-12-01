﻿"""Приклад використання модуля operator"""

from operator import neg, mul, le  # larger or equal
from functools import reduce, partial

# Зробити числа списку негативними
print(list(map(neg, [2, 4, 8, 9, 1])))

# Обчислити добуток елементів списку
print(reduce(mul, [3, 4, 5]))

# Залишити лише числа, великі або рівні п'яти (використовується оператор <=, так як за допомогою функції
# partial застосовується перший аргумент, тобто умова виглядає як 5 <= x).
print(list(filter(partial(le, 5), [5, 4, 8, 1, 3, 6, 4, 5, 10])))