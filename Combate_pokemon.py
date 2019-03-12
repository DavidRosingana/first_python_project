print("Simulador de combates. En este combate controlaras a un Pikachu")
print("Puedes combatir contra Casado, Rivera o Santi")

rival_elegido = input("Contra quien quieres combatir:").capitalize()
vida_pikachu = 100
vida_enemigo = 0

if rival_elegido == "Casado":
    vida_enemigo = 100
elif rival_elegido == "Rivera":
    vida_enemigo = 100
elif rival_elegido == "Santi":
    vida_enemigo = 100
else:
    vida_enemigo = 1
    print("has elegido al pokemon auxiliar Metapod")

while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_pikachu = input("Que ataque quieres elegir:\n(Pikachu puede usar chispazo y bola voltio)").capitalize()
    if ataque_pikachu == "Chispazo":
        print("Pikachu usó:", ataque_pikachu)
        vida_enemigo -= 10

    if ataque_pikachu == "Bola voltio":
        print("Pikachu usó:", ataque_pikachu)
        vida_enemigo -= 12

    print("Vida del enemigo", vida_enemigo)

    if rival_elegido == "Casado":
        print("Casado usó ataque aborto")
        vida_pikachu -= 8

    if rival_elegido == "Rivera":
        print("Rivera usó ataque neoliberalismo")
        vida_pikachu -= 1

    if rival_elegido == "Santi":
        print("Santi usó ataque ESPAÑA")
        vida_pikachu -= 5
    print("Vida de Pikachu:", vida_pikachu)

if vida_enemigo <= 0:
    print("Pikachu ha roto ESPAÑA")
else:
    print("El separatista Pikachu ha muerto")
print("\ncombate finalizado")
