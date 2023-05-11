from random import randint


def proc3():
    slova = []
    while (one_word := str(input())) !="stop":
        slova.append(one_word)

    print(" ".join(slova))
proc3()


def proc4():
 word = input("введите слово:")
 for i in range(len(word)):
    if word[i]=="Ф" or word[i]=="ф":
        print("Ого! Это редкое слово")
        break
    else:
        print("Эч , это не очень редкое слово")
        break
proc4()

def proc5():
    uni=0


    print("Для завершения игры введите слово stop")
    while True:
        a = randint(1, 100)
        b = randint(1, 100)
        print(f"{a} + {b} = ", end="")
        res = input()

        if res == "stop":
            break
        res = int(res)
        if a+b == res:
            print("Правильно!")
        else:
            print("Ответ неправильный :(")
            uni = uni + 1
        if uni == 3:
           print('игра окончена')
           break

proc5()
