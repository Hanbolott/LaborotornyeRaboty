def proc1():
    password = input('Введите пороль :')
    is_numeric = False
    is_upper = False
    is_lower = False
    is_spec = False

    for tap in password:
        if tap.isnumeric():
            is_numeric = True
        elif tap.islower():
            is_lower = True
        elif tap.isupper():
            is_upper = True
        elif tap in "#%&@$^*":
            is_spec = True

    if len(password) > 6 and is_numeric and is_upper and is_lower and is_spec:
        print('Пароль : Надежный ')
    else:
        print('Пароль не очень надежный , попробуйте еще раз')


proc1()


def proc2():
    des = int(input('Введите номер вашего места вагоне:'))
    print()
    if des >= 36:
        print('Ваше место - боковое.')
    elif des % 2:
        print('Ваше места в купе внизу')
    else:
        print('Ваше место в купе наверху ')


proc2()


def proc3():
    year = int(input())
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print('Высокосный')
    else:
        print('Не высокосный')


proc3()


def proc4():
    svet1 = input('Введи первый цвет')
    svet2 = input('Введи второй цвет')
    if (svet1 == 'красный' or svet2 == 'красный') and (svet1 == 'синий' or svet2 == 'синий'):
        print('фиолетовый')
    elif (svet1 == 'красный' or svet2 == 'красный') and (svet1 == 'желтый' or svet2 == 'желтый'):
        print('оранжевый')
    elif (svet1 == 'синий' or svet2 == 'синий') and (svet1 == 'желтый' or svet2 == 'желтый'):
        print('зеленый')
    elif svet1 == svet2 and (svet1 == 'синий' or svet1 == 'красный' or svet1 == 'желтый'):
        print(svet1)
    else:
        print('Ошибка в выборе цвета')


proc4()