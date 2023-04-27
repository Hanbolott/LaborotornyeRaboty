def zadach1():
    k = input("выберите число")
    k = int(k)
    l = [1,2,3,4,5,6]
    if k in l:
        print('поздравляю вы угадали!')
    else:
        print("нет такого числа")

def zadach2():

        list = ["1", "2", "3", "3", "5", "5", "6"]
        for i in range(len(list) - 1):
            if list[i] == list[i + 1]:
                print('Есть совпадение', list[i])


def zadach3():
    weeks = ("mond",'tued','wedd','thud','frid','sund','sutd')
    a =input('введите день: ')
    print('ваши выходные: ',weeks[7-int(a):])
    print("оставшие дни: ",weeks[:7-int(a)])

def zadach4():
    k = 0
    list = ["Абийбиллаев", " Капров", "Иванов", " студент1", "студент2", " студент3", " студент4", " студент5",
            "студент6", " студент7"]
    list1 = ["Абийбиллаев23", " Иванов", " Анисова", " студент0", "студент9", " студент77", " студент99", " студент66",
             "студент68", " студент87"]
    list2 = (list[0], list[1], list[0], list[8])
    print(list)
    print(list1)
    print(list2)
    print(len(list2))
    list2 = tuple(sorted(list2))
    print(list2)
    for i in range(len(list2)):
        if list2[i] == "Иванов":
            k += 1

    else:
        print('не встречается')


    print('встречается', k, 'раз')

zadach4()

