## По двум заданным числам проверять является ли первое квадратом второго
def Task_1(x,y):
    return x == y**2

a = int(input('a = '))
b = int(input('b = '))
print(Task_1(a, b))