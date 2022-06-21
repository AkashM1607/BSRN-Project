import random
spielfeldgröße = 8-1

def zufall():
    list1=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i','j','k','l']
    list2=[1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12]
    b=random.randint(0,spielfeldgröße)
    a=random.randint(0,spielfeldgröße)


    zeile = list2[b]
    spalte = list1[a]
    print(zeile)
    print(spalte)


eingabe =1
if eingabe == 1:
    zufall()
else:
    print("ups")


