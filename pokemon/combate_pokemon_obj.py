class BasePokemon:
    base_hp = 100
    damage = 10
    name = "Pokemon"
    attacks = []

    def __init__(self):
        self.hp = self.base_hp

    def fight(self, enemy, attack_name=None):
        print("{} ataca a {} con {}".format(self.name, enemy.name, attack_name if attack_name else "su ataque base"))
        if not attack_name:
            enemy.take_damage(self.damage)
        else:
            for attack in self.attacks:
                if attack.name ==attack_name:
                    enemy.take_damage(attack.damage)
                    return

    def take_damage(self, damage):
        self.hp -= damage

    def show_hp(self):
        print("Vida de {} = {}".format(self.name, self.hp))

    def is_defeated(self):
        return self.hp <= 0


class BasePokemonAttack():
    name = ""
    damage = 0


class TruenoAttack(BasePokemonAttack):
    name = "Trueno"
    damage = 15


class RayoAttack(BasePokemonAttack):
    name = "Rayo"
    damage = 10


class Charmander(BasePokemon):
    base_hp = 100
    damage = 10
    name = "Charmander"


class Squirtle(BasePokemon):
    base_hp = 110
    damage = 9
    name = "Squirtle"


class Bulbasaur(BasePokemon):
    base_hp = 120
    damage = 8
    name = "Bulbasaur"


class Pikachu(BasePokemon):
    base_hp = 90
    damage = 11
    name = "Pikachu"
    attacks = [RayoAttack, TruenoAttack]

