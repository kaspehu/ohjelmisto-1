
import random

def nopanheitto():
    while True:
        nopanheitto = random.randint(1, 6)
        if nopanheitto != 6:
            print(f"Heitit: {nopanheitto}")
        else:
            print(f"Heitit: {nopanheitto}, onneksi olkoon!")
            return

print(nopanheitto())