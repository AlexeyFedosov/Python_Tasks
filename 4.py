## Найти максимальное из трех чисел
import random
num = random.randint(1,99)
num2 = random.randint(1,99)
num3 = random.randint(1,99)

num4 = max(num, num2, num3)
print(f'{num4} это большее из чисел {num}, {num2} и {num3}')