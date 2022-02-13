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

## Написать программу замену элементов массива на противоположные
import random
array = []

for i in range(1, 13):
    array.append(random.randint(-9, 9))
    
print(array)   

for i in range(0, len(array)):
    if array[i] < 0:
        array[i] = abs(array[i])
    else:
        array[i] = array[i] * -1
        
print(array)

## Определить, присутствует ли в заданном массиве, некоторое число

import random
array = []
for i in range(1, 9):
    array.append(random.randint(1, 10))
print(array)   
num = int(input('введите число которое будем искать: '))


if num in array:
    print(f'да, оно есть на позиции {array.index(num) + 1}. всего в списке это число встречается {array.count(num)} раз(а)')
else:
    print('такого числа нет')

## Задать массив, заполнить случайными положительными трёхзначными числами. Показать количество нечетных\четных чисел

import random
array = []
count_even = 0

for i in range(1, 9):
    array.append(random.randint(100, 999))
print(array)  

for i in array:
    if i % 2 == 0:
        count_even += 1
        
print(f'четных чисел {count_even}, а нечетных {len(array) - count_even}')

## В одномерном массиве из 123 чисел найти количество элементов из отрезка [10,99]

import random
array = []
count = 0

for i in range(1, 124):
    array.append(random.randint(1, 999))

for i in array:
    if i in range(10, 100):
        count += 1
        
print(count) 

## Найти сумму чисел одномерного массива стоящих на нечетной позиции

import random
array = []
my_summa = 0

for i in range(1, 15):
    array.append(random.randint(1, 9))
    
for i in range(1, len(array), 2):
    my_summa += array[i]
    
print(array, my_summa)

## Найти произведение пар чисел в одномерном массиве. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random
array = []
new_array = []
my_summa = 0

for i in range(0, 11):
    array.append(random.randint(1, 9))
 
print(array)
   
   
if len(array) % 2 != 0:
    for i in range(0, round((len(array) - 1) / 2)):
        new_array.append(array[i] * array[(i + 1) * (-1)])
    new_array.append(array[round((len(array) - 1 )/ 2)])
else:
    for i in range(0, round(len(array) / 2)):
        new_array.append(array[i] * array[(i + 1) * (-1)])
    
print(new_array)

## В Указанном массиве вещественных чисел найдите разницу между максимальным и минимальным элементом

import random
array = []

for i in range(0, 11):
    array.append(random.randint(1, 9999))
    
min_value = min(array)
max_value = max(array)

print(f'{array} \n {max_value} - {min_value} = {max_value - min_value}')

## Выяснить являются ли три числа сторонами треугольника

triangle = []

for i in range(0, 3):
    triangle.append(int(input('введите значение стороны предполагаемого треугольника ')))
    
def realy_triangle(number):
    a = number[0]
    b = number[1]
    c = number[2]   
    return (a < (b + c)) and (b < (a + c)) and (c < (a + b));

if realy_triangle(triangle):
    print(*triangle, 'являются сторонами треугольника')
else:
    print(*triangle, 'не являются сторонами треугольника')

## Определить сколько чисел больше 0 введено с клавиатуры

count = 0

while True:
    my_number = input()
    if my_number == 'end':
        break
    if int(my_number) > 0:
        count += 1
print(count)

## Написать программу преобразования десятичного числа в двоичное

number = int(input('введите число для преобразования в двоичное: '))

def double_calc(n):
    result = ''
    while n != 0:
        result = str(n % 2) + result
        n //= 2
    return result

result = double_calc(number)
print(result)

## Найти точку пересечения двух прямых заданных уравнением y = k1 * x + b1, y = k2 * x + b2, b1 k1 и b2 и k2 заданы

b1, k1, b2, k2 = input('Введите b1, k1, b2, k2 через пробел: ').split()
b1 = int(b1)
k1 = int(k1)
b2 = int(b2)
k2 = int(k2)

if k1 == k2: 
    print ('Прямые параллельны.')
    exit(0)

x = (b2 - b1) / (k1 - k2)
y = k1 * x + b1 

print(f'Координаты точки пересечения прямых x = {x}, y = {y}')

## Показать числа Фибоначчи

num = int(input('сколько чисел Фибоначчи показать? '))
fib = [0, 1]

for i in range(1, num - 1):
    fib.append(fib[i] + fib[i - 1])
    
print(*fib)

## Написать программу масштабирования фигуры. Масштабируем восьмиугольник

my_string = ''
my_list = []
while True:
    my_string = str(input('первое значение Х, второе Y '))
    if my_string == 'end':
        break
    my_list.append([int(i) for i in my_string.split()])
    
#ищем координаты середины восьмиугольника
# это пересечение линий между противоположными точками
# y = a1*x+b1
# y = a2*x+b2
a1 = (my_list[0][1] - my_list[4][1]) / (my_list[0][0] - my_list[4][0])
a2 = (my_list[1][1] - my_list[5][1]) / (my_list[1][0] - my_list[5][0])
b1 = my_list[0][1] - a1 * my_list[0][0]
b2 = my_list[1][1] - a2 * my_list[1][0]

middle_x = (b2 - b1) / (a1 - a2)
middle_y = a1 * middle_x + b1 

print(f'координаты середины октагона х = {middle_x}, y = {middle_y}')

# ищем расстояние от середины до каждой из вершин

distance = []

for i in range(0, len(my_list) - 1):
    num = ((middle_x - my_list[i][0]) ** 2 + (middle_y - my_list[i][1]) ** 2) ** (1/3)
    distance.append(round(num,2))

print(*distance)

def new_octagon(num, list, x, y):
    for i in range(0, len(list)):
        list[i][0] = num * list[i][0] - x
        list[i][1] = num * list[i][1] - y
    return list
        
def new_dist(num, distance_list):
    for i in range(0, len(distance_list)):
        distance_list[i] *= num 
    return distance_list

number = float(input('введите масштаб изменения фигуры: '))   
new_list = new_octagon(number, my_list, middle_x, middle_y)
new_distance = new_dist(number, distance)

print(f'{new_list} \n {new_distance}')

## Написать программу копирования массива
import random
array = []

for i in range(1, 13):
    array.append(random.randint(-9, 9))
      
new_array = []

new_array.append([i for i in array])

print(f'{array} \n{new_array}')

# Показать двумерный массив размером m×n заполненный целыми числами
import random


m = int(input('Введите число m: '))
n = int(input('Введите число n: '))
array = [[0 for i in range(0, m)] for j in range(0, n)]

for i in range(0, m):
    for j in range(0, n):
        array[j][i] = random.randint(1, 99)
        
for i in array:
    print(i)

## Показать двумерный массив размером m×n заполненный вещественными числами
import random


m = int(input('Введите число m: '))
n = int(input('Введите число n: '))
array = [[0 for i in range(0, m)] for j in range(0, n)]

for i in range(0, m):
    for j in range(0, n):
        array[j][i] = round(random.uniform(1, 99), 4)
        
for i in array:
    print(i)    

## В двумерном массиве n×k заменить четные элементы на противоположные
import random


m = int(input('Введите число m: '))
n = int(input('Введите число n: '))
array = [[0 for i in range(0, m)] for j in range(0, n)]

for i in range(0, m):
    for j in range(0, n):
        array[j][i] = random.randint(1, 99)

for i in range(0, m):
    for j in range(0, n):
        if array[j][i] % 2 == 0:
            array[j][i] *= -1
        
for i in array:
    print(i)

## Задать двумерный массив следующим правилом: Aₘₙ = m+n
m = int(input('Введите число m: '))
n = int(input('Введите число n: '))
array = [[0 for i in range(0, m)] for j in range(0, n)]

for i in range(0, m):
    for j in range(0, n):
        array[j][i] = i + j
        
for i in array:
    print(i)

## В двумерном массиве заменить элементы, у которых оба индекса чётные на их квадраты

import random


m = int(input('Введите число m: '))
n = int(input('Введите число n: '))
array = [[0 for i in range(0, m)] for j in range(0, n)]

for i in range(0, m):
    for j in range(0, n):
        array[j][i] = random.randint(1, 99)
        

for i in range(0, m, 2):
    for j in range(0, n, 2):
        array[j][i] **= 2
 
        
for i in array:
    print(i)

## В двумерном массиве показать позиции числа, заданного пользователем или указать, что такого элемента нет


import random


m = int(input('Введите число m: '))
n = int(input('Введите число n: '))
array = [[0 for i in range(0, m)] for j in range(0, n)]

for i in range(0, m):
    for j in range(0, n):
        array[j][i] = random.randint(1, 9)
        
num = int(input('inter a number for search: '))

count = 0           
for i in range(0, m):    
    for j in range(0, n):
        if array[j][i] == num:
            print(f'{num} in [{j}][{i}] position')
            count += 1

if count == 0:
    print('not in a list')
            
        
for i in array:
    print(i)

## Дан целочисленный массив. Найти среднее арифметическое каждого из столбцов.

import random
from all_def import fill, print_ar

m = 4
array = [[0 for i in range(0, m)] for j in range(0, m)]
       
def middle(any):
    mid = []
    summ = 0
    for i in range(0, len(any)):
        for j in range(0, len(any[0])):
            summ += any[j][i]
        mid.append(summ/len(any))
        summ = 0
    return mid
            
fill(array)
print_ar(array)
print(middle(array))

## В матрице чисел найти сумму элементов главной диагонали

import random
from all_def import fill, print_ar
m = int(input('Введите число m: '))
array = [[0 for i in range(0, m)] for j in range(0, m)]

def summa(any):
    j = 0
    summ = 0
    for i in range(0, len(any)):
        summ += any[i][j]
        j += 1
    return summ
      

fill(array)
print_ar(array)
print(summa(array))

## Написать программу, которая обменивает элементы первой строки и последней строки

import random
from all_def import fill, print_ar

m = 4
array = [[0 for i in range(0, m)] for j in range(0, m)]

def rebase(any):
    count = any[0]
    any[0] = any[len(any) - 1]
    any[len(any) - 1] = count
    return any
        
fill(array)
print_ar(array)
rebase(array)
print()
print_ar(array)

## Написать программу, упорядочивания по убыванию элементы каждой строки двумерной массива.

import random
from all_def import fill, print_ar

m = 4
array = [[0 for i in range(0, m)] for j in range(0, m)]
        
def sorting(any):
    for i in any:
        i.sort(reverse = True)
    return any

fill(array)
print_ar(array)
print()
sorting(array)
print_ar(array)

## Написать программу, которая в двумерном массиве заменяет строки на столбцы или сообщить, 
# что это невозможно (в случае, если матрица не квадратная).

import random
from all_def import fill, print_ar

m = int(input('Введите число m: '))
n = int(input('Введите число n: '))
array = [[0 for i in range(0, m)] for j in range(0, n)]
if m != n:
    print('замена не возможна!')
    exit(0)
 
def rebase(any):
    new_any = [[0 for i in range(0, len(any))] for j in range(0, len(any))]
    for i in range(0, len(any)):
        for j in range(0, len(any[0])):
            new_any[j][i] = any[i][j]
    return new_any
        
fill(array)
print_ar(array)
print()
print_ar(rebase(array))

## В прямоугольной матрице найти строку с наименьшей суммой элементов.

import random
from all_def import fill, print_ar

m = int(input('Введите число m: '))
n = int(input('Введите число n: '))
array = [[0 for i in range(0, m)] for j in range(0, n)]
if m == n:
    print('необходима прямоугольная матрица')
    exit(0)

def search(any):
    min_summa = 99999
    min_list = []
    summ = 0
    for i in any:
        for j in range(0, len(i)):
            summ += i[j]
        if summ < min_summa:
            min_summa = summ
            min_list = i
        summ = 0
    return min_list, min_summa
        

fill(array)
print_ar(array)
print()
print(search(array))

## Составить частотный словарь элементов двумерного массива

import random
from all_def import fill, print_ar

m = 10
array = [[0 for i in range(0, m)] for j in range(0, m)]

def dictinary(any):
    my_dict = {}
    for i in range(0, len(any)):
        for j in range(0, len(any[0])):
            if any[i][j] not in my_dict.keys():
                my_dict[any[i][j]] = 1
            else:
                my_dict[any[i][j]] += 1                
    return my_dict

            
fill(array)
print_ar(array)
result = dictinary(array)

for key,value in result.items():
    print(f'{key}: {value} - {round(value/((m * m) / 100), 2)}%')

## Найти произведение двух матриц

import random
from all_def import fill, print_ar

m = 5
array = [[0 for i in range(0, m)] for j in range(0, m)]
array2 = [[0 for i in range(0, m)] for j in range(0, m)]

def product(any, any2):
    new_any = [[0 for i in range(0, len(any))] for j in range(0, len(any))]
    for i in range(0, len(any)):
        for j in range(0, len(any[0])):
            new_any[i][j] = any[i][j] * any2[i][j]
    return new_any

fill(array)
fill(array2)
print_ar(array)
print()
print_ar(array2)
print()
print_ar(product(array, array2))

## В двумерном массиве целых чисел. Удалить строку и столбец, на пересечении которых расположен наименьший элемент.

import random
from all_def import fill, print_ar

m = 5
array = [[0 for i in range(m)] for j in range(m)]

def search_position(any):
    minimum = any[0][0]
    min_pos_row = 0
    min_pos_str = 0
    for i in any:
        for j in i:
            if j < minimum:
                minimum = j
                min_pos_row = i.index(j)
                min_pos_str = any.index(i)
    return minimum, min_pos_str, min_pos_row

def delete_str_row(any, str, row):
    new_any =[[0 for i in range(len(any) - 1)] for j in range(len(any) - 1)]
    k = 0
    m = 0
    for i in range(len(any)):
        if i + 1 > len(any):
            break
        elif i == str:
            continue
        for j in range(len(any)):
            if j + 1 > len(any):
                break
            elif j == row and j + 1 <= len(any):
                continue
            new_any[k][m] = any[i][j]
            m += 1
        m = 0
        k += 1
    return new_any
            

fill(array)
min_num, min_str, min_row = search_position(array)
print_ar(array)
print(f'минимальное число - {min_num} [{min_str}][{min_row}]')
new_array = delete_str_row(array, min_str, min_row)
print_ar(new_array)

## Спирально заполнить двумерный массив:

n = int(input())
spiral = [[None]* n for j in range(n)]
dx, dy = 1,0
x, y = 0,0
for i in range(1, int(n**2 + 1)):
    spiral[x][y] = i
    nx, ny = x + dx, y + dy
    if 0<=nx<n and 0<=ny<n and spiral[nx][ny] == None:
        x, y = nx, ny
    else:
        dx,dy = -dy,dx
        x,y = x+dx, y+dy
                 
for i in range(n):
    for j in range(n):
        print(spiral[j][i], end = ' ')
    print()


## Дана последовательность чисел. Получить список неповторяющихся элементов заданной последовательности. 
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

my_list = [1, 2, 3, 5, 1, 5, 3, 10]

def new_list(any_list):
    return set(any_list)

print(*new_list(my_list))