class Pet:
    def __init__(self, name=None):
        self.name = name


class Dog(Pet):
    def __init__(self, name=None, breed=None):
        super().__init__(name)
        self.breed = breed

    def say(self):
        return '{}: waw'.format(self.name)


dog = Dog('Шарик', 'asd')
print(dog.name)
print(dog.breed)
print(dog.say())