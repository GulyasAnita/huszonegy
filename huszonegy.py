#megoldás
jatekos_lapok = [2, 3, 4]
gep_lapok = [10, 4, 10]


def eredmeny(jatekos_lapok: [int], gep_lapok: [int]):
    jatekos_lapok:int = pontszamitas(jatekos_lapok)
    gep_lapok:int = pontszamitas(gep_lapok)
    if jatekos_lapok > 21:
        print("vesztett")
    elif gep_lapok > 21:
        print("vesztett")
    else:
        print("Mindketten vesztettek")

def pontszamitas(lapok : [int]):
    osszeg = 0
    for i in range(len(lapok)):
        osszeg = osszeg +lapok[i]
    return osszeg





#esetek