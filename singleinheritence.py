""" class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname,self.lname)

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self,fname,lname)

x = Student("Krutarth","Bari")
x.printname() """

class Manager:
    def __init__(self):
        self.name = "Krutarth"
        self.empid = 1001
        self.designation = "Manager"
        self.package = "5 LPA" 

    def show(self):
        print(f"name: {self.name}\n employee id: {self.empid}\n designation:{self.designation}\n package:{self.package}")

class Executive(Manager):
    """ def __init__(self,name1,empid1,des,pk):
        Manager.__init__(self)
        self.name1 = name1
        self.empid1 = empid1
        self.designation = des
        self.package = pk
        self.reporting = self.name,self.empid """
    
    def edata(self):
        
        self.name1 = "riya"
        self.empid1 = 1005
        self.designation = "HR"
        self.package = "3 LPA"
        self.reporting = self.name,self.empid

    def display(self):
        print(f"name: {self.name}\n employee id: {self.empid}\n designation:{self.designation}\n package:{self.package}\n reports to:{self.reporting}")
    
m1 = Manager()
m1.show()
#e1 = Executive("riya",1005,"developer","3 LPA")
e1 = Executive()
e1.edata()
e1.display()
print(Executive.mro())


                     
        
        