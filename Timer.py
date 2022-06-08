#importe
import threading
import time
from threading import Thread


exit_event = threading.Event()

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
# Thread 2 wird beendet
    exit_event.set()
    print("Ihre Zeit ist abgelaufen!")


thread_1 = Thread(target=timer)
thread_1.start()

def randomehit():
    print("Zufallsschuss!")

if exit_event.is_set():
    randomehit()


def schleife():
    for i in range(1,100):
        time.sleep(1)
        print(i)
        if exit_event.is_set():
            break

thread_2 = Thread(target=schleife)
thread_2.start()


