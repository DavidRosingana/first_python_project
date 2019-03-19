
class Dog:
    def __init__(self, name, specie, age):
        self.name = name
        self.specie = specie
        self.age = age

    def speak(self):
        print("Wof Wof")

my_dog = Dog("Doggy", "Bulldog", 13)
my_dog2 = Dog("Cat", "Caniche", 2)
my_dog3 = Dog("Luko", "Huskye", 13)


my_dog