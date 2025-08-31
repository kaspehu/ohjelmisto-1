# Tehtävä 1.

# Määritetään luvut
suurin_luku = 1000
kasvava_luku = 0

while kasvava_luku < suurin_luku:
    kasvava_luku += 1
    if kasvava_luku % 3 == 0: # Ohjelma laskee kolmella jaolliset numerot ja tulostaa ne
        print(f"{kasvava_luku},")


# Tehtävä 2.

app_running = True

while app_running:
    command = float(input("Syötä tuuma: "))
    if command >= 0: # Pyydetään käyttäjältä tuumat
        print(f"Tuumat senttimetreinä {command * 2.54:.2f}") # Muunnetaan tuumat senttimetreiksi
    elif command < 0: # Ohjelma sulkeutuu jos tulos on negatiivinen
        print("Negatiivinen luku, ohjelma sulkeutuu.")
        app_running = False