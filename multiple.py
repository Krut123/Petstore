class Employee:
    def __init__(self,name):
        self.name = name

    def info(self):
        print("name:",self.name)

class Dancer:
    def __init__(self,dancetype):
        self.dance = dancetype

    def info(self):
        print("name:",self.name)
        print("dance style:",self.dance)

class DancerEmpl(Dancer,Employee):
    def __init__(self, dancetype,name):
        Dancer.__init__(self,dancetype)
        Employee.__init__(self,name)

d2 = DancerEmpl("Kathak","Rani")
d2.info()


class Father:
    def __init__(self,name,age,village):
        self.name = name
        self.age = age
        self.village = village

    def fdisplay(self):
        print(f"father name: {self.name}\n father age: {self.age}\n father village{self.village}")

class Mother:
    def __init__(self,name,age,village):
        self.name = name
        self.age = age
        self.village = village

    def mdisplay(self):
        print(f"mother name: {self.name}\n mother age: {self.age}\n mother village{self.village}")
           
           
class Child(Father,Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)

    def cdata(self):
        self.name = "rohot"
        self.age = 10

    def display(self):
        print(f"child name: {self.name}\n child age: {self.age}\n child village{self.village}")
        
       
       
m1 = Mother("seema",55," UP")
m1.display()
f1 = Father("ramesh",55," UP")
f1.display()
c1 = Child("tom",10,"UP")
c1.display()
        
            


    
        
        
        