import math
import pygame
kat1 = []
kat2 = []

def start():
    pass
def obliczanie_dlugosci_boku():
    del kat1[:]
    del kat2[:]
    x_1 = int(float(input("podaj współrzędną x pierwszego punktu: ")))
    y_1 = int(float(input("podaj współrzędną y pierwszego punktu: ")))
    x_2 = int(float(input("podaj współrzędną x drugiego punktu: ")))
    y_2 = int(float(input("podaj współrzędną y drugiego punktu: ")))
    kat1.append(x_1)
    kat1.append(y_1)
    kat2.append(x_2)
    kat2.append(y_2)

    dlugosc = math.pow((kat2[0]- kat1[0]),2)+math.pow((kat2[1]-kat1[1]),2)
    print("wynik to pierwiastek z", dlugosc)
    print("czyli", math.sqrt(dlugosc))


def oblicznie_srodka():
    del kat1[:]
    del kat2[:]

    x_1 = int(float(input("podaj współrzędną x pierwszego punktu: ")))
    y_1 = int(float(input("podaj współrzędną y pierwszego punktu: ")))
    x_2 = int(float(input("podaj współrzędną x drugiego punktu: ")))
    y_2 = int(float(input("podaj współrzędną y drugiego punktu: ")))
    kat1.append(x_1)
    kat1.append(y_1)
    kat2.append(x_2)
    kat2.append(y_2)

    s_x = (kat1[0] + kat2[0]) / 2
    s_y = (kat1[1] + kat2[1]) / 2
    print("środek wypada na wsółrzędnych x: ", s_x, "y: ", s_y)
run = True
while run:
    start()
    rodzaj = input("jaką zagadnienie związane z matematyką chcesz obliczyc? \n"
                   " 1.Obliczenie długości boku na polu współrzędnych \n"
                   " 2.Obliczenie gdzie znajduje sie środek boku.\n"
                   "odpowadaj cyframi\n"
                   "wpisz \"q\" żeby wyjsć: " )
    if rodzaj == 'q':
        run = False
    if int(rodzaj) == 1:
        obliczanie_dlugosci_boku()
    if int(rodzaj) == 2:
        oblicznie_srodka()
    if int(rodzaj) == 3:
        pass


