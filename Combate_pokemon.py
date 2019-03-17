print("Simulador de combates Pokemon por España.")
elecc = input("Elige a tu Pokemon ").capitalize()
if elecc == "Pikachu":
    print("Has elegido a Pikachu ")
else:
    print("No tenemos a ese Pokemon, se te asignará un Pikachu")

print("Puedes combatir contra Casado, Rivera o Santiago")

rival_elegido = input("Contra quién quieres combatir? ").capitalize()
vida_pikachu = 100

if rival_elegido == "Casado":
    vida_enemigo = 100
    nombre_rival = "Casado"
    dano_enemigo = 12
    nombre_ataque = "Titulo de master"

elif rival_elegido == "Rivera":
    vida_enemigo = 100
    nombre_rival = "Rivera"
    dano_enemigo = 8
    nombre_ataque = "Feminismo liberal"

elif rival_elegido == "Santiago":
    vida_enemigo = 100
    nombre_rival = "Santiago"
    dano_enemigo = 9
    nombre_ataque = "No somos fachas, pero..."

else:
    vida_enemigo = 100000000000
    nombre_rival = "Trump"
    dano_enemigo = 99
    nombre_ataque = "DESTRUCCIÓN INFINITA"
    print("Hala, por listo vas a combatir contra {}".format(nombre_rival))

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_pikachu = input("Que ataque quieres elegir:\n(Pikachu puede usar Chispazo y Bola voltio) ").capitalize()
    if ataque_pikachu == "Chispazo":
        dano_pikachu = 10
        print("Pikachu usó:", ataque_pikachu)
        vida_enemigo -= dano_pikachu

    elif ataque_pikachu == "Bola voltio":
        dano_pikachu = 12
        print("Pikachu usó:", ataque_pikachu)
        vida_enemigo -= dano_pikachu

    else:
        dano_pikachu = 8
        print("Pikachu usó: combate")
        vida_enemigo -= dano_pikachu
        print("Pikachu se hirió a si mismo")
        vida_pikachu -= 3

    print("{} usó: {} ".format(nombre_rival, nombre_ataque))
    print("Vida de {} = {} ".format(nombre_rival, vida_enemigo))

    vida_pikachu -= dano_enemigo
    print("Vida de Pikachu = ", vida_pikachu)



if vida_enemigo <= 0:
    print("Pikachu ha roto ESPAÑA")
else:
    print("El separatista Pikachu ha muerto")
print("\ncombate finalizado")
