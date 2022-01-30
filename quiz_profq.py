

def correct():

    if odp1.upper() == "A" or odp1.upper() == "B"  or odp1.upper()== "C" or odp1.upper() == "D":
        return True
    else: return False

def pyt1():
    global odpowiedzi
    global odp1

    print("1. DB-25 jest wykorzystywane jako złącze \n A.vga,SVGA i XGA \n B.GamePort \n C.portu równoległego LPT \n D.portu RS-422A")
    odp1 = input("prawidłowa odpowiedź to ?? ")
    if correct():
        if odp1.upper() == "D":
            print("Ta odpowiedź jest prawidłowa")
            odpowiedzi += 1
        else:
            print("Nieprawidłowa odpowiedź. ")
    else:
        print("Odpowiedzi mozemy udzielić tylko za pomocą liter A, B, C, i D")
        pyt1()
def pyt2():
    global odpowiedzi
    global odp1

    print("1. DB-25 jest wykorzystywane jako złącze \n A.vga,SVGA i XGA \n B.GamePort \n C.portu równoległego LPT \n D.portu RS-422A")
    odp1 = input("prawidłowa odpowiedź to ?? ")
    if correct():
        if odp1.upper() == "D":
            print("Ta odpowiedź jest prawidłowa")
            odpowiedzi += 1
        else:
            print("Nieprawidłowa odpowiedź. ")
    else:
        print("Odpowiedzi mozemy udzielić tylko za pomocą liter A, B, C, i D")
        pyt2()
run = True

while run:
    #zmienne
    odpowiedzi = 0
    pytania = [pyt1(), pyt2()]
    ilość_pytań = 2
    #wyjscie

    #wyświetlanie pytań
    for i in range(ilość_pytań):
        pytania[i]
    procent = ((odpowiedzi/ilość_pytań) * 100)
    print("uzyskałeś: " + str(procent), "%")
    run = False