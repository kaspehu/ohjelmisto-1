

vuodenajat = ("talvi",
              "talvi",
              "kevät",
              "kevät",
              "kevät",
              "kesä",
              "kesä",
              "kesä",
              "syksy",
              "syksy",
              "syksy",
              "talvi",)

knro = int(input("Syötä kuukauden numero (1-12): "))
# jos numero on 1 ja 12 väliltä
if 1 <= knro <= 12:
    # printtaa kuukausi
    print(vuodenajat[knro-1])
else:
    print("Virheellinen kuukausi!")