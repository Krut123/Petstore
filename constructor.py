""" class student:
    def __init__(self,name,course):
        print("hii iam an object")
        self.name = name
        self.crse = course
        print(self.name,self.crse)

s1 = student("krut","FSD")
s2 = student("madhav","DSE") """

    



class student1:
    name = "john"
    age = 30

    def __init__(self): #default constructor
        print("program executing")

    def info(self):
        print(f"{self.name} is {self.age} year old")
    
s1 = student1()
s1.info()
s2 = student1()
s2.name = "rocky"
s2.age = 40
s2.info()
