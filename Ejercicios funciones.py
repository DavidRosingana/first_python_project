"""

Ejercicio 1

    Escribe una función que encuentre el numero más grande entre 3 numeros.

Ejercicio 2

    Escribe una funcion que dado un numero y un rango (otros dos numeros), compruebe que ese numero está entre los dos (dentro del rango).

    numero_en_rango(10, 1, 100) # Devuelve True
    numero_en_rango(101, 1, 100) # Devuelve False

Ejercicio 3

    Escribe una función que reciba una lista de números y devuelva otra pero conteniendo solo los números pares.

    devolver_pares([1, 2, 3, 4, 5, 6])
    [2, 4, 6]

"""


def numero_mayor():
    numero_max = 0
    primero = int(input("Dame el primer numero: "))
    segundo = int(input("Dame el segundo numero: "))
    tercero = int(input("Dame el tercer numero: "))
    if primero > numero_max:
        numero_max = primero

    if segundo > numero_max:
        numero_max = segundo

    if tercero > numero_max:
        numero_max = tercero

    return numero_max

def numero_en_rango(a, i, f):
    if a >= i and a <= f:
        print("True")
    else:
        print("False")



ej_1 = False
if ej_1 == True:
    print(numero_mayor())

ej_2 = False
if ej_2 == True:
    print(numero_en_rango(1, 3, 10))


