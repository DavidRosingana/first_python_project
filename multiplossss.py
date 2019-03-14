"""
Crear un programa que guarde e imprima varias listas con todos los números que estén dentro de una
lista proporcionada por el usuario y sean múltiplos de 2, de 3, de 5 y de 7.

Ejemplo:

input = [1, 10, 70, 30, 50, 55]

multiplos_dos = [10, 70, 30, 50]
multiplos_tres = [30]
multiplos_cinco = [10, 70, 30, 60, 55]
multiplos_siete = [70]
"""

numeros = []
multiplos_dos = []
multiplos_tres = []
multiplos_cinco = []
multiplos_siete = []

while len(numeros) <= 5:
    numeros.append(int(input("añada numeros a la lista: ")))

for i in range(len(numeros)):
    numero = numeros[i]

    if numero % 2 == 0:
        multiplos_dos.append(int(numero))

    if numero % 3 == 0:
        multiplos_tres.append(int(numero))

    if numero % 5 == 0:
        multiplos_cinco.append(int(numero))

    if numero % 7 == 0:
        multiplos_siete.append(int(numero))

print(multiplos_dos)
print(multiplos_tres)
print(multiplos_cinco)
print(multiplos_siete)