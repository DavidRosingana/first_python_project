"""
Crea un programa que calcule la media de los elementos de la lista de números
introducida por el usuario (media = suma de todos los numeros / numero de numeros )

# Números usuario
numeros = [11, 21, 3, 42, 3, 2]
# Output
media = 13.666666666666666

"""
lista_numero = []
numero = ""
n_lista = len(lista_numero)
n_max = int(input("De cuantos numeros harás la lista? "))
sumatorio = 0
media = None

#crear lista

while n_lista < n_max:
    numero = input("añada un numero: ")
    while not numero.isdigit():
        numero = input("añada un numero: ")
    lista_numero.append(int(numero))
    print("numero añadido correactamente")
    n_lista += 1

print("Esta es tu lista:", lista_numero)

for item in lista_numero:
    sumatorio += item
    media = sumatorio/n_lista

print("la media es: ", media)
