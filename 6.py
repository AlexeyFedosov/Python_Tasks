## Выяснить является ли число чётным
from cProfile import run
import random
num = random.randint(1,99)

if num % 2 == 0:
    print(f'число {num} является четным')
else:
    print(f'число {num} не является четным')