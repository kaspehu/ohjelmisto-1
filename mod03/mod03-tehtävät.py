# Tehtävät; 3. Valinta rakenne if:

# Tehtävä 1.

input_kuhan_pituus = float(input("Kuhan pituus: ")) #Kysytään kuhan pituus

# Määritetään ehdot ja tulostukset syötön perusteella
if input_kuhan_pituus >= 37:
    print(f"Kuhan pituus on: {input_kuhan_pituus:.2f}""cm\n")
else:
    print(f"Laske kuha vapaaksi, sen pituudesta puuttuu: {37 - input_kuhan_pituus:.2f}""cm\n")

# Tehtävä 2.

# Kysytään käyttäjältä hytin luokka
input_hytin_luokka = input("Syötä laivan hyttiluokka (A, B, C tai LUX): ")

# Määritetään vastauksen mukaan määriytyvät vastaukset
if input_hytin_luokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.\n")
elif input_hytin_luokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.\n")
elif input_hytin_luokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.\n")
elif input_hytin_luokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.\n")
else:
    print("Virheellinen hyttiluokka.\n")

# Tehtävä 3.

# Kysytään sukupuoli
input_sukupuoli = input("Nainen vai mies: ")

# Määritetään hemoglobiiniarvot ja vastaukset käyttäjän syötteen perusteella
if input_sukupuoli == "Nainen" or "nainen":
    naisen_hemoglobiiniarvo = float(input("Syötä hemoglobiinarvo: "))
    if naisen_hemoglobiiniarvo < 117:
        print("Alhainen hemoglobiini\n")
    elif naisen_hemoglobiiniarvo > 175:
        print("Korkea hemoglobiini\n")
    else:
        print("Normaali hemoglobiini\n")

elif input_sukupuoli == "Mies" or "mies":
    miehen_hemoglobiiniarvo = float(input("Syötä hemoglobiinarvo: "))
    if miehen_hemoglobiiniarvo < 134:
        print("Alhainen hemoglobiini\n")
    elif miehen_hemoglobiiniarvo > 195:
        print("Korkea hemoglobiini\n")
    else:
        print("Normaali hemoglobiini\n")

# Tehtävä 4.

# Kysytään vuosiluku
input_vuosiluku = int(input("Syötä vuosiluku: "))

# Määritetään jakojäännöksellä neljällä jaolliset luvut
if input_vuosiluku % 4 == 0:
    print("Vuosi on karkausvuosi: ")
else:
    print("Vuosi ei ole karkausvuosi: ")


