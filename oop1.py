class Employee:
    name = "john"
    salary = 40000

    def info(self):
        print(f"my name is {self.name} and salary is {self.salary}")
    
    def show(abc):
        print(f"my name is {abc.name}")


#creating object
#obj1 = classname()

e1 = Employee()
print(e1)
print(e1.name)
print(e1.salary)

e2 = Employee()
e2.name = "krutarth"
e2.salary = 50000
print(e2)
print(e2.name)


""" print(Employee.__doc__)
help(Employee) """ 
e1.info()
e2.info()
e1.show()
e2.show()




