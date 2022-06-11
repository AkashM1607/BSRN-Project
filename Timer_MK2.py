#Importe
import sys
import time
import threading
from threading import Thread

exit_event = threading.Event()

def schuss():
    thread_1 = Thread(target=timer)         #Erster Thread wird erstellt
    thread_1.start()                        #Thread wird gestartet
    time.sleep(0.5)                         #wartet 0.5 Sekunden (schönere ausgabe)
    schuss = input("Wo möchten sie hinschießen?")
    print(schuss)
    try:
        #Eingabe passt
        int(schuss)
        print("Timer Stop")
        exit_event.set()                    #Event wird gesetzt, um den timer zu stopen
    except ValueError:
        #Eingabe passt nicht
        print("timer läuft weiter")





#Muss eröfnet werden und wieder gelossen
def timer():
    t =25             #t Sekunden Zeit
    print("Sie haben ", t ," Sekunden Zeit")
    while t:
        minuten = t // 60
        sekunden = t % 60
        timer = '{:02d}:{:02d}'.format(minuten, sekunden)
       #print(timer, end="\r")   #time wird ausgegeben und dann mit der neunen time überschrieben
        time.sleep(1)
        t -= 1
        if exit_event.is_set():            #bei event wird der timer gestopt (schleife unterbrochen)
            break
    if t == 0:
        #Timer ist abgelaufen, Zufallsschuss kann gesetzt werden
        print("Ihre Zeit ist abgelaufen!")
        print("Zufallsschuss!")

schuss()


