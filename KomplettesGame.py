import sys

spielfeldgröße = 0

while not (8 <= spielfeldgröße <= 12):
    try:
        print("Bitte geben Sie die gewünschte Spielfeldgröße ein (AxA) zulässige Eingaben: 8-12\n")
        spielfeldgröße = int(input('Spielfeldgröße: '))
        if 12 < spielfeldgröße or spielfeldgröße < 8:
            print('Spielfeldgröße nicht nicht akzeptiert. Zulässige Größe: 8-12')
        else:
            continue
    except ValueError:
        print("Falsche Eingabe, nur Zahlen erlaubt")


Player1 = []
Player2 = []
space = " "
Name1 = input("\nWie heißt Spieler1? Spieler1: ")
Name2 = input("\nWie heißt Spieler2? Spieler2: ")
Gone1 = []
Gone2 = []
Board1, Board2 = [[space] * spielfeldgröße for i in range(spielfeldgröße)], \
                 [[space] * spielfeldgröße for i in range(spielfeldgröße)]

Guess1, Guess2 = [[space] * spielfeldgröße for i in range(spielfeldgröße)], \
                 [[space] * spielfeldgröße for i in range(spielfeldgröße)]

Board3 = [[space] * spielfeldgröße for i in range(spielfeldgröße)]

ships = {"Ship1": 5,
         "Ship2": 4,
         "Ship3": 3,
         "Ship4": 2}

shipcount = {"Ship1": 1,
             "Ship2": 2,
             "Ship3": 3,
             "Ship4": 4}

Player1.append(Name1)
Player1.append(Board1)
Player1.append(Guess1)
Player1.append(Gone1)
Player1.append(ships)
Player2.append(Name2)
Player2.append(Board2)
Player2.append(Guess2)
Player2.append(Gone2)
Player2.append(ships)


def clearscreen():
    for i in range(50):
        print("")

clearscreen()

def print_grid(Board):
    # Buchstaben Notation als Spalte
    sys.stdout.write("  ")
    for i in range(spielfeldgröße):
        sys.stdout.write(" " + chr(i + 65))
    print(" ")

    # Schönere Darstellung
    row_number = 1
    for row in Board:
        if row_number < 10:
            grid = ("%d |%s|" % (row_number, "|".join(row)))
        else:
            grid = ("%d|%s|" % (row_number, "|".join(row)))
        print(grid)
        row_number += 1



def placeship(Board,Gone,Name):
    print(Name+",","Bitte Platziere deine Schiffe")
    print("")
    print_grid(Board)
    Board3 = [[space] * spielfeldgröße for i in range(spielfeldgröße)]
    for j in range(shipcount["Ship1"]):
        while True:
            try:
                while True:
                    zustand = True
                    while True:
                        try:
                            while zustand:
                                print("\nIn welche Zeile soll das", j + 1, "te Schlachtschiff gesetzt werden?")
                                Zeile = int(input("Zeile: ")) - 1
                                for i in range(spielfeldgröße):
                                    if Zeile == i:
                                        zustand = False
                                        break
                            break
                        except ValueError:
                            print("Falsche Eingabe! Bitte nochmal eingeben! ")
                    zustand = True
                    while zustand:
                        print("\nIn welche Spalte soll das", j + 1, "te Schlachtschiff gesetzt werden?")
                        Spalte = (input("Spalte: "))
                        for i in range(spielfeldgröße):
                            if Spalte == chr(i + 65):
                                zustand = False
                                break

                    break

                while True:
                    try:
                        ShipPosition = int(input("\nTippe 0 für Horizontal und 1 für Vertikal. "))
                        print("")
                        if ShipPosition != 1 and ShipPosition != 0:
                            raise Exception
                        break
                    except Exception:
                        print("Unzulässige Eingabe, nochmal eingeben! ")

                for i in range(ships["Ship1"]):

                    if ShipPosition == 0:
                        Board3[Zeile][(i + ord(Spalte)) - 65] = "s"




                    else:
                        Board3[i + Zeile][ord(Spalte) - 65] = "s"
                break
            except IndexError:
                print("Kein Platz")
                Board3.clear()
                Board3 = [[space] * spielfeldgröße for i in range(spielfeldgröße)]

        array = [(ix, iy) for ix, row in enumerate(Board3) for iy, i in enumerate(row) if i == "s"]
        Board3.clear()
        Board3 = [[space] * spielfeldgröße for i in range(spielfeldgröße)]
        for p in array:
            a = any(p in sublist for sublist in Gone)
            if a == True:
                print("Geht nicht")
                break
        if a == False:
            for i in range(ships["Ship1"]):
                if ShipPosition == 0:
                    Board[Zeile][(i + ord(Spalte)) - 65] = "s"

                else:
                    Board[i + Zeile][ord(Spalte) - 65] = "s"

        if any(p in sublist for sublist in Gone) == False:
            Gone.append(array)
        print_grid(Board)



    for j in range(shipcount["Ship2"]):
        a=True
        while True:
            try:
                while True:
                    try:
                        while True:
                            zustand = True
                            while True:
                                try:
                                    while zustand:
                                        print("\nIn welche Zeile soll der", j + 1, "te Kreuzer gesetzt werden?")
                                        Zeile = int(input("Zeile: ")) - 1
                                        for i in range(spielfeldgröße):
                                            if Zeile == i:
                                                zustand = False
                                                break
                                    break
                                except ValueError:
                                    print("Falsche Eingabe! Bitte nochmal eingeben! ")
                            zustand = True
                            while zustand:
                                print("\nIn welche Spalte soll der", j + 1, "te Kreuzer gesetzt werden?")
                                Spalte = (input("Spalte: "))
                                for i in range(spielfeldgröße):
                                    if Spalte == chr(i + 65):
                                        zustand = False
                                        break

                            break

                        while True:
                            try:
                                ShipPosition = int(input("\nTippe 0 für Horizontal und 1 für Vertikal. "))
                                print("")
                                if ShipPosition != 1 and ShipPosition != 0:
                                    raise Exception
                                break
                            except Exception:
                                print("Unzulässige Eingabe, nochmal eingeben!")

                        for i in range(ships["Ship2"]):

                            if ShipPosition == 0:
                                Board3[Zeile][(i + ord(Spalte)) - 65] = "k"




                            else:
                                Board3[i + Zeile][ord(Spalte) - 65] = "k"
                        break
                    except IndexError:
                        print("Kein Platz! Spielfeld wurde überquert. Nochmal versuchen! ")
                        Board3.clear()
                        Board3 = [[space] * spielfeldgröße for i in range(spielfeldgröße)]

                array2 = [(ix, iy) for ix, row in enumerate(Board3) for iy, i in enumerate(row) if i == "k"]
                Board3.clear()
                Board3 = [[space] * spielfeldgröße for i in range(spielfeldgröße)]
                for p in array2:
                    a = any(p in sublist for sublist in Gone)
                    if a == True:
                        raise Exception
                break
            except Exception:
                print("Unzulässige Eingabe! Nochmal eingeben!")

        if a == False:
            for i in range(ships["Ship2"]):
                if ShipPosition == 0:
                    Board[Zeile][(i + ord(Spalte)) - 65] = "k"

                else:
                    Board[i + Zeile][ord(Spalte) - 65] = "k"

        if any(p in sublist for sublist in Gone) == False:
            Gone.append(array2)
        print_grid(Board)

    for j in range(shipcount["Ship3"]):
        a=True
        while True:
            try:
                while True:
                    try:
                        while True:
                            zustand = True
                            while True:
                                try:
                                    while zustand:
                                        print("\nIn welche Zeile soll der", j + 1, "te Zerstörer gesetzt werden?")
                                        Zeile = int(input("Zeile: ")) - 1
                                        for i in range(spielfeldgröße):
                                            if Zeile == i:
                                                zustand = False
                                                break
                                    break
                                except ValueError:
                                    print("Falsche Eingabe! Nochmal eingeben! ")
                            zustand = True
                            while zustand:
                                print("\nIn welche Spalte soll der", j + 1, "te Zerstörer gesetzt werden?")
                                Spalte = (input("Spalte: "))
                                for i in range(spielfeldgröße):
                                    if Spalte == chr(i + 65):
                                        zustand = False
                                        break

                            break

                        while True:
                            try:
                                ShipPosition = int(input("\nTippe 0 für Horizontal und 1 für Vertikal! "))
                                print("")
                                if ShipPosition != 1 and ShipPosition != 0:
                                    raise Exception
                                break
                            except Exception:
                                print("Unzulässige Eingabe, nochmal eingeben! ")

                        for i in range(ships["Ship3"]):

                            if ShipPosition == 0:
                                Board3[Zeile][(i + ord(Spalte)) - 65] = "z"




                            else:
                                Board3[i + Zeile][ord(Spalte) - 65] = "z"
                        break
                    except IndexError:
                        print("Kein Platz")
                        Board3.clear()
                        Board3 = [[space] * spielfeldgröße for i in range(spielfeldgröße)]

                array2 = [(ix, iy) for ix, row in enumerate(Board3) for iy, i in enumerate(row) if i == "z"]
                Board3.clear()
                Board3 = [[space] * spielfeldgröße for i in range(spielfeldgröße)]
                for p in array2:
                    a = any(p in sublist for sublist in Gone)
                    if a == True:
                        raise Exception
                break
            except Exception:
                print("Unzulässige Eingabe! Nochmal eingeben! ")

        if a == False:
            for i in range(ships["Ship3"]):
                if ShipPosition == 0:
                    Board[Zeile][(i + ord(Spalte)) - 65] = "z"

                else:
                    Board[i + Zeile][ord(Spalte) - 65] = "z"

        if any(p in sublist for sublist in Gone) == False:
            Gone.append(array2)
        print_grid(Board)

    for j in range(shipcount["Ship4"]):
        a=True
        while True:
            try:
                while True:
                    try:
                        while True:
                            zustand = True
                            while True:
                                try:
                                    while zustand:
                                        print("\nIn welche Zeile soll das", j + 1, "te UBoot gesetzt werden? ")
                                        Zeile = int(input("Zeile: ")) - 1
                                        for i in range(spielfeldgröße):
                                            if Zeile == i:
                                                zustand = False
                                                break
                                    break
                                except ValueError:
                                    print("Falsche Eingabe! Nochmal eingeben! ")
                            zustand = True
                            while zustand:
                                print("\nIn welche Spalte soll das", j + 1, "te UBoot gesetzt werden?")
                                Spalte = (input("Spalte: "))
                                for i in range(spielfeldgröße):
                                    if Spalte == chr(i + 65):
                                        zustand = False
                                        break

                            break

                        while True:
                            try:
                                ShipPosition = int(input("\nTippe 0 für Horizontal und 1 für Vertikal. "))
                                print("")
                                if ShipPosition != 1 and ShipPosition != 0:
                                    raise Exception
                                break
                            except Exception:
                                print("Unzulässige Eingabe, nochmal eingeben!")

                        for i in range(ships["Ship4"]):

                            if ShipPosition == 0:
                                Board3[Zeile][(i + ord(Spalte)) - 65] = "u"




                            else:
                                Board3[i + Zeile][ord(Spalte) - 65] = "u"
                        break
                    except IndexError:
                        print("Kein Platz! ")
                        Board3.clear()
                        Board3 = [[space] * spielfeldgröße for i in range(spielfeldgröße)]

                array2 = [(ix, iy) for ix, row in enumerate(Board3) for iy, i in enumerate(row) if i == "u"]
                Board3.clear()
                Board3 = [[space] * spielfeldgröße for i in range(spielfeldgröße)]
                for p in array2:
                    a = any(p in sublist for sublist in Gone)
                    if a == True:
                        raise Exception
                break
            except Exception:
                print("Nochmal eingeben! ")

        if a == False:
            for i in range(ships["Ship4"]):
                if ShipPosition == 0:
                    Board[Zeile][(i + ord(Spalte)) - 65] = "u"

                else:
                    Board[i + Zeile][ord(Spalte) - 65] = "u"

        if any(p in sublist for sublist in Gone) == False:
            Gone.append(array2)
        print_grid(Board)






#placeship(Board1)
#print_grid(Board1)

def attack(Board,Guess,Name,Gone):

    print(Name,"ist dran, bitte Bildschirm übergeben!\n")
    input(Name+", bitte Enter drücken \n")
    if Board==Board1:
        print_grid(Board2)
        print_grid(Guess)
    elif Board==Board2:
        print_grid(Board1)
        print_grid(Guess)
    while True:
        try:
            while True:
                zustand = True
                while True:
                    try:
                        while zustand:
                            print("Welche Zeile willst du attackieren?")
                            Zeile = int(input("Zeile: ")) - 1
                            for i in range(spielfeldgröße):
                                if Zeile == i:
                                    zustand = False
                                    break
                        break
                    except ValueError:
                        print("Falsche Eingabe! ")
                zustand = True
                while zustand:
                    print("Welche Spalte willst du attackieren?")
                    Spalte = (input("Spalte: "))
                    print()
                    for i in range(spielfeldgröße):
                        if Spalte == chr(i + 65):
                            zustand = False
                            break

                break
            if Guess[Zeile][(ord(Spalte)) - 65] == "x" or Guess[Zeile][(ord(Spalte)) - 65] == "0":
                raise Exception
            break
        except Exception:
            print("Dieses Feld wurde schon nach Schiffen überprüft.")
            print("Bitte ein anderes Feld eingeben!")
    Gone3 = []
    if(Board[Zeile][(ord(Spalte)) - 65]) != " ":
        Guess[Zeile][(ord(Spalte)) - 65]="x"

        shot = ([(ix, iy) for ix, row in enumerate(Guess) for iy, i in enumerate(row) if i == "x"])
        for p in shot:
            b=any(p in sublist for sublist in Gone)
            if b==True:
                Gone = [list(tuple(ele for ele in sub if ele != p)) for sub in Gone]

        for i in range(10):
            if i==0:
                if Gone[i] == []:
                    Gone3.append("Schlachtschiff zerstört!")

            if i==1 or i==2:
                if Gone[i] == []:
                    Gone3.append("Kreuzer zerstört!")
            if i==3 or i==4 or i==5:
                if Gone[i] == []:
                    Gone3.append("Zerstörer zerstört!")
            if i==6 or i==7 or i==8 or i==9:
                if Gone[i] == []:
                    Gone3.append("U-Boot zerstört!")


        if Gone3 == []:
            print("\nBis jetzt keine Schiffe zerstört.\n")
        else:
            print(Gone3)

    if (Board[Zeile][(ord(Spalte)) - 65]) == " ":
        Guess[Zeile][(ord(Spalte)) - 65] = "0"
        print("Fehlschuss!")

    if Board==Board1:
        print_grid(Board2)
        print_grid(Guess)
    elif Board==Board2:
        print_grid(Board1)
        print_grid(Guess)
    if Gone[0] == [] and Gone[1] == [] and Gone[2] == [] and Gone[3] == [] and Gone[4] == [] and Gone[5] == []\
            and Gone[6] == [] and Gone[7] == [] and Gone[8] == [] and Gone[9] == []:
        sys.exit("Game Over"+" "+Name+" "+"hat Gewonnen")


placeship(Board1,Gone1,Name1)
input("\nBitte drücke Enter und übergebe die Kontrolle an den anderen Spieler.\n")
clearscreen()
placeship(Board2,Gone2,Name2)
input("\nBitte drücke Enter um das Spiel zu starten.")
clearscreen()

while True:
    attack(Board2,Guess1,Name1,Gone2)#spieler1
    input("")
    clearscreen()
    attack(Board1,Guess2,Name2,Gone1)#spieler2
    input("")
    clearscreen()


# print(Gone1)
# print(Gone2)
# print_grid(Board1)
# print_grid(Board2)

# liste=[[(1,2),(3,4)],[(6,7),(8,9)]]
# tupel=[(8,9)]
#
# print(tupel[0])
#


# new_list = [x for x in new_list if x[0] != "J04550"]
# Gone=[((0, 1), (0, 2), (0, 3), (0, 4), ['Ship']), ((1, 0), (1, 1), (1, 2), (1, 3), ['Ship']), ((2, 0), (2, 1), (2, 2), (2, 3), ['Ship'])]
# Gone.pop(1)
# print(Gone)
