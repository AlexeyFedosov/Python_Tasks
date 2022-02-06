#Для натурального N создать множество: 1, -3, 9, -27, 81 и т.д.v
def mess (x):
    i = 0
    IO = 1
    while i < x:
        if i %2 != 0:
            print (IO*-3)
            IO *= 3
            i += 1
        else:
            print(IO*3)
            IO *= 3
            i += 1
mess(5)