## Выяснить, кратно ли число заданному, если нет, вывести остаток.
def kratno_or_not(x, y):
    if x%y ==0: return f'Число {x} кратно числу {y}'
    else: return x%y

j = -9
k = int(input('Введите число = '))
print(kratno_or_not(j, k))