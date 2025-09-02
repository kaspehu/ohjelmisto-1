
luku = int(input("Anna kokonaisluku, tarkistetaan onko alkuluku: "))
jaollinen = []

# oletusarvo on että luku on alkuluku, todennetaan tämä jakamalla
onko_alkuluku = True

for i in range(2, luku):
    if luku % i == 0:
        onko_alkuluku = False
        jaollinen.append(i)

if onko_alkuluku:
    print(f"{luku} on alkuluku.")
else:
    print(f"{luku} ei ole alkuluku")
    print(jaollinen)
