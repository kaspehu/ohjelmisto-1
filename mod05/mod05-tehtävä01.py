
import random

n = int(input("Syötä arpakuutioiden määrä: "))
heitot = []
total = 0

for i in range(n):
    heitto = random.randint(1,6)
    print(f"Heitit: {heitto}")
    total += heitto

print(f"Arpakuutioiden yhteistulos: {total}")




