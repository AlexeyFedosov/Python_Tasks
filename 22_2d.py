## Найти расстояние между точками в пространстве 2D

xa = int(input('Введите координату X для точки A: '))
ya = int(input('Введите координату Y для точки A: '))
xb = int(input('Введите координату X для точки B: '))
yb = int(input('Введите координату Y для точки B: '))

distanceAB = round(((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5, 4)
print(f'Расстояние между точками A и B равно {distanceAB}')