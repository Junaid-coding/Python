class Dog:
    species = 'mammal'
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
Tom = Dog("Tom", "Husky")
Nick = Dog("Nick", "Labrador")
print("Tom is a {}".format(Tom.species))
print("Nick is also a {}".format(Nick.species))
print("{} is a {}".format(Tom.name, Tom.breed))
print("{} is a {}".format(Nick.name, Nick.breed))