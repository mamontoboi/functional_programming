﻿"""Приклад використання функції map"""
import operator

string = '2 4 8 15 42'
numbers = map(int, string.split())
print(list(numbers))
print(type(numbers))
