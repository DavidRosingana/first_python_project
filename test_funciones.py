
def input_user(pregunta):
    confirmacion = False
    dato_user = ""
    while not confirmacion:
        dato_user = input(pregunta).capitalize()
        seguro = input("Has dicho {}, seguro? ".format(dato_user))
        if seguro == "si":
            confirmacion = True
    return dato_user

nombre = input_user("Como te llamas? ")
print("Has confirmado que te llamas {} ".format(nombre))

def reverse_str():
    str_to_reverse = input("Di tu frase: ")
    str_reversed = ""
    indice = len(str_to_reverse) - 1
    while indice >= 0:
       str_reversed += str_to_reverse[indice]
       indice -= 1
    return str_reversed

string_final = reverse_str()
print(string_final)
