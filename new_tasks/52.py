# Дана последовательность чисел. Получить список неповторяющихся элементов заданной последовательности. 
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

my_list = [1, 2, 3, 5, 1, 5, 3, 10]

def new_list(any_list):
    return set(any_list)

print(*new_list(my_list))