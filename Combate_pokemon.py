print("Simulador de combates. En este combate controlaras a un Pikachu")
print("Puedes combatir contra Casado, Rivera o Santi")

rival_elegido = input("Contra quien quieres combatir:").capitalize()
vida_pikachu = 100

if rival_elegido == "Casado":
    vida_enemigo = 100
    nombre_rival = "Casado"
    dano_enemigo = 12
elif rival_elegido == "Rivera":
    vida_enemigo = 100
    nombre_rival = "Rivera"
    dano_enemigo = 8
elif rival_elegido == "Santi":
    vida_enemigo = 100
    nombre_rival = "Santi"
    dano_enemigo = 9
else:
    vida_enemigo = 1
    nombre_rival = "Metapod"
    dano_enemigo = 0
    print("Has elegido al pokemon auxiliar Metapod")

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_pikachu = input("Que ataque quieres elegir:\n(Pikachu puede usar chispazo y bola voltio) ").capitalize()
    if ataque_pikachu == "Chispazo":
        dano_pikachu = 8
        print("Pikachu usó:", ataque_pikachu)
        vida_enemigo -= dano_pikachu

    elif ataque_pikachu == "Bola voltio":
        dano_pikachu = 12
        print("Pikachu usó:", ataque_pikachu)
        vida_enemigo -= dano_pikachu

    print("Vida de {} = {} ".format(nombre_rival, vida_enemigo))

    vida_pikachu -= dano_enemigo
    print("Vida de Pikachu = ", vida_pikachu)

if vida_enemigo <= 0:
    print("Pikachu ha roto ESPAÑA")
else:
    print("El separatista Pikachu ha muerto")
print("\ncombate finalizado")
