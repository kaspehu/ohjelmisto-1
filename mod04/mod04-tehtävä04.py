# Tehtävä 4.

import random

app_running = True
satunnaisluku = random.randint(1,10) # ohjelma arpoo luvun väliltä 1-10
luku_valilta_1_10 = int(input("Syötä luku väliltä 1-10: "))

while app_running:
    while luku_valilta_1_10 < satunnaisluku: # luku alle satunnaisluvun, kysytään uudestaan
        print("liian pieni luku")
        luku_valilta_1_10 = int(input("Syötä luku väliltä 1-10: "))
    while luku_valilta_1_10 > satunnaisluku: # luku yli satunnaisluvun, kysytään uudestaan
        print("liian suuri luku")
        luku_valilta_1_10 = int(input("Syötä luku väliltä 1-10: "))
    if luku_valilta_1_10 == satunnaisluku: # luku yhtä suuri kuin satunnaisluku, ohjelma sulkeutuu
        print("Oikea luku!")
        app_running = False