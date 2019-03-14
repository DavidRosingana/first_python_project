"""
Dada una lista de enteros:
sustituir los multiplos de 3 por Fizz y los multiplos de 5 por un Buzz
multiplos de 3 y de 5 se sustituyen por un D10S

"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 20, 15, 30, 60, 70]

for i in range(len(numeros)):
    numero = numeros[i]
    if numero % 3 == 0 or numero % 5 == 0:
        numeros[i] = ""

        if numero % 3 == 0 and numero % 5 == 0:
            numeros[i] += "D10S"

        elif numero % 3 == 0:
            numeros[i] += "Fizz"

        elif numero % 5 == 0:
            numeros[i] += "Buzz"

print(numeros)
