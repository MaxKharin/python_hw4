# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141    10^{-1} ≤ d ≤10^{-10}

from math import pi

num = int(input('Enter a number of digits after the decimal point: '))
print(f'π = {round(pi, num)}')