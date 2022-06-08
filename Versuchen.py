import sys
spielfeldgröße=8
Player1=[]
Player2=[]
space= " "
Name1=input()
Name2=input()
Gone=[]
Board1,Board2 = [[space] * spielfeldgröße for i in range(spielfeldgröße)],\
                [[space] * spielfeldgröße for i in range(spielfeldgröße)]

Guess1,Guess2= [[space] * spielfeldgröße for i in range(spielfeldgröße)],\
                [[space] * spielfeldgröße for i in range(spielfeldgröße)]

Board3=[[space] * spielfeldgröße for i in range(spielfeldgröße)]

ships = {"Ship1": 5,
             "Ship2": 4,
             "Ship3": 3,
             "Ship4": 2}

shipcount= {"Ship1": 1,
             "Ship2": 2,
             "Ship3": 3,
             "Ship4": 4}

Player1.append(Name1)
Player1.append(Board1)
Player1.append(Guess1)
Player1.append(Gone)
Player1.append(ships)
Player2.append(Name2)
Player2.append(Board2)
Player2.append(Guess2)
Player2.append(ships)



def print_grid(Board):
    #Buchstaben Notation als Spalte
    sys.stdout.write("  ")
    for i in range(spielfeldgröße):
        sys.stdout.write(" " + chr(i + 65))
    print(" ")

    #Schönere Darstellung
    row_number = 1
    for row in Board:
        if row_number<10:
            grid=("%d |%s|" % (row_number,"|".join(row)))
        else:
            grid = ("%d|%s|" % (row_number, "|".join(row)))
        print(grid)
        row_number += 1
print_grid(Board1)

def placeship(Board):
    Board3 = [[space] * spielfeldgröße for i in range(spielfeldgröße)]
    for j in range(shipcount["Ship1"]):
        while True:
            try:
                while True:
                    zustand = True
                    while True:
                        try:
                            while zustand:
                                print("Welche Zeile soll das", j + 1, "te Schlachtschiff gesetzt werden")
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
                        print("Welche Spalte soll das", j + 1, "te Schlachtschiff gesetzt werden")
                        Spalte = (input("Spalte"))
                        for i in range(spielfeldgröße):
                            if Spalte == chr(i + 65):
                                zustand = False
                                break

                    break

                ShipPosition = int(input("0 für Horizontal und 1 für Vertikal"))

                for i in range(ships["Ship1"]):

                    if ShipPosition == 0:
                        Board3[Zeile][(i + ord(Spalte)) - 65] = "x"




                    else:
                        Board3[i + Zeile][ord(Spalte) - 65] = "x"
                break
            except IndexError:
                print("Kein Platz")
                Board3.clear()
                Board3 = [[space] * spielfeldgröße for i in range(spielfeldgröße)]

        array = [(ix, iy) for ix, row in enumerate(Board3) for iy, i in enumerate(row) if i == "x"]
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
                    Board[Zeile][(i + ord(Spalte)) - 65] = "x"

                else:
                    Board[i + Zeile][ord(Spalte) - 65] = "x"

        if any(p in sublist for sublist in Gone) == False:
            Gone.append(array)

    print(array)
    print(Gone)

    for j in range(shipcount["Ship2"]):
        while True:
            try:
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
                        print("Welche Spalte soll der", j + 1, "te Kreuzer gesetzt werden")
                        Spalte = (input("Spalte"))
                        for i in range(spielfeldgröße):
                            if Spalte == chr(i + 65):
                                zustand = False
                                break

                    break

                ShipPosition = int(input("0 für Horizontal und 1 für Vertikal"))

                for i in range(ships["Ship2"]):

                    if ShipPosition == 0:
                        Board3[Zeile][(i + ord(Spalte)) - 65] = "s"




                    else:
                        Board3[i + Zeile][ord(Spalte) - 65] = "s"
                break
            except IndexError:
                print("Kein Platz")
                Board3.clear()
                Board3 = [[space] * spielfeldgröße for i in range(spielfeldgröße)]
                
        array2 = [(ix, iy) for ix, row in enumerate(Board3) for iy, i in enumerate(row) if i == "s"]
        Board3.clear()
        Board3 = [[space] * spielfeldgröße for i in range(spielfeldgröße)]
        for p in array2:
            a=any(p in sublist for sublist in Gone)
            if a==True:
                print("Geht nicht")
                break
        if a==False:
            for i in range(ships["Ship2"]):
                if ShipPosition == 0:
                    Board[Zeile][(i + ord(Spalte)) - 65] = "s"

                else:
                    Board[i + Zeile][ord(Spalte) - 65] = "s"

        if any(p in sublist for sublist in Gone) == False:
            Gone.append(array2)

    print(array2)
    print(Gone)


# liste=[1,3,2]
# indices = [i for i, x in enumerate(liste) if x == 3]
placeship(Board1)
print_grid(Board1)
#print(indices)
# print(liste.index(3))
#print(Player1)

#print_grid(Board3)


# Board1[0][0]="x"
# Board1[5][2]="x"
# a = Board1
#
# [(ix,iy) for ix, row in enumerate(a) for iy, i in enumerate(row) if i == "x"]

# a=[[1,2,3]]
# b=[1,4,5]
# for i in b:
#
#     if any(i in sublist for sublist in a):
#         print("ja")
#         print(i)

# Board3[0][5]="s"
# Board3[0][4]="s"
# a=[[2,3,4],[3,4,5]]
# Board3.clear()

# Board3[1][0]="s"
# Board3[1][1]="s"
# Board3[1][2]="s"
# Board3[1][3]="s"
#
# print_grid(Board3)
# array2 = [(ix, iy) for ix, row in enumerate(Board3) for iy, i in enumerate(row) if i == "s"]
# Gone=[[(0,1),(0,2),(1,6),(0,6)]]
# for q in array2:
#     if any(q in sublist for sublist in Gone):
#         print(q)
#     else:
#         Board3[3][2] = "s"
#         Board3[4][2] = "s"
#         Board3[5][2] = "s"
#         Board3[6][2] = "s"
