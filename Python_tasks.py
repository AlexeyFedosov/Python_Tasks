## Вывести квадрат числа
import random
num = random.randint(1,1000)
print(f'квадрат {num} = {num**2}')

## По двум заданным числам проверять является ли первое квадратом второго
def Task_1(x,y):
    return x == y**2

a = int(input('a = '))
b = int(input('b = '))
print(Task_1(a, b))

## Даны два числа. Показать большее и меньшее число

num = int(input())
num2 = int(input())

if num > num2:
    print(f'{num} больше {num2}')
elif num == num2:
    print(f'{num} равно {num2}')
else:
    print(f'{num2} больше {num}')

## По заданному номеру дня недели вывести его название
days = {1: 'понедельник', 
        2: 'вторник',
        3: 'среда',
        4: 'четверг',
        5: 'пятница',
        6: 'суббота',
        7: 'воскресенье'}

my_day = int(input('Введите номер дня недели '))

if my_day in days:
    print(days[my_day])

## Найти максимальное из трех чисел
import random
num = random.randint(1,9999)
num2 = random.randint(1,9999)
num3 = random.randint(1,9999)

num4 = max(num, num2, num3)
print(f'{num4} это бОльшее из чисел {num}, {num2} и {num3}')

##Написать программу вычисления значения функции y = f(a)
import math
def find_cosinus(x):
    return f'cos{x} = {math.cos(x)}'

d = int(input('число = '))
print(find_cosinus(d))

## Выяснить является ли число чётным
from cProfile import run
import random
num = random.randint(1,99)

if num % 2 == 0:
    print(f'число {num} является четным')
else:
    print(f'число {num} не является четным')

## Показать числа от -N до N
import random
num = random.randint(1,10)
for i in range(-num, num+1):
    print(i)

##Показать четные числа от 1 до N
import random
num = random.randint(1, 20)

for i in range(2, num, 2):
    print(i)

## Показать последнюю цифру трёхзначного числа
import random

num = random.randint(100,999)

print(f'{num} {num%10}')

## Показать вторую цифру трёхзначного числа
import random

num = random.randint(100,999)
second_num = (num%100)//10

print(f'{num} {second_num}')

## Удалить вторую цифру трёхзначного числа
import random
num = random.randint(100, 999)
new_num = (num//100) * 10 + num % 10

print(num, new_num)

## Выяснить, кратно ли число заданному, если нет, вывести остаток.
def kratno_or_not(x, y):
    if x%y ==0: return f'Число {x} кратно числу {y}'
    else: return x%y

j = -9
k = int(input('Введите число = '))
print(kratno_or_not(j, k))

## Найти третью цифру числа или сообщить, что её нет
import random
num = random.randint(1,999)

third_num = (num % 1000)//100

if num > 99:
    print(third_num)
else:
    print('третьей цифры нет')

print(num)

## Дано число. Проверить кратно ли оно 7 и 23
g = 161

if g%7==0 and g%23 ==0:
    print(f'число {g} кратно 7 и 23')
else:
    print(f'число {g} некратно 7 и 23')

    ## Дано число обозначающее день недели. Выяснить является номер дня недели выходным

days = {1: 'понедельник', 
        2: 'вторник',
        3: 'среда',
        4: 'четверг',
        5: 'пятница',
        6: 'суббота',
        7: 'воскресенье'}

my_day = int(input('Введите номер дня недели '))

if my_day in range(6,7):
    print(f'{days[my_day]} явлется выходным') 
else:
    print(f'{days[my_day]} не явлется выходным')

    # По двум заданным числам проверять является ли одно квадратом другого

num1 = int(input('введите первое число '))
num2 = int(input('введите второе число '))

if num1 ** 0.5 == num2:
    print(f'{num1} является квадратом {num2}')
elif num2 ** 0.5 == num1:
    print(f'{num2} является квадратом {num1}')
else:
    print('ни одно из чисел не является квадратом второго')

    # # Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y

from xmlrpc.client import boolean


def TrueFalse(x, y):
    FlagX = bool(x != 0)
    FlagY = bool(y != 0)
    left = not(FlagX or FlagY)
    right = not FlagX and not FlagY
    return left == right

for i in range(0,2):
    for j in range(0,2):
        if TrueFalse(i, j):
            print(f'При x = {i} и y = {j} выражение ¬(X ⋁ Y) = ¬X ⋀ ¬Y истинно')
        else:
            print(f'При x = {i} и y = {j} выражение ¬(X ⋁ Y) = ¬X ⋀ ¬Y ложно')
        j += 1
    i += 1

## Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0

x = int(input('введите х не равный нулю '))
y = int(input('введите y не равный нулю '))

if x > 0 and y > 0:
    print('точка находится в 1 четверти')
elif x < 0 and y > 0:
    print('точка находится во 2 четверти')
elif x < 0 and y < 0:
    print('точка находится в 3 четверти')
elif x > 0 and y < 0:
    print('точка находится в 4 четверти')

## Задать номер четверти, показать диапазоны для возможных координат

diapason = {1: 'x > 0, y > 0',
            2: 'x < 0, y > 0',
            3: 'x < 0, y < 0',
            4: 'x >0, y < 0'}

num = int(input('введите номер четверти '))

if num in diapason:
    print(diapason[num])

## Программа проверяет пятизначное число на палиндромом.
num = int(input('введите пятизначное число '))

def palindrom(x):
    if x % 10 == x // 10000 and (x % 100)//10 == (x // 1000) % 10:
        return True

if palindrom(num):
    print(f'{num} является палиндромом')
else:
     print(f'{num} не является палиндромом')

## Найти расстояние между точками в пространстве 2D

xa = int(input('Введите координату X для точки A: '))
ya = int(input('Введите координату Y для точки A: '))
xb = int(input('Введите координату X для точки B: '))
yb = int(input('Введите координату Y для точки B: '))

distanceAB = round(((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5, 4)
print(f'Расстояние между точками A и B равно {distanceAB}')

## Найти расстояние между точками в пространстве 3D

xa = int(input('Введите координату X для точки A: '))
ya = int(input('Введите координату Y для точки A: '))
za = int(input('Введите координату Z для точки A: '))
xb = int(input('Введите координату X для точки B: '))
yb = int(input('Введите координату Y для точки B: '))
zb = int(input('Введите координату Z для точки A: '))

distanceAB = round(((xa - xb) ** 2 + (ya - yb) ** 2 + (za - zb) ** 2) ** 0.5, 4)
print(f'Расстояние между точками A и B равно {distanceAB}') 

## Показать таблицу квадратов чисел от 1 до N

import random
num = random.randint(1, 99)
for i in range(1, num):
    print(f'{i} ^ 2 = {i ** 2}')

## Найти кубы чисел от 1 до N

import random
num = random.randint(1, 99)
for i in range(1, num):
    print(f'{i} ^ 3 = {i ** 3}')

## Найти сумму чисел от 1 до А

import random
num = random.randint(1, 99)
sum = 0

for i in range(1, num):
    sum += i

print(num, sum)

## Возведите число А в натуральную степень B используя цикл

number_a = int(input('введите число А: '))
number_b = int(input('введите целую степень числа А: '))
result = 1
for i in range(1, number_b + 1):
    result *= number_a

print(result)

## Определить количество цифр в числе

num = int(input('введите число: '))

count = 0

while num != 0:
    num //= 10
    count += 1

print(count)

## Подсчитать сумму цифр в числе

import random
num = random.randint(300, 9999)
print(num)
result = 0

while num != 0:
    result += num % 10
    num //= 10

print(result)

## Написать программу вычисления произведения чисел от 1 до N

import random
num = random.randint(1, 300)
result = 1

for i in range(1, num + 1):
    result *= i

print(num, result)

## Показать кубы чисел, заканчивающихся на четную цифру

number = 999

for i in range(2, round(number ** (1/3)) + 1, 2):
    print(f'{i ** 3} = {i} ^ 3')

## Задать массив из 8 элементов и вывести их на экран

import random
array = []
for i in range(1, 9):
    array.append(random.randint(1, 999))

print(array)

## Задать массив из 8 элементов, заполненных нулями и единицами вывести их на экран
import random
array = []
for i in range(1, 9):
    array.append(random.randint(0, 1))

print(array)

## Задать массив из 12 элементов, заполненных числами из [0,9]. Найти сумму положительных/отрицательных элементов массива

import random
array = []
for i in range(1, 13):
    array.append(random.randint(-9, 9))

result_min = 0
result_plus = 0
for i in array:
    if i < 0:
        result_min += i
    else:
        result_plus += i
print(array, result_plus, result_min)