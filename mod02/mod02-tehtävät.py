#mod02 tehtäväratkaisuja

# 2. Muuttujat ja vuorovaikutteiset ohjelmat

# Tehtävä 1.

nimi = input("Hei,anna nimesi: ") #kysytään käyttäjältä nimi

tervehdys = "Hei, " + nimi + "!\n" #määritetään tervehdys

print(tervehdys) #ohjelma tervehtii


# Tehtävä 2.

import math # Tuodaan kirjasto "math" pi:n arvoa varten

sade = float(input("Hei, syötä ympyrän säde: ")) #Kysytään käyttäjältä ympyrän säde

ympyran_pinta_ala = math.pi * sade ** 2 #määritetään ympyrän pinta-ala

print(f"Ympyrän pinta-ala on: {ympyran_pinta_ala:.2f}\n") #tulostetaan vastaus


# Tehtävä 3.

kanta = float(input("Hei, syötä suorakulmion kanta: ")) # Kysytään käyttäjältä suorakulmion kanta
korkeus = float(input("Ja korkeus myös kiitos: ")) # Kysytään myös korkeus

nelion_piiri = 2 * kanta + 2 * korkeus # Määritetään piiri
nelion_pinta_ala = kanta * korkeus # Määritetään pinta-ala

print(f"Nelion piiri on : {nelion_piiri:.2f}") # Tulostetaan piiri
print(f"Neliön pinta-ala on: {nelion_pinta_ala:.2f}\n") # Tulostetaan pinta-ala

# Tehtävä 4.

# Kysytään käyttäjältä luvut
luku1 = float(input("Hei, syötä luku: "))
luku2 = float(input("Syötä toinen luku: "))
luku3 = float(input("Ja kolmas luku: "))

# Määritetään eri tulokset
summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = (luku1 + luku2 + luku3) / 3

# tulostetaan kyseiset tulokset
print(f"Lukujen summa on: {summa:.2f}")
print(f"Lukujen tulo on: {tulo:.2f}")
print(f"Lukujen keskiarvo on: {keskiarvo:.2f}\n")

# Tehtävä 5.

# Määritetään numeraaliset arvot tehtävänannon mukaisesti
gramma = 1
kilogramma = gramma * 1000
luoti = gramma * 13.3
naula = luoti * 20
leiviska = naula * 20

# Kysytään käyttäjältä luvut
luku_1 = float(input("Anna leiviskät: "))
luku_2 = float(input("Anna naulat: "))
luku_3 = float(input("Anna luodit: "))

# Määritetään tulostettavat printit ja erotetaan grammat ja kilogrammat
kokonaistulos = (luku_1 * leiviska) + (luku_2 * naula) + (luku_3 * luoti)
kilogrammat = int(kokonaistulos // kilogramma)
grammat = kokonaistulos % kilogramma

# Printataan pyydetyt arvot
print(f"Massa nykymittojen mukaan:\n{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.\n")

# Tehtävä 6.

import random # Tuodaan "random" lukujen arpomista varten

# Määritetään satunnaisten lukujen arpojat
random_number1= random.randint(0, 9)
random_number2 = random.randint(0, 9)
random_number3 = random.randint(0, 9)
random_number4 = random.randint(1, 6)
random_number5 = random.randint(1, 6)
random_number6 = random.randint(1, 6)
random_number7 = random.randint(1, 6)

# Ohjelma syöttää kolmi- ja nelinumeroisen luvun
print(f"Kolminumeroinen koodi: {random_number1}{random_number2}{random_number3}")
print(f"Nelinumeroinen koodi: {random_number4}{random_number5}{random_number6}{random_number7}")


















