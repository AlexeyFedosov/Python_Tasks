# Найти корни квадратного уравнения Ax² + Bx + C = 0
#     - Математикой
#     - Используя дополнительные библиотеки*



import math 

def korni(a, b, c):
    x1 = 0
    x2 = 0
    d = b ** 2 - 4 * a * c
    if d < 0: 
        return None, None
    elif d == 0:
        x1 = (-1 * b) / 2 * a
        x2 = x1
        return x1, x2
    else:
        x1 = (-1 * b + math.sqrt(d)) / (2 * a)
        x2 = (-1 * b - math.sqrt(d)) / (2 * a)
        return x1, x2
    
my_a_b_c = [int(x) for x in input('введите a b c через пробел: ').split()]

a, b, c = my_a_b_c

print(korni(a, b, c))