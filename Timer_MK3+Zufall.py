#Importe
import sys
import time
import threading
from threading import Thread
import random


class bcolors:
    END = '\033[91m'                        #Text wird in Rot geaendert
    HIT = '\033[92m'                        #Text wird in Grün geandert
    RESET = '\033[0m'                       #Farbwechsel wird rueckgaengig gemacht
exit_event = threading.Event()

spielfeldgröße = 8-1                        #groeße des Spielfeldes, zur veranschaulichung vorgegeben

def schuss():
    thread_1 = Thread(target=timer)         #Erster Thread wird erstellt
    thread_1.start()                        #Thread wird gestartet
    time.sleep(0.25)                        #wartet 0.5 Sekunden (schönere ausgabe)
    while True:
        schuss = input("Wo möchten sie hinschißen?\n")

        try:
            #Eingabe passt
            int(schuss)
            exit_event.set()                    #Event wird gesetzt, um den timer zu stopen
            print("Timer Stop")
            break

        except ValueError:
                                                #Eingabe passt nicht
            print("Falsche eingabe!")
            print("Timer läuft weiter:")

def zufall():
    list1=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i','j','k','l']      #Liste der Spalten
    list2=[1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12]                           #Liste der Zeilen
    b=random.randint(0,spielfeldgröße)
    a=random.randint(0,spielfeldgröße)


    zeile = list2[b]
    spalte = list1[a]
    #print("Es wird auf Zeile:" , zeile , "geschossen")
    #print("Es wird auf Spalte:" , spalte , "geschossen")
    print("Es wird auf die Kordinate:"+bcolors.HIT+str(zeile)+spalte+bcolors.RESET+" geschossen" )


def timer():
    t =15             #t Sekunden Zeit
    print("Sie haben ", t ," Sekunden Zeit")
    time.sleep(0.5)                        #Programm warte 0,5 Sekunden
    while t:
        minuten = t // 60
        sekunden = t % 60
        timer = '{:02d}:{:02d}'.format(minuten, sekunden)
        print("--> " + timer, end=" ")
        time.sleep(1)                      #Programm wartet 1 Sekunde
        t -= 1
        if exit_event.is_set():            #bei event wird der timer gestopt (schleife unterbrochen)
            break
    if t == 0:
        print("-->" + bcolors.END + " 00:00" + bcolors.RESET)   #Der Text "00:00" wird in Rot geaendert.
        print("Ihre Zeit ist abgelaufen!")
        zufall()

schuss()