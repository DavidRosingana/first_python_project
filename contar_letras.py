#PROGRAMA QUE CUENTA VOCALES Y CONSONANTES DE UNA FRASE INTRODUCIDA POR EL USUARIO

vocales = ["a" , "e" , "i" , "o" , "u"]
puntuacion = [" ", ".", ","]
n_vocales = 0
n_consonantes = 0
n_puntuacion = 0


frase = input("di tu frase: ")
for item in frase:
    if item in vocales:
        n_vocales += 1
    elif item in puntuacion:
        n_puntuacion += 1
    else:
        n_consonantes += 1

print("el numero de consonantes es {}".format(n_consonantes))
print("el numero de vocales es {}".format(n_vocales))
print("el numero de puntos y comas y hostias es {}".format(n_puntuacion))