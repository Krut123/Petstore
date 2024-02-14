class Employee:
    comp_name="Apple"
    increment=1.5
    no_of_leaves = 8
    no_of_emp = 0
    def __init__(self,name,salary,occupation="HR"):
        self.name=name
        self.salary=salary
        self.occ=occupation
        Employee.no_of_emp += 1
    def show(self):
        print(f"My name is {self.name} and my salry is{self.salary}")

    def increase(self):
        self.salary = self.salary * self.increment

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves
        
emp1=Employee("Ron",2000)
emp1.show()
print(emp1.comp_name)

e2 = Employee("sarika",30000,"clerk")
e2.show()
e3 = Employee("rani",25000,"accountant")
e3.show()
print(Employee.no_of_leaves)
Employee.change_leaves(12)
print(emp1.no_of_leaves)
print(Employee.no_of_leaves)
print(e2.no_of_leaves)
e3.change_leaves(10)
print(e3.no_of_leaves)
print(Employee.no_of_leaves)
print("total no. of employee",Employee.no_of_emp)

