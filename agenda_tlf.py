

salida = False
agenda = dict()

while not salida:
    accion = input("Qué quieres hacer? [A] Añadir numero / [C] Consultar numero / Salir [S]: ").capitalize()
    if accion == "A":
        print("Añadir numero")
        print("-------------")
        nombre = input("Nombre: ")
        numero = input("Numero: ")
        agenda[nombre] = numero

    elif accion == "C":
        print("Consultar numero")
        print("----------------")
        nombre = input("Nombre del contacto: ")
        print(agenda[nombre])

    elif accion == "S":
        salida = True
