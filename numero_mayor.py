numero_magico = 3

numero_intentos=0

numero_user = int(input("Adivina mi numero, tienes 5 intentos: "))

if numero_magico == numero_user:
    print("win")
elif numero_intentos != numero_magico:
    while numero_intentos < 5:
        numero_user = int(input("otra oportunidad: "))
        if numero_user == numero_magico:
            print("win")
            break
        else:
            numero_intentos += 1
else:
    print("lose")
