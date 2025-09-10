icao_list = {"EFHK": "Helsinki",
                "EFKT": "Kittilä"}

kysy = True

while kysy:
    cmd = input("Haluatko syöttää uuden lentoaseman (U), hakea jo syötetyn lentoaseman (H) vai lopettaa (L): ").lower()
    if cmd == "u":
        print("Lisätään uusi kenttä")
        icao = input("Anna ICAO-koodi: ").upper()
        nimi = input("Anna lentokentän nimi: ")
        icao_list[icao] = nimi
        print("Lentokenttä lisätty.", icao_list)
    elif cmd == "h":
        print("Haetaan lentokenttä")
        icao = input("Anna ICAO-koodi mitä haetaan (EHKF): ").upper()
        if icao in icao_list:
            print(f"Haulla {icao} löytyi lentokenttä: ", icao_list[icao])
    elif cmd == "l":
        print("Lopetetaan")
        kysy = False
    else:
        print("Virheellinen syöte, yritä uudelleen.")