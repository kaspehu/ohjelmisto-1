# Tehtävä 3.

app_running = True

luku = [] # Määritetään tyhjä lista myöhempää varten

while app_running:
    user_input = input("Anna kokonaisluku tai lopeta painamalla enter: ")
    if user_input.isdigit():
        number = int(user_input)
        luku.append(number) # Määritetään "luvulle" arvo käyttäjän syöttämän luvun mukaan
    elif user_input == "": # Ohjelma printtaa luvut painettaessa enter
        print(f"Suurin syötetty luku: {max(luku)} ja pienin syötetty luku {min(luku)}")
        app_running = False
    else:
        print("Et syöttänyt kokonaislukua:")
