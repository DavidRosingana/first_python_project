"""
obetener el tipo de dato de cada dato de una lista
"""

lista = ["rwgetsgbv", 4, "dsfgsdgdsfg", "dsf", 3, "hola", 6, "True"]

lista_dat = []
lista_str = []

for item in lista:
    if type(item) == int:
        lista_dat.append(item)
    else:
        lista_str.append(item)

print(lista_dat)
print(lista_str)

