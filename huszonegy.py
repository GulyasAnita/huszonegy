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

def tesztek():
    jatekosVesztettTeszt()

tesztek()
#esetek