def f_task():
    n = int(input('Введите количество монеток: '))
    count_z, count_o = 0, 0
    print('Введите монетки через Enter, 1 - решка, 0 - орел: ')
    for i in range(n):
        coin = int(input())
        if coin < 0 or coin > 1:
            print('Вы ввели некорректное значение!')
            break
        elif coin == 1:
            count_o += 1
        elif coin == 0:
            count_z += 1
    print(f'Минимальное количество монет: {count_o if count_z > count_o else count_z}')
def s_task():
    s = int(input('Введите сумму двух чисел: '))
    p = int(input('Введите произведение двух чисел: '))
    for x in range(s):
        for y in range(p):
            if s == x + y and p == x * y:
                print(f'Первое число: {x}, второе: {y}')
def th_task():
    num, i = int(input('Введите число: ')), 0
    while 2 ** i <= num:
        print(2 ** i)
        i += 1
stp = True
while stp:
    n = int(input('Введите номер задачи: '))
    if n == 1:
        f_task()
    elif n == 2:
        s_task()
    elif n == 3:
        th_task()
    else:
        print('Программа завершена')
        stp = False