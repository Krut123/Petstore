class Animal:
    def __init__(self,name,species) -> None:
        self.name = name
        self.species=species
        
    def makeSound(self):
        print("Sound made by the animal")
        
class Dog(Animal):
    def __init__(self, name, breed) -> None:
        Animal.__init__(self,name,species="Dog")
        self.breed =breed
        
    def makeSound(self):
        print(f"{self.breed} {self.species} Barks")

class Cat(Animal):
    def __init__(self, name, breed) -> None:
        Animal.__init__(self,name,species="Cat")
        self.breed =breed
        
    def makeSound(self):
        print(f"{self.breed} {self.species} Meeos")
  
d1 = Dog("Tob","Permerian")
d1.makeSound()    
a1 =Animal("Tob","Dog")
a1.makeSound()
c1=Cat("Kitty","Persian")
c1.makeSound()

        
        