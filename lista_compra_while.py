mi_lista=[]

input_user = ""

input_user = input("Qué quieres comprar?\n(escribe FIN para salir)\n ")

while input_user != "FIN":
    mi_lista.append(input_user)
    input_user = input("Qué quieres comprar?\n(escribe FIN para salir)\n ")

for item in mi_lista:
    print("Mi lista para comprar es: {}".format(item))

