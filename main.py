# Ship sinking console application
# Test Test test
# Testttt

import random

def uvod(): 
    print("Dobrodošli u igru potapanja brodova!")
    print("Unesite koordinate broda i smer u kojem želite da ga postavite.")
    print("Koordinate su u formatu A1, A2, A3... J10.")
    print("Smer može biti horizontalan (h) ili vertikalan (v).")
    print("Srećno!")
    print()
    izbor = input("Unesite Y za početak igre: ")
    if izbor == "Y" or izbor == "y":
        zapocni_igru()
    else:
        return False
    
def zapocni_igru():
    kolicina_brodova = 15
    print("Igra je počela!")
    while kolicina_brodova > 0:
        tabla = [ ["."]*10 for i in range(10) ]
        ispisi_tablu(tabla)
        x = input("Unesite X koordinate broda: ")
        y = input("Unesite Y koordinate broda: ")
        smer = input("Unesite smer broda (h/v): ")
        postavi_brod(tabla, 4, x, y, smer)
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

# ispisi_tablu([["."]*10 for i in range(10)])

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
        tabla = [ ["."]*10 for i in range(10) ]
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        smer = random.choice(["h", "v"])
        postavi_brod(tabla, 4, x, y, smer)
        kolicina_brodova -= 1

def gađaj(tabla):
    x = input("Unesite X koordinate gađanja: ")
    y = input("Unesite Y koordinate gađanja: ")
    if tabla[x][y] == "X":
        print("Pogodak!")
        tabla[x][y] = "O"
        ispisi_tablu(tabla)
    else:
        print("Promašaj!")
        ispisi_tablu(tabla)
    if proveri_pobedu(tabla) == True:
        print("Pobedili ste!")
        return True
    print("Neprijatelj gađa...")

def neprijatelj_gađa(tabla):
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    if tabla[x][y] == "X":
        print("Neprijatelj je pogodio vaš brod!")
        tabla[x][y] = "O"
        ispisi_tablu(tabla)
    else:
        print("Neprijatelj je promašio!")
        ispisi_tablu(tabla)
    if proveri_pobedu(tabla) == True:
        print("Izgubili ste!")
        return True  

def proveri_pobedu(tabla):
    for i in range(10):
        for j in range(10):
            if tabla[i][j] == "X":
                return False
    return True

uvod()

    
# postavi_brod([["."]*10 for i in range(10)], 4, 3, 4, "v")