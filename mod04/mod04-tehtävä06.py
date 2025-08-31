import random
# Kaikkien pisteiden määrä N
N = int(input("Syötä pisteiden määrä (mitä isompi luku, sen tarkempi): "))
# Ympyrän sisään osuvien pisteiden lkm n
n = 0
i = 0

while i < N: # ohjelma suoriutuu käyttäjän syöttämän lukumäärän mukaan
    i += 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:  # Yhtälö x^2 + y^2 < 1
        n += 1  # kasvatetaan sisään osuvien pisteiden lukumäärää yhtälön toteutuessa

pi_likiarvo = 4*n / N # Tehtävänannosta saatu yhtälö pi:n likiarvolle π≈4n/N
print(f"pi:n likiarvo on: {pi_likiarvo:.4f}")








