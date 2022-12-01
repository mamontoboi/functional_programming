﻿"""Приклад використання функції reduce"""

from functools import reduce
from operator import mul

numbers = [3, 2, 1, 8, -3, -2]
# Добуток усіх чисел списку
product = reduce(lambda x, y: x * y, numbers)

print(product)

