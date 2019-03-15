"""
Ejercicio 4

Crea una función que muestre por pantalla un texto y tantas barritas de subrayado como larga sea la string.

mostrar_titulo_subrayado("Hola mundo")

Hola mundo
----------
"""
def subrayado():
    frase = input("Di tu frase: ")
    rayas = ""
    longitud = len(frase)
    while longitud > len(rayas):
        rayas += "-"
    print(frase)
    print(rayas)
    return

(subrayado())