import sys
#Namensgebung
#while True:
#   playerOne = input('Name Player 1:')
#   if len(playerOne) > 10:
#      print('Try Again')
#   else:
#       break
#while True:
#   playerTwo = input('Name Player 2:')
#   if len(playerTwo) <= 10 and playerTwo != playerOne:
#       break
#   else:
#        print('Try Again')

#Spielfelderstellung (iedeer auf 0 setzen nach Auskommentierung
spielfeldgröße = 8

#while not (8 <= spielfeldgröße <= 12):
 #   spielfeldgröße = int(input('Bitte geben Sie die gewünschte Spielfeldgröße ein (AxA).'))
  #  if 12 < spielfeldgröße or spielfeldgröße < 8:
   #     print('Spielfeldgröße nicht nicht akzeptiert.')
    #else:
     #   continue
space=" "
hit="X"
miss="O"
ship="*"

#Ausgabe der x-Achsenbeschriftung

board = [[space] * spielfeldgröße for i in range(spielfeldgröße)]
def print_grid(board):
    sys.stdout.write("  ")
    for i in range(spielfeldgröße):
        sys.stdout.write(" " + chr(i + 65))
    print(" ")
    row_number = 1
    for row in board:
        if row_number<10:
            grid=("%d |%s|" % (row_number,"|".join(row)))
        else:
            grid = ("%d|%s|" % (row_number, "|".join(row)))
        print(grid)
        row_number += 1

print_grid(board)
#TrefferQuoten:
#8x8: 30/64 9x9: 30/81 10x10: 30/100 11x11: 30/121 12x12 30/144
schiffe=["Schlachtschiff","Kreuzer","Zerstörer","UBoot"]

schiffgröße={"Schlachtschiff":5,"Kreuzer":4,"Zerstörer":3,"UBoot":2}
# Anzahl Schiffe
ships={"Schlachtschiff":1, "Kreuzer":2, "Zerstörer":3, "UBoot":4}

def place_ship():

            ShipPosition = int(input("0 für Horizontal und 1 für Vertikal"))

            if ShipPosition == 0:
                zustand=True
                while zustand:
                    Zeile = int(input("Zeile:"))
                    for k in range(spielfeldgröße):
                        if Zeile == k + 1:
                            zustand=False
                            break
                        else:
                            print("Eingabe nicht zuläsig")
                while True:
                    Spalte = input("Spalte:")
                    if (ord(Spalte)-65) <= spielfeldgröße-schiffgröße["Schlachtschiff"]:
                        False
                        break
                    else:
                        print("Eingabe nicht zuläsig")

                for k in range(schiffgröße["Schlachtschiff"]):
                    board[Zeile-1][k+(ord(Spalte)) - 65]=ship
                print_grid(board)

            else:

                while True:
                    Spalte= input("Spalte:")
                    for i in range(spielfeldgröße):
                        if Spalte == chr(i + 65):
                            False
                            break
                        else:
                            print("Eingabe nicht zuläsig")
                while True:
                    Zeile=int(input("Zeile:"))
                    if Zeile <= spielfeldgröße-schiffgröße["Schlachtschiff"]:
                        False
                        break
                    else:
                        print("Eingabe nicht zuläsig")

                for k in schiffgröße:
                    board[k+Zeile - 1][(ord(Spalte)) - 65] = ship

                print_grid(board)

place_ship()

# #Eingabe Spalte zulässig ja/nein
# while True:
#     zustand=True
#     while zustand:
#         spalte=input("Spalte:")
#         for i in range(spielfeldgröße):
#             if spalte == chr(i + 65):
#                 zustand=False
#                 break
#     zustand=True
#     while zustand:
#         zeile=int(input("Zeile:"))
#         for i in range(spielfeldgröße):
#             if zeile == i+1:
#                 zustand=False
#                 break
#
#
# #if schiff!=spalte/zeile
#     board[Zeile-1][(ord(Spalte))-65]= miss
#     print("Schuss ins Leere")
#     print_grid(board)
#     break
# # if schiff==spalte/zeile
#    # board[[(ord(spalte))-65]*zeile]= hit
#     #print("Sie haben ein Schiff getroffen")
#     #print_grid(board)

