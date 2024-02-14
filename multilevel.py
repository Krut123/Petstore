class Animal:
    def __init__(self,name,species):
        self.name = name;
        self.species = species;

    def info(self):
        print(f"{self.name} is {self.species}")

class dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name,species = "dog")
        self.breed = breed

    def info(self):
        Animal.info(self)
        print(f"{self.breed} is {self.species} that barks")

class doberman(dog):
    def __init__(self, name, color):
        dog.__init__(self,name,breed="doberman")
        self.color = color
    def info(self):
        dog.info(self)
        print(f"color: {self.color}")

""" d1 = dog("twitter","doberman")
d1.info() """
obj1 = doberman("twitter","brown")
obj1.info()

        
        




class Cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name,species = "Cat")
        self.breed = breed

    def info(self):
        Animal.info(self)
        print(f"{self.breed} is {self.species} that meow")

class Gavthi(dog):
    def __init__(self, name, color):
        Cat.__init__(self,name,breed="gavthi")
        self.color = color
    def info(self):
        Cat.info(self)
        print(f"color: {self.color}")

obj1 = Gavthi("pari","brown")
obj1.info()