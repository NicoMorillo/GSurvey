from asd import formato
import time


def todojunto(lista):

    print("Complete list")
    for i, linea in enumerate(lista, 1):
        print("\t {} - {}. ".format(i, linea))

desarrollo = formato()



x = 0
while  x != 3:
    time.sleep(1.5)
    todojunto(desarrollo)
    x += 1
    chose = int(input("Pick: "))
    if chose == 1 or chose == 2 or chose == 3:
        print("x")