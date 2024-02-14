class person:
    name = "krutarth"
    age = 20
    gender = "male"

    def sleep(self):
        print(f"{self.name} sleep")
    
    def eat(self):
        print(f"{self.name} can eat")

    def walk(self):
        print(f"{self.name} can walk")

p1 = person
p1.name()
p1.age()
p1.gender()


