class Animal:
    def __init__(self, name, species, speak="Animal sound"):
        self.name = name
        self.species = species
        self.speak = speak

    def __repr__(self):
        return f"I'm an animal named {self.name}, my species is {self.species}."

    def make_sound(self):
        print(f'{self.name} says, {self.speak}')
    
class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name, 'Mammal', 'I am a Mammal!')

    def give_birth(self):
        print(f'{self.name} has given birth!')

class Primate(Mammal):
    def __init__(self, name):
        Mammal.__init__(self)

    def climb_trees(self):
        print(f"I'm a {self.species} and I'm climbing a tree!")

class Marsupial(Mammal):
    def __init__(self, name):
        Mammal.__init__(self, name)

    def carry_baby(self):
        print(f"I'm a {self.name} and I'm carrying a baby!")

class Bird(Animal):
    def __init__(self, name, wingspan=2.5):
        super().__init__(name, "Bird", "I am a Bird!")
        self.wingspan = wingspan

class Reptile(Animal):
    def __init__(self, name):
        super().__init__(name, "Reptile", "I am a Reptile!")

    def bask_in_sun(self):
        print(f'My name is {self.name} and I am basking in the sun...')

class Aviary():
    def __init__(self):
        self.birds = []
        self.birds.append(Bird(self.name))

    


# elephant = Mammal('elephant')
# print(elephant)
# elephant.give_birth()
# elephant.make_sound()
parrot = Bird('bob', '27 feet')
# print(parrot.wingspan)
# mini = Marsupial("mini")
# mini.carry_baby()
print(Aviary.birds, list)