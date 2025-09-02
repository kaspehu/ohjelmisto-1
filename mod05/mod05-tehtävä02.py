
# oma versio, olettaa, että syötetään väh. 5 lukua
app_running = True

luku = [] # Määritetään tyhjä lista myöhempää varten

while app_running:
    user_input = input("Anna kokonaisluku tai lopeta painamalla enter: ")
    if user_input.isdigit():
        number = int(user_input)
        luku.append(number)
    elif user_input == "":
        for i in range(5):
            luku.sort(reverse = True)
            print(luku[i])
            app_running = False
    else:
        print("Et syöttänyt kokonaislukua: ")




"""
luvut = []
n = input("Anna luku, paina enter lopettaaksesi: ")
while n != "":
    print(n)
    luvut.append(int(n))
    n = input("Anna luku, tyhjä lopettaa: ")

luvut.sort(reverse = True)
print(luvut)

viisi_suurinta = luvut[:5]

for v in viisi_suurinta:
    print(v)
"""


