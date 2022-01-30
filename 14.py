## Найти третью цифру числа или сообщить, что её нет
import random
num = random.randint(1,999)

third_num = (num % 1000)//100

if num > 99:
    print(third_num)
else:
    print('третьей цифры нет')

print(num)