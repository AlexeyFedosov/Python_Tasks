#Вычислить число π c заданной точностью d
#Пример: при d = 0.001,π = 3.141.10^(-1)≤d≤10^(-10)

import math

d = '0.00001'
d = int(len(d) -2)
pi = round(math.pi, d)
print(pi)

print(f'Число Пи {math.pi: .3f}')