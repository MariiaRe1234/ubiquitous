class Animal:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Dog(Animal):
    type = 'dog'


class Hamster(Animal):
    type = 'hamster'


class Human:

    def __init__(self, name, age=None):
        self.name = name
        self.age = age
        self.pets = []

    def get_name_age(self):
        return self.name, self.age


pet3 = Hamster('Niko')
person = Human('Brian', 22)
person.pets.append(pet3)
person.pets.append(Hamster('Emi'))

print(person.name)
print(pet3.type)









n = 300


while True:
    print(input('Please enter your account ID: '))
