@staticmethod
def isopen(day):
    if day == "sunday":
        return "closed"
    else:
        return "open"
    
emp1 = Employee("Ron",50000)
emp1.show()
print(emp1.comp_name)
e2 = Employee("Sarika",30000,"Clerk")
e2.show()
e3 = Employee("Rani",25000,"Accountant")
print(e2.isopen("SUnday"))
print(Employee.isopen("Friday"))