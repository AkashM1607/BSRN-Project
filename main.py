import sys
#spielfeld
spielfeldgröße = 0

while not (8 <= spielfeldgröße <= 12):
    try:
        spielfeldgröße = int(input('Bitte geben Sie die gewünschte Spielfeldgröße ein (AxA).'))
        if 12 < spielfeldgröße or spielfeldgröße < 8:
            print('Spielfeldgröße nicht nicht akzeptiert.')
        else:
            continue
    except ValueError:
        print("Falsche Eingabe, nur Zahlen erlaubt")


space=" "
hit="X"
miss="O"
ship="*"

#Board
board = [[space] * spielfeldgröße for i in range(spielfeldgröße)]
def print_grid():
    #Buchstaben Notation als Spalte
    sys.stdout.write("  ")
    for i in range(spielfeldgröße):
        sys.stdout.write(" " + chr(i + 65))
    print(" ")

    #Schönere Darstellung
    row_number = 1
    for row in board:
        if row_number<10:
            grid=("%d |%s|" % (row_number,"|".join(row)))
        else:
            grid = ("%d|%s|" % (row_number, "|".join(row)))
        print(grid)
        row_number += 1

print_grid()

def place_ship():


    ships = {"Ship1": 5,
             "Ship2": 4,
             "Ship3": 3,
             "Ship4": 2}

    for j in range(1):
        while True:
            zustand = True
            while True:
                try:
                    while zustand:
                        print("Welche Zeile soll das Schlachtschiff gesetzt werden")
                        Zeile = int(input("Zeile")) - 1
                        for i in range(spielfeldgröße):
                            if Zeile == i:
                                zustand = False
                                break
                    break
                except ValueError:
                    print("Falsche Eingabe")
            zustand = True
            while zustand:
                print("Welche Spalte soll das Schlachtschiff gesetzt werden")
                Spalte = (input("Spalte"))
                for i in range(spielfeldgröße):
                    if Spalte == chr(i + 65):
                        zustand = False
                        break

            break
        ShipPosition = int(input("0 für Horizontal und 1 für Vertikal"))


        for i in range(ships["Ship1"]):
            if ShipPosition == 0:
                board[Zeile][(i + ord(Spalte)) - 65] = "x"
            else:
                board[i + Zeile][ord(Spalte) - 65] = "x"

    for j in range(2):
        while True:
            zustand = True
            while True:
                try:
                    while zustand:
                        print("Welche Zeile soll der", j + 1, "te Kreuzer gesetzt werden")
                        Zeile = int(input("Zeile")) - 1
                        for i in range(spielfeldgröße):
                            if Zeile == i:
                                zustand = False
                                break
                    break
                except ValueError:
                    print("Falsche Eingabe")
            zustand = True
            while zustand:
                print("Welche Spalte soll der",j+1,"te Kreuzer gesetzt werden")
                Spalte = (input("Spalte"))
                for i in range(spielfeldgröße):
                    if Spalte == chr(i + 65):
                        zustand = False
                        break

            break
        ShipPosition = int(input("0 für Horizontal und 1 für Vertikal"))
        for i in range(ships["Ship2"]):
            if ShipPosition == 0:
                board[Zeile][i + ord(Spalte) - 65] = "x"
            else:
                board[i + Zeile][ord(Spalte) - 65] = "x"

    for j in range(3):
        while True:
            zustand = True
            while True:
                try:
                    while zustand:
                        print("Welche Zeile soll der", j + 1, "te Zerstörer gesetzt werden")
                        Zeile = int(input("Zeile")) - 1
                        for i in range(spielfeldgröße):
                            if Zeile == i:
                                zustand = False
                                break
                    break
                except ValueError:
                    print("Falsche Eingabe")
            zustand = True
            while zustand:
                print("Welche Spalte soll der",j+1,"te Zerstörer gesetzt werden")
                Spalte = (input("Spalte"))
                for i in range(spielfeldgröße):
                    if Spalte == chr(i + 65):
                        zustand = False
                        break

            break
        ShipPosition = int(input("0 für Horizontal und 1 für Vertikal"))
        for i in range(ships["Ship3"]):
            if ShipPosition == 0:
                board[Zeile][i + ord(Spalte) - 65] = "x"
            else:
                board[i + Zeile][ord(Spalte) - 65] = "x"

    for j in range(4):
        while True:
            zustand = True
            while True:
                try:
                    while zustand:
                        print("Welche Zeile soll das", j + 1, "te Uboot gesetzt werden")
                        Zeile = int(input("Zeile")) - 1
                        for i in range(spielfeldgröße):
                            if Zeile == i:
                                zustand = False
                                break
                    break
                except ValueError:
                    print("Falsche Eingabe")
            zustand = True
            while zustand:
                print("Welche Spalte soll das",j+1,"te Uboot gesetzt werden")
                Spalte = (input("Spalte"))
                for i in range(spielfeldgröße):
                    if Spalte == chr(i + 65):
                        zustand = False
                        break

            break
        ShipPosition = int(input("0 für Horizontal und 1 für Vertikal"))
        for i in range(ships["Ship4"]):
            if ShipPosition == 0:
                board[Zeile][i + ord(Spalte) - 65] = "x"
            else:
                board[i + Zeile][ord(Spalte) - 65] = "x"

place_ship()
print_grid()
# Zeile=int(input("Welche Zeile"))-1
# Spalte=(input("Welche Spalte"))
#
#
# print_grid()
# if board[Zeile][ord(Spalte)-65]=="x":
#     print("Treffer")
# else:
#     print("Kein Treffer")
