# Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.
file = open('file_54.txt', 'r')
file_1 = open('file_54_1.txt', 'r')

first_line = file.readline().replace(' ', '')
second_line = file_1.readline().replace(' ', '')
file.close()
file_1.close()

x = int(input('введите x: '))
answer = eval(f'{first_line}+{second_line}')

answer_file = open('file_54_ans.txt', 'w')
answer_file.write(f'при x = {x} \n{first_line}+{second_line} = {answer}')
answer_file.close()