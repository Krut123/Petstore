""" class student:
    def __init__(self,name,eng,math):
        self.name = name
        self.eng = eng
        self.math = math
    
    def _add__(self,other):
        return "total marks of each subject ",self.eng + other.eng,self.math+other.math
    
    def __sub__(self,other):
        return "total marks of each subject: ",self.eng + other.eng,self.math+other.math """
    

class employee:
    def __init__(self,name,age,package):
        self.name = name
        self.age = age
        self.package = package

    def __ge__(self,other):
        if self.age>other.age:
            return f"{self.name}'s age is greater than {other.name}'s age"
        else:
            return f"{other.name}'s age is greater than {self.name}'s age"
        

    def __le__(self,other):
        if self.package<other.package:
            return f"{self.name}'s package is less than {other.name}'s package"
        else:
            return f"{other.name}'s package is less than {self.name}'s package"
        
e1 = employee("vicky",25,300000)
e2 = employee("rocky",30,400000)

print(e1>=e2)
print(e1<=e2)

        