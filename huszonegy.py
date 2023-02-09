#megoldás


def eredmeny(jatekos_lapok: [int], gep_lapok: [int]):
    szoveg = ""
    jatekos_lapok:int = pontszamitas(jatekos_lapok)
    gep_lapok:int = pontszamitas(gep_lapok)

    if jatekos_lapok > 21:
        szoveg ="Játékos vesztett"
    elif gep_lapok > 21:
        szoveg="Gép vesztett"
    else:
        szoveg = "mindketten vesztettek"
    return szoveg
def pontszamitas(lapok : [int]):
    osszeg = 0
    for i in range(len(lapok)):
        osszeg = osszeg +lapok[i]
    return osszeg


def jatekosVesztettTeszt():

    jatekosLista = [6, 4, 8, 9]
    gepLista = [6, 4, 11]
    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Játékos vesztett"

    if kapottEredmeny == vartEredmeny:
        print("Teszt sikeres. ")
    else:
        print("Teszt megbukott.")


def jatekosVesztettTeszt2():
    jatekosLista = [10, 3,  3, ]
    gepLista = [6, 10]
    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Játékos vesztett"

    if kapottEredmeny == vartEredmeny:
        print("Teszt sikeres. ")
    else:
        print("Teszt megbukott.")

def jatekosVesztettTeszt3():
    jatekosLista = [10 , 2, 8, 9]
    gepLista = [ 5, 4, 2 ]

    if len(jatekosLista) > len(gepLista):
        print("játékos vesztett")
    else:
        print("A teszt sikertelen")
def jatekosVesztettTeszt4():
    jatekosLista = [10 , 6]
    gepLista = [ 10,6]

    if len(jatekosLista) > len(gepLista):
        print("játékos vesztett")
    elif len(jatekosLista) == len(gepLista):
        print("egyenlő lapok")
    else:
        print("A teszt sikertelen")
def gepVesztettTeszt5():
    jatekosLista = [10, 6]
    gepLista = [10,2,5]

    if len(jatekosLista) < len(gepLista):
        print("gép vesztett")
    else:
        print("A teszt sikertelen")

def egyenloTeszt6():
    jatekosLista = [10,6]
    gepLista = [10,6]

    if len(jatekosLista) ==  len(gepLista):
        print("egyenlő lapok")
    else:
        print("A teszt sikertelen")


def jatekosTeszt7():
    jatekosLista = [10,6,5]
    gepLista = [10,6,3]

    if len(jatekosLista) == 21:
        print("A játékos nyert")
    else:
        print("A teszt sikertelen")

def jatekosTeszt8():
    jatekosLista = [10,5,4]
    gepLista = [6,2]

    if len(jatekosLista) > len(gepLista):
        print("A játékos nyert")
    else:
        print("A teszt sikertelen")


def tesztek():
    jatekosVesztettTeszt()
    jatekosVesztettTeszt2()
    jatekosVesztettTeszt3()
    jatekosVesztettTeszt4()
    gepVesztettTeszt5()
    egyenloTeszt6()
    jatekosTeszt7()
    jatekosTeszt8()
tesztek()
#esetek