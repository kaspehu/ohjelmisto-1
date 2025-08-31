# Tehtävä 5.


# Määritetään oikea salasana, käyttäjä ja saillittujen yritysten määrä
user = "python"
password = "rules"
max_attempts = 5
attempt = 0

# yritysten alittaessa maksimiyritykset, kysytään käyttäjää ja salasanaa
while app_running and attempt < max_attempts:
    input_user = input("Käyttäjänimi: ")
    input_pass = input("Salasana: ")
    if input_user == "python" and input_pass == "rules":
        print("Tervetuloa!") # Jos oikein, ohjelma tervehtii ja sulkeutuu
        app_running = False
    else:
        attempt += 1
if attempt == max_attempts: # kun yritysten määrä täyttyy, ohjelma myös sulkeutuu
    print("Pääsy evätty")
    app_running = False
