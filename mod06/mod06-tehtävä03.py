
def bensamuunnos(gallonat):
    return gallonat * 3.785

while True:
    gallonat = float(input("Syötä bensiinin määrä nestegallonoina, negatiivinen luku lopettaa: "))
    if gallonat < 0:
        break
    elif gallonat >= 0:
        litrat = bensamuunnos(gallonat)
        print(f"Bensiinin määrä litroina: {litrat:.2f}l")







