import random

def nopanheitto(tahkot):
    while True:
        nopanheitto = random.randint(1, tahkot)
        if nopanheitto != tahkot:
            print(f"Heitit: {nopanheitto}")
        else:
            print(f"Heitit: {nopanheitto}, onneksi olkoon!")
            return

print(nopanheitto(int(input("Tahkot: "))))
