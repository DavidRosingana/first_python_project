from pokemon.combate_pokemon_obj import Charmander, Squirtle, Bulbasaur, Pikachu

"""
while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_pikachu = input("Que ataque quieres elegir:\n(Pikachu puede usar Chispazo y Bola voltio) ").capitalize()

    print("{} usó: {} ".format(nombre_rival, nombre_ataque))
    print("Vida de {} = {} ".format(nombre_rival, vida_enemigo))

    vida_pikachu -= dano_enemigo
    print("Vida de Pikachu = ", vida_pikachu)

if vida_enemigo <= 0:
    print("Pikachu ha roto ESPAÑA")
else:
    print("El separatista Pikachu ha muerto")
print("\ncombate finalizado")
"""


def choose_pokemon():
    print("Puedes combatir contra Charmander, Squirtle o Bulbasaur")
    chosen_pokemon = input("Contra quién quieres combatir? ").capitalize()

    if chosen_pokemon == "Charmander":
        return Charmander()

    elif chosen_pokemon == "Squirtle":
        return Squirtle()

    elif chosen_pokemon == "Bulbasaur":
        return Bulbasaur()


def main():
    enemy = choose_pokemon()
    pikachu = Pikachu()

    while not enemy.is_defeated and Pikachu.is_defeated():
        chosen_attack = input("Que ataque quieres elegir:\n(Pikachu puede usar Rayo y Trueno) ").capitalize()
        pikachu.fight(enemy, chosen_attack)
        enemy.show_hp()
        enemy.fight(pikachu)
        pikachu.show_hp()

    if enemy.is_defeated():
        print("Has ganado")

    elif pikachu.is_defeated():
        print("Has perdido")


if __name__ == "__main__":
    main()
