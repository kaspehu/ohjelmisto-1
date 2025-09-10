nimet = set()

while True:
    nimi = input("Syötä nimi: ")
    if nimi == "":
        break
    elif nimi in nimet:
        print(f"{nimi} löytyy jo listalta.")
    else:
        nimet.add(nimi)
        print(f"Uusi nimi, {nimi} lisätty listaan.")

print("Nimilista: ")
for n in nimet:
    print(n)
