
import math

def pizza(hinta, halkaisija):
    säde = (halkaisija * 0.01) / 2
    pinta_ala = math.pi * (säde ** 2)
    tulos = hinta / pinta_ala
    return tulos

pizza1hinta = float(input("Syötä pizzan 1 hinta euroina: "))
pizza1halk = float(input("Syötä pizzan 1 halkaisija senttimetreinä: "))
pizza2hinta = float(input("Syötä pizzan 2 hinta euroina: "))
pizza2halk = float(input("Syötä pizzan 2 halkaisija senttimetreinä: "))

if pizza1hinta / pizza1halk < pizza2hinta / pizza2halk:
    yksikkohinta = pizza(pizza1hinta, pizza1halk)
    yksikkohinta2 = pizza(pizza2hinta, pizza2halk)
    print(f"Pizzan 2 yksikköhinta on {yksikkohinta:.2f} €/m^2 ja se on parempi vastine rahalle.")
    print(f"Pizzan 1 yksikköhinta: {yksikkohinta2:.2f} €/m^2.")
elif pizza1hinta / pizza1halk > pizza2hinta / pizza2halk:
    yksikkohinta = pizza(pizza2hinta, pizza2halk)
    yksikkohinta2 = pizza(pizza1hinta, pizza1halk)
    print(f"Pizzan 1 yksikköhinta on {yksikkohinta:.2f} €/m^2 ja se on parempi vastine rahalle.")
    print(f"Pizzan 2 yksikköhinta: {yksikkohinta2:.2f} €/m^2.")