#Crea un programa que encuentre el número más grande de una serie de 10 números introducidos por el usuario.

lista = []
numero = ""
n_lista = len(numero)

while n_lista < 10:
    numero = input(("Especifica un numero: "))
    while not numero.isdigit():
        numero = input(("Especifica un numero: "))
    lista.append(int(numero))
    print("numero añadido correactamente")
    n_lista += 1

print("Esta es tu lista:\n {}".format(lista))

numero_mayor = lista[0]

for item in lista:
    if item > numero_mayor:
        numero_mayor = item

print(numero_mayor)