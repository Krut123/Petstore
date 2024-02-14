class Student:
    schoolname = "ABC School"
    def __init__(self,name,age) :
        self.name=name
        self.a = age

s1=Student("krut",20)
print(s1.name,s1.a)

print(Student.schoolname)
print(s1.schoolname)
s2 = Student("Ram",20)
print(s2.name,s2.a,s2.schoolname)


class Employee:
    comp_name="Apple"
    increment=1.5
    def __init__(self,name,salary,occupation="HR"):
        self.name=name
        self.salary=salary
        self.occ=occupation
    def show(self):
        print(f"My name is {self.name} and my salry is{self.salary}")

    def increase(self):
        self.salary = self.salary * self.increment
        
emp1=Employee("Ron",2000)
emp1.show()
print(emp1.comp_name)

e2 = Employee("sarika",30000,"clerk")
e2.show()
e3 = Employee("rani",25000,"accountant")
e3.show()
emp1.increase()
emp1.show()
e2.increment = 2.0
e2.increase()
e2.show()
print(Employee.increment)


        