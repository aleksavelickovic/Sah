# Ship sinking console application

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
        print("Nevalidan smer")
    
postavi_brod([["."]*10 for i in range(10)], 4, 3, 4, "v")