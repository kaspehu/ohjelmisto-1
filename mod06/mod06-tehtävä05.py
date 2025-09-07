
def kokonaislukulista(lista):
    for n in lista:
        if n % 2 != 0:
            print(n)

lista = [55, 66, 77, 88]
print(lista)
kokonaislukulista(lista)