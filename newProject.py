import sys
#Namensgebung
while True:
    playerOne = input('Name Player 1:')
    if len(playerOne) > 10:
        print('Try Again')
    else:
        break
while True:
    playerTwo = input('Name Player 2:')
    if len(playerTwo) <= 10 and playerTwo != playerOne:
        break
    else:
        print('Try Again')

#Spielfelderstellung
spielfeldgröße = 0

while not (8 < spielfeldgröße < 12):
    spielfeldgröße = int(input('Bitte geben Sie die gewünschte Spielfeldgröße ein (AxA).'))
    if 12 < spielfeldgröße or spielfeldgröße < 8:
        print('Spielfeldgröße nicht nicht akzeptiert.')
    else:
        continue
space=" "
hit="X"
miss="O"
ship="*"

#Ausgabe der x-Achsenbeschriftung
sys.stdout.write ("  ")
for i in range(spielfeldgröße):
    sys.stdout.write (" "+chr(i+65))
print(" ")
board = [[space] * spielfeldgröße for i in range(spielfeldgröße)]
def print_grid(board):
    row_number = 1
    for row in board:
        if row_number<10:
            grid=("%d |%s|" % (row_number,"|".join(row)))
        else:
            grid = ("%d|%s|" % (row_number, "|".join(row)))
        print(grid)
        row_number += 1

print_grid(board)

#Eingabe Spalte zulässig ja/nein
while True:
    zustand=True
    while zustand:
        spalte=input("Spalte:")
        for i in range(spielfeldgröße):
            if spalte == chr(i + 65):
                zustand=False
                break
    zustand=True
    while zustand:
        zeile=int(input("Zeile:"))
        for i in range(spielfeldgröße-1):
            if zeile == i:
                zustand=False
                break
#if schiff!=spalte/zeile
    board[zeile-1][(ord(spalte))-65] = miss
    print("Schuss ins Leere")
    print_grid(board)
    break
# if schiff==spalte/zeile
    board[zeile-1][(ord(spalte))-65]= hit
    print("Sie haben ein Schiff getroffen")
    print_grid(board)

