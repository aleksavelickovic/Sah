# Ship sinking console application

import random

def uvod(): 
    print("Dobrodošli u igru potapanja brodova!")
    print("Unesite koordinate broda i smer u kojem želite da ga postavite.")
    print("Koordinate su u formatu A1, A2, A3... J10.")
    print("Smer može biti horizontalan (h) ili vertikalan (v).")
    print("Srećno!")
    print()
    input = input("Unesite Y za početak igre: ")
    if input == "Y" or input == "y":
        return True
    else:
        return False
    
def zapocni_igru():
    if uvod == True:
        kolicina_brodova = 15
        print("Igra je počela!")
        while kolicina_brodova > 0:
            tabla = [ ["."]*10 for i in range(10) ]
            ispisi_tablu(tabla)
            x = input("Unesite X koordinate broda: ")
            y = input("Unesite Y koordinate broda: ")
            postavi_brod(tabla, 4, x, y, "h")
            kolicina_brodova -= 1
            ispisi_tablu(tabla)
        print("Postavili ste sve brodove! Sada neprijatelj postavlja svoje brodove.")
        neprijatelj_postavlja_brodove()


def ispisi_tablu(tabla):
    print("  1 2 3 4 5 6 7 8 9 10")
    for i in range(10):
        print(chr(65+i), end=" ")
        for j in range(10):
            print(tabla[i][j], end=" ")
        print()

ispisi_tablu([["."]*10 for i in range(10)])

def postavi_brod(tabla, brod, x, y, smer):
    if smer == "h":
        for i in range(brod):
            tabla[x][y+i] = "X"
        ispisi_tablu(tabla)
    elif smer == "v":
        for i in range(brod):
            tabla[x+i][y] = "X"
        ispisi_tablu(tabla)
    else:
        print("Nevalidan smer!")
        x = input("Unesite X koordinate broda: ")
        y = input("Unesite Y koordinate broda: ")
        postavi_brod(tabla, 4, x, y, "h")
        # return False

def neprijatelj_postavlja_brodove():
    kolicina_brodova = 15
    while kolicina_brodova > 0:
        x = random.randint(0, 9)
        y = random.randint(0, 9)

    
# postavi_brod([["."]*10 for i in range(10)], 4, 3, 4, "v")