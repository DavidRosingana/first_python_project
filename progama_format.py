"""
Crear un programa que le repita al usuario todo lo que dice pero con todas las vocales cambiadas por i.
"""

vocales = ["a", "e", "i", "o", "u"]
string = input("Di tu frase: ")


for item in string:
    if item in vocales:
        string = string.replace(item, "i")

print(string)