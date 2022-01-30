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