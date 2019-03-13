"""
CALCULO DE LA TABLA DE MULTIPLICAR DE UN NUMERO DADO
"""

numero = int(input("di un numero: "))

for multiplo in range(11, 0, -1):
    print("{} * {} = {}".format(numero, multiplo, numero * multiplo))