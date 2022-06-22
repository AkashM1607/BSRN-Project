import sys

boardSize = 0
#Boardgröße bestimmen.
while not (8 <= boardSize <= 12):
    try:
        boardSize = int(input('Bitte geben Sie die gewünschte Spielfeldgröße ein (AxA).'))
        if 12 < boardSize or boardSize < 8:
            print('Spielfeldgröße nicht nicht akzeptiert.')
        else:
            continue
    except ValueError:
        print("Falsche Eingabe, nur Zahlen erlaubt")

#Spieler Profile erstellen
Player1 = []
Player2 = []
space = " "
Name1 = input("Wie heißt Spieler1?")#Name Spieler1
Name2 = input("Wie heißt Spieler2?")#Name Spieler2
#Gone speichert koordinaten als liste von Tupeln von gesetzten Schiffen
Gone1 = []
Gone2 = []
#Board 1 und Board 2 für Spieler 1 und Spieler 2
Board1, Board2 = [[space] * boardSize for i in range(boardSize)], \
                 [[space] * boardSize for i in range(boardSize)]

#Boards für Abgeschlossene versuche
Guess1, Guess2 = [[space] * boardSize for i in range(boardSize)], \
                 [[space] * boardSize for i in range(boardSize)]

#Schiffe mit dazugehörigen Längen
ships = {"Ship1": 5,
         "Ship2": 4,
         "Ship3": 3,
         "Ship4": 2}

#Schiffe mit dazugehörige Anzahl
shipcount = {"Ship1": 1,
             "Ship2": 2,
             "Ship3": 3,
             "Ship4": 4}

#Spieler Profil, alle Werte zuweisen.
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

#Bildschirm leeren mit Leerzeilen
def clearscreen():
    for i in range(50):
        print("")

clearscreen()

#Board in richtiger Formatierung ausgeben.
def print_grid(Board):
    # Buchstaben Notation als Spalte
    sys.stdout.write("  ")
    for i in range(boardSize):
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


#Schiffe Platzieren
def placeship(Board,Gone,Name):
    print(Name+",","Bitte Platziere deine Schiffe")
    print_grid(Board)
    #Board um Später Kooardinaten gültiger versuche zu bekommen bevor man ins richtige Board einsetzt
    board3 = [[space] * boardSize for i in range(boardSize)]
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
                                for i in range(boardSize):
                                    if Zeile == i:
                                        zustand = False
                                        break
                            break
                        except ValueError:
                            print("Falsche Eingabe")#falsche Eingaben abfangen
                    zustand = True
                    while zustand:
                        print("Welche Spalte soll das", j + 1, "te Schlachtschiff gesetzt werden")
                        Spalte = (input("Spalte"))
                        for i in range(boardSize):
                            if Spalte == chr(i + 65):
                                zustand = False
                                break

                    break

                while True:
                    try:
                        ShipPosition = int(input("0 für Horizontal und 1 für Vertikal"))
                        if ShipPosition != 1 and ShipPosition != 0:
                            raise Exception
                        break
                    except Exception:
                        print("Keine Zulässige eingabe, nochmal eingeben")#Falsche eingabe Abfangen

                for i in range(ships["Ship1"]):

                    if ShipPosition == 0:
                        board3[Zeile][(i + ord(Spalte)) - 65] = "s"




                    else:
                        board3[i + Zeile][ord(Spalte) - 65] = "s"
                break
            except IndexError:
                print("Kein Platz")#Platzierung Außerhalb des Boardes abfangen
                board3.clear()
                board3 = [[space] * boardSize for i in range(boardSize)]
        #die Koordinaten von den platzierten schiffteilen auf board3 abspeichern
        safe = [(ix, iy) for ix, row in enumerate(board3) for iy, i in enumerate(row) if i == "s"]
        #board3 für weiteren verlauf resetten, für mehrere schiffe des selben typs.
        board3.clear()
        board3 = [[space] * boardSize for i in range(boardSize)]
        for p in safe:
            #überprüfen ob Koordinaten von platzierten schiffen in liste Gone existiert
            a = any(p in sublist for sublist in Gone)
            #falls schon in Gone existiert, dann nicht auf dem echten Board nochmal setzen da schon vorhanden
            if a == True:
                print("Geht nicht")
                break
        if a == False:
            #Falls noch nicht existiert, dann auf dem echten Board setzen
            for i in range(ships["Ship1"]):
                if ShipPosition == 0:
                    Board[Zeile][(i + ord(Spalte)) - 65] = "s"

                else:
                    Board[i + Zeile][ord(Spalte) - 65] = "s"

        if any(p in sublist for sublist in Gone) == False:
            #In Gone die Koordinaten vom neu gesetzen Schiff abspeichern umd später Überlappung zu vermeiden.
            Gone.append(safe)
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
                                        print("Welche Zeile soll der", j + 1, "te Kreuzer gesetzt werden")
                                        Zeile = int(input("Zeile")) - 1
                                        for i in range(boardSize):
                                            if Zeile == i:
                                                zustand = False
                                                break
                                    break
                                except ValueError:
                                    print("Falsche Eingabe")#Falsche Eingabe abfangen
                            zustand = True
                            while zustand:
                                print("Welche Spalte soll der", j + 1, "te Kreuzer gesetzt werden")
                                Spalte = (input("Spalte"))
                                for i in range(boardSize):
                                    if Spalte == chr(i + 65):
                                        zustand = False
                                        break

                            break

                        while True:
                            try:
                                ShipPosition = int(input("0 für Horizontal und 1 für Vertikal"))
                                if ShipPosition != 1 and ShipPosition != 0:
                                    raise Exception
                                break
                            except Exception:
                                print("Keine Zulässige eingabe, nochmal eingeben")#Falsche Eingabe Abfangen

                        for i in range(ships["Ship2"]):

                            if ShipPosition == 0:
                                board3[Zeile][(i + ord(Spalte)) - 65] = "k"




                            else:
                                board3[i + Zeile][ord(Spalte) - 65] = "k"
                        break
                    except IndexError:
                        print("Kein Platz")#Platzierung Außerhalb Board abfangen
                        board3.clear()
                        board3 = [[space] * boardSize for i in range(boardSize)]

                safe = [(ix, iy) for ix, row in enumerate(board3) for iy, i in enumerate(row) if i == "k"]
                board3.clear()
                board3 = [[space] * boardSize for i in range(boardSize)]
                for p in safe:
                    a = any(p in sublist for sublist in Gone)
                    if a == True:
                        raise Exception
                break
            except Exception:
                print("Nochmal eingeben")#Überlappung Abfangen

        if a == False:
            for i in range(ships["Ship2"]):
                if ShipPosition == 0:
                    Board[Zeile][(i + ord(Spalte)) - 65] = "k"

                else:
                    Board[i + Zeile][ord(Spalte) - 65] = "k"

        if any(p in sublist for sublist in Gone) == False:
            Gone.append(safe)
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
                                        print("Welche Zeile soll der", j + 1, "te Zerstörer gesetzt werden")
                                        Zeile = int(input("Zeile")) - 1
                                        for i in range(boardSize):
                                            if Zeile == i:
                                                zustand = False
                                                break
                                    break
                                except ValueError:
                                    print("Falsche Eingabe")#Falsche Eingabe Abfangen
                            zustand = True
                            while zustand:
                                print("Welche Spalte soll der", j + 1, "te Zerstörer gesetzt werden")
                                Spalte = (input("Spalte"))
                                for i in range(boardSize):
                                    if Spalte == chr(i + 65):
                                        zustand = False
                                        break

                            break

                        while True:
                            try:
                                ShipPosition = int(input("0 für Horizontal und 1 für Vertikal"))
                                if ShipPosition != 1 and ShipPosition != 0:
                                    raise Exception
                                break
                            except Exception:
                                print("Keine Zulässige eingabe, nochmal eingeben")#Falsche Eingabe Abfangen

                        for i in range(ships["Ship3"]):

                            if ShipPosition == 0:
                                board3[Zeile][(i + ord(Spalte)) - 65] = "z"




                            else:
                                board3[i + Zeile][ord(Spalte) - 65] = "z"
                        break
                    except IndexError:
                        print("Kein Platz")#Platzierung außerhalb Board abfangen
                        board3.clear()
                        board3 = [[space] * boardSize for i in range(boardSize)]

                safe = [(ix, iy) for ix, row in enumerate(board3) for iy, i in enumerate(row) if i == "z"]
                board3.clear()
                board3 = [[space] * boardSize for i in range(boardSize)]
                for p in safe:
                    a = any(p in sublist for sublist in Gone)
                    if a == True:
                        raise Exception
                break
            except Exception:
                print("Nochmal eingeben")#Überlappung abfangen

        if a == False:
            for i in range(ships["Ship3"]):
                if ShipPosition == 0:
                    Board[Zeile][(i + ord(Spalte)) - 65] = "z"

                else:
                    Board[i + Zeile][ord(Spalte) - 65] = "z"

        if any(p in sublist for sublist in Gone) == False:
            Gone.append(safe)
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
                                        print("Welche Zeile soll das", j + 1, "te UBoot gesetzt werden")
                                        Zeile = int(input("Zeile")) - 1
                                        for i in range(boardSize):
                                            if Zeile == i:
                                                zustand = False
                                                break
                                    break
                                except ValueError:
                                    print("Falsche Eingabe")#Falsche Eingabe abfangen
                            zustand = True
                            while zustand:
                                print("Welche Spalte soll das", j + 1, "te UBoot gesetzt werden")
                                Spalte = (input("Spalte"))
                                for i in range(boardSize):
                                    if Spalte == chr(i + 65):
                                        zustand = False
                                        break

                            break

                        while True:
                            try:
                                ShipPosition = int(input("0 für Horizontal und 1 für Vertikal"))
                                if ShipPosition != 1 and ShipPosition != 0:
                                    raise Exception
                                break
                            except Exception:
                                print("Keine Zulässige eingabe, nochmal eingeben")#falsche Eingabe abfangen

                        for i in range(ships["Ship4"]):

                            if ShipPosition == 0:
                                board3[Zeile][(i + ord(Spalte)) - 65] = "u"




                            else:
                                board3[i + Zeile][ord(Spalte) - 65] = "u"
                        break
                    except IndexError:
                        print("Kein Platz")#Platzierung außerhalb Board abfangen
                        board3.clear()
                        board3 = [[space] * boardSize for i in range(boardSize)]

                safe = [(ix, iy) for ix, row in enumerate(board3) for iy, i in enumerate(row) if i == "u"]
                board3.clear()
                board3 = [[space] * boardSize for i in range(boardSize)]
                for p in safe:
                    a = any(p in sublist for sublist in Gone)
                    if a == True:
                        raise Exception
                break
            except Exception:
                print("Nochmal eingeben")#Überlappung abfangen

        if a == False:
            for i in range(ships["Ship4"]):
                if ShipPosition == 0:
                    Board[Zeile][(i + ord(Spalte)) - 65] = "u"

                else:
                    Board[i + Zeile][ord(Spalte) - 65] = "u"

        if any(p in sublist for sublist in Gone) == False:
            Gone.append(safe)
        print_grid(Board)






#placeship(Board1)
#print_grid(Board1)

def attack(Board,Guess,Name,Gone):

    print(Name,"ist dran, bitte Bildschirm übergeben")
    input(Name+", Bitte Enter drücken \n")
    #Richtige Board zuordnung für Spieler
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
                            Zeile = int(input("Zeile")) - 1
                            for i in range(boardSize):
                                if Zeile == i:
                                    zustand = False
                                    break
                        break
                    except ValueError:
                        print("Falsche Eingabe")
                zustand = True
                while zustand:
                    print("Welche Spalte willst du attackieren?")
                    Spalte = (input("Spalte"))
                    for i in range(boardSize):
                        if Spalte == chr(i + 65):
                            zustand = False
                            break

                break
            if Guess[Zeile][(ord(Spalte)) - 65] == "x" or Guess[Zeile][(ord(Spalte)) - 65] == "0":
                raise Exception
            break
        except Exception:
            print("Dieses Feld wurde schon überprüft nach Schiffen")#Falls schon überprüft, abfangen
            print("Bitte ein anderes Feld eingeben")
    Gone3 = []
    #falls im Board ein Schiff Platziert wurde
    if(Board[Zeile][(ord(Spalte)) - 65]) != " ":
        Guess[Zeile][(ord(Spalte)) - 65]="x"
        #Koordinaten speichern von getroffenen Schiffen
        shot = ([(ix, iy) for ix, row in enumerate(Guess) for iy, i in enumerate(row) if i == "x"])
        for p in shot:
            #Wenn die Koordinaten vom getroffenen Schiff in Gone Existieren
            b=any(p in sublist for sublist in Gone)
            if b==True:
                #Von Gone diese Koordinate entfernen, da dieses Schiffsteil getroffen wurde
                Gone = [list(tuple(ele for ele in sub if ele != p)) for sub in Gone]
        #Wenn alle Schiffsteile von einem Schiff entfernt wurden, ist das Schiff Zerstört
        for i in range(10):
            if i==0:
                if Gone[i] == []:
                    Gone3.append("Schlachtschiff Zerstört")

            if i==1 or i==2:
                if Gone[i] == []:
                    Gone3.append("Kreuzer Zerstört")
            if i==3 or i==4 or i==5:
                if Gone[i] == []:
                    Gone3.append("Zerstörer Zerstört")
            if i==6 or i==7 or i==8 or i==9:
                if Gone[i] == []:
                    Gone3.append("UBoot Zerstört")

        #Wenn noch kein Schiff Zerstört wurde
        if Gone3 == []:
            print("Bis jetzt keine Schiffe Zerstört")
        else:
            print(Gone3)
    #Wenn in Board kein Schiff eingetragen wurde, in Guess als Fehlschuss markieren
    if (Board[Zeile][(ord(Spalte)) - 65]) == " ":
        Guess[Zeile][(ord(Spalte)) - 65] = "0"
        print("Fehlschuss")
    #Richtige Zuordnung von Spieler Board und Guess Board
    if Board==Board1:
        print_grid(Board2)
        print_grid(Guess)
    elif Board==Board2:
        print_grid(Board1)
        print_grid(Guess)
    #Wenn alle Schiffe Zerstört wurden, endet das Spiel
    if Gone[0] == [] and Gone[1] == [] and Gone[2] == [] and Gone[3] == [] and Gone[4] == [] and Gone[5] == []\
            and Gone[6] == [] and Gone[7] == [] and Gone[8] == [] and Gone[9] == []:
        sys.exit("Game Over"+" "+Name+" "+"hat Gewonnen")


placeship(Board1,Gone1,Name1)
input("Bitte drücke Enter und Übergebe Dannach die Kontrolle den anderen Spieler")
clearscreen()
placeship(Board2,Gone2,Name2)
input("Bitte drücke Enter um das Spiel zu Starten")
clearscreen()

while True:
    attack(Board2,Guess1,Name1,Gone2)#spieler1
    input("")
    clearscreen()
    attack(Board1,Guess2,Name2,Gone1)#spieler2
    input("")
    clearscreen()

